# Kristal publication to UCKK

UCKK publication is an optional Interaction Kernel flow. The canonical Kristal remains upstream; UCKK receives a publication projection and owns only its local publication lifecycle.

## Roles

| Component | Responsibility |
|---|---|
| Kristal | canonical knowledge artifact/release semantics |
| kOA Mediatheque | may own immutable publication bundle bytes and SHA-256 |
| Da'at | IK admission/orchestration at the Kristal boundary |
| IK | command/event/reference transport and reliability semantics |
| UCKK adapter | maps IK publication lifecycle into the UCKK participant API |
| UCKK | owns the UCKK-local publication object |

## Publish

Da'at sends `kristal.publication.request/1.0.0` to `uckk`. The envelope must include exactly one `ArtifactRef` whose `artifact_type` is `kristal.publication_bundle`. The reference must carry SHA-256 integrity and an opaque locator. The `ArtifactRef.owner.system` may be `mediatheque-koa`; transport through Da'at does not transfer artifact ownership.

`supersedes_publication_id` creates a replacement relationship. The old publication remains historical/provenance state.

A successful UCKK implementation returns a final Receipt containing `publication_id`, `uckk_object_id` and state, and may emit `kristal.publication.available/1.0.0`.

## Revoke

Da'at sends `kristal.publication.revoke.request/1.0.0`. UCKK revokes its local projection and preserves the historical mapping. A replacement may be named with `replacement_publication_id`. UCKK may emit `kristal.publication.revoked/1.0.0`.

Revocation never deletes or rewrites the canonical Kristal corpus or source media.

## Idempotency

Publication and revocation commands require an idempotency key. A replay with the same semantic operation returns the prior result; a divergent operation under the same key is rejected with `IK_IDEMPOTENCY_CONFLICT`.

The reference adapter uses an in-memory replay ledger for executable tests. Production participants must persist idempotency and publication state in the participant-owned UCKK implementation.
