from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Protocol

from interaction_kernel.errors import IKError
from interaction_kernel.models import new_receipt

PUBLICATION_PROFILE = "kristal.publication.request"
REVOCATION_PROFILE = "kristal.publication.revoke.request"
PUBLICATION_ARTIFACT_TYPE = "kristal.publication_bundle"


@dataclass(frozen=True)
class PublicationResult:
    uckk_object_id: str
    state: str = "published"
    external_reference: str | None = None
    data: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class RevocationResult:
    uckk_object_id: str
    state: str = "revoked"
    external_reference: str | None = None
    data: Mapping[str, Any] | None = None


class UckkKristalPublicationPort(Protocol):
    """UCKK-owned implementation boundary.

    The port may resolve the immutable ArtifactRef itself or delegate resolution to
    a local artifact access layer. IK never becomes the artifact store.
    """

    def publish(
        self,
        *,
        publication_id: str,
        kristal_id: str,
        kristal_version: str,
        channel: str,
        artifact_ref: Mapping[str, Any],
        supersedes_publication_id: str | None,
        metadata: Mapping[str, Any],
    ) -> PublicationResult: ...

    def revoke(
        self,
        *,
        publication_id: str,
        reason: str,
        replacement_publication_id: str | None,
    ) -> RevocationResult: ...


class UckkKristalPublicationAdapter:
    """Reference IK↔UCKK mapping with replay protection.

    Production deployments should persist the idempotency ledger. This reference
    implementation keeps it in memory so the required semantics remain explicit
    and testable without turning IK into operational storage.
    """

    def __init__(self, port: UckkKristalPublicationPort) -> None:
        self._port = port
        self._replays: dict[str, tuple[tuple[Any, ...], dict[str, Any]]] = {}

    @staticmethod
    def _profile_id(envelope: Mapping[str, Any]) -> str:
        profile = envelope.get("profile")
        if not isinstance(profile, Mapping):
            raise IKError("IK_INVALID_ENVELOPE", "profile is required")
        return str(profile.get("id") or "")

    @staticmethod
    def _assert_route(envelope: Mapping[str, Any], profile_id: str) -> None:
        if UckkKristalPublicationAdapter._profile_id(envelope) != profile_id:
            raise IKError("IK_INVALID_ENVELOPE", f"expected profile {profile_id}")
        source = envelope.get("source") or {}
        target = envelope.get("target") or {}
        if source.get("system") != "daat" or target.get("system") != "uckk":
            raise IKError("IK_TARGET_NOT_FOUND", "UCKK publication route must be daat -> uckk")
        if not envelope.get("idempotency_key"):
            raise IKError("IK_INVALID_ENVELOPE", "idempotency_key is required")

    @staticmethod
    def _publication_artifact(envelope: Mapping[str, Any]) -> Mapping[str, Any]:
        refs = envelope.get("artifact_refs") or []
        matches = [r for r in refs if isinstance(r, Mapping) and r.get("artifact_type") == PUBLICATION_ARTIFACT_TYPE]
        if len(matches) != 1:
            raise IKError(
                "IK_INVALID_ENVELOPE",
                "kristal publication requires exactly one kristal.publication_bundle ArtifactRef",
            )
        artifact = matches[0]
        integrity = artifact.get("integrity")
        if not isinstance(integrity, Mapping) or integrity.get("algorithm") != "sha256" or not integrity.get("digest"):
            raise IKError("IK_INVALID_ENVELOPE", "publication ArtifactRef requires sha256 integrity")
        locator = artifact.get("locator")
        if not isinstance(locator, Mapping) or not locator.get("ref"):
            raise IKError("IK_INVALID_ENVELOPE", "publication ArtifactRef requires an opaque locator")
        return artifact

    def _replay_or_store(
        self,
        *,
        key: str,
        signature: tuple[Any, ...],
        invoke: Any,
    ) -> dict[str, Any]:
        prior = self._replays.get(key)
        if prior is not None:
            prior_signature, prior_receipt = prior
            if prior_signature != signature:
                raise IKError("IK_IDEMPOTENCY_CONFLICT", "idempotency key was reused for a different UCKK operation")
            return prior_receipt
        receipt = invoke()
        self._replays[key] = (signature, receipt)
        return receipt

    def handle(self, envelope: Mapping[str, Any]) -> dict[str, Any]:
        profile_id = self._profile_id(envelope)
        if profile_id == PUBLICATION_PROFILE:
            return self.handle_publication(envelope)
        if profile_id == REVOCATION_PROFILE:
            return self.handle_revocation(envelope)
        raise IKError("IK_UNKNOWN_PROFILE", f"UCKK adapter does not handle {profile_id}")

    def handle_publication(self, envelope: Mapping[str, Any]) -> dict[str, Any]:
        self._assert_route(envelope, PUBLICATION_PROFILE)
        artifact = self._publication_artifact(envelope)
        data = envelope.get("data") or {}
        publication_id = str(data.get("publication_id") or "")
        kristal_id = str(data.get("kristal_id") or "")
        kristal_version = str(data.get("kristal_version") or "")
        channel = str(data.get("channel") or "")
        supersedes = data.get("supersedes_publication_id")
        metadata = data.get("metadata") if isinstance(data.get("metadata"), Mapping) else {}
        digest = (artifact.get("integrity") or {}).get("digest")
        signature = (PUBLICATION_PROFILE, publication_id, kristal_id, kristal_version, channel, digest, supersedes)
        key = str(envelope["idempotency_key"])

        def invoke() -> dict[str, Any]:
            result = self._port.publish(
                publication_id=publication_id,
                kristal_id=kristal_id,
                kristal_version=kristal_version,
                channel=channel,
                artifact_ref=artifact,
                supersedes_publication_id=supersedes if isinstance(supersedes, str) else None,
                metadata=metadata,
            )
            return new_receipt(
                interaction_id=str(envelope["id"]),
                source={"system": "uckk"},
                target={"system": "daat"},
                status="succeeded",
                retryable=False,
                external_reference=result.external_reference or result.uckk_object_id,
                correlation_id=envelope.get("correlation_id"),
                data={
                    "publication_id": publication_id,
                    "uckk_object_id": result.uckk_object_id,
                    "state": result.state,
                    **dict(result.data or {}),
                },
            )

        return self._replay_or_store(key=key, signature=signature, invoke=invoke)

    def handle_revocation(self, envelope: Mapping[str, Any]) -> dict[str, Any]:
        self._assert_route(envelope, REVOCATION_PROFILE)
        data = envelope.get("data") or {}
        publication_id = str(data.get("publication_id") or "")
        reason = str(data.get("reason") or "")
        replacement = data.get("replacement_publication_id")
        signature = (REVOCATION_PROFILE, publication_id, reason, replacement)
        key = str(envelope["idempotency_key"])

        def invoke() -> dict[str, Any]:
            result = self._port.revoke(
                publication_id=publication_id,
                reason=reason,
                replacement_publication_id=replacement if isinstance(replacement, str) else None,
            )
            return new_receipt(
                interaction_id=str(envelope["id"]),
                source={"system": "uckk"},
                target={"system": "daat"},
                status="succeeded",
                retryable=False,
                external_reference=result.external_reference or result.uckk_object_id,
                correlation_id=envelope.get("correlation_id"),
                data={
                    "publication_id": publication_id,
                    "uckk_object_id": result.uckk_object_id,
                    "state": result.state,
                    **dict(result.data or {}),
                },
            )

        return self._replay_or_store(key=key, signature=signature, invoke=invoke)
