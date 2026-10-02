from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

from _paths import CONTRACTS
from interaction_kernel.errors import IKError
from interaction_kernel.validator import ContractValidator

ADAPTER_PATH = Path(__file__).resolve().parents[3] / "adapters" / "uckk" / "kristal_publication_adapter.py"
spec = importlib.util.spec_from_file_location("uckk_kristal_publication_adapter", ADAPTER_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = module
spec.loader.exec_module(module)
PublicationResult = module.PublicationResult
RevocationResult = module.RevocationResult
UckkKristalPublicationAdapter = module.UckkKristalPublicationAdapter


class FakePort:
    def __init__(self) -> None:
        self.publish_calls = []
        self.revoke_calls = []

    def publish(self, **kwargs):
        self.publish_calls.append(kwargs)
        return PublicationResult(uckk_object_id="uckk:pub:42", external_reference="uckk://publication/42")

    def revoke(self, **kwargs):
        self.revoke_calls.append(kwargs)
        return RevocationResult(uckk_object_id="uckk:pub:42")


def publication_envelope(*, key="pub-key-1", publication_id="pub-1", digest="a" * 64):
    return {
        "specversion": "ik/1.1",
        "id": "interaction-publication-0001",
        "class": "command",
        "time": "2026-10-02T12:00:00Z",
        "profile": {"id": "kristal.publication.request", "version": "1.0.0"},
        "source": {"system": "daat"},
        "target": {"system": "uckk"},
        "subject": {"type": "kristal", "id": "history-tech"},
        "idempotency_key": key,
        "authority": {"kind": "knowledge-publication", "claims": ["publish:kristal"]},
        "data": {
            "publication_id": publication_id,
            "kristal_id": "history-tech",
            "kristal_version": "2.4.0",
            "channel": "reference",
            "metadata": {"title": "History Tech"}
        },
        "artifact_refs": [{
            "owner": {"system": "mediatheque-koa"},
            "artifact_type": "kristal.publication_bundle",
            "artifact_id": "koa:publication:pub-1",
            "version": "2.4.0",
            "integrity": {"algorithm": "sha256", "digest": digest},
            "locator": {"ref": "koa-media://publication/pub-1"},
            "content": {"media_type": "application/zip", "contract_ref": "kristal-publication/1"}
        }]
    }


def revocation_envelope(*, key="revoke-key-1"):
    return {
        "specversion": "ik/1.1",
        "id": "interaction-revocation-0001",
        "class": "command",
        "time": "2026-10-02T12:10:00Z",
        "profile": {"id": "kristal.publication.revoke.request", "version": "1.0.0"},
        "source": {"system": "daat"},
        "target": {"system": "uckk"},
        "subject": {"type": "kristal-publication", "id": "pub-1"},
        "idempotency_key": key,
        "authority": {"kind": "knowledge-publication", "claims": ["revoke:kristal"]},
        "data": {"publication_id": "pub-1", "reason": "superseded", "replacement_publication_id": "pub-2"}
    }


class UckkAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = ContractValidator(CONTRACTS)

    def test_publication_profile_and_adapter(self):
        env = publication_envelope()
        self.validator.validate_envelope(env)
        port = FakePort()
        adapter = UckkKristalPublicationAdapter(port)
        receipt = adapter.handle(env)
        self.validator.validate_receipt(receipt)
        self.assertEqual(receipt["status"], "succeeded")
        self.assertEqual(receipt["data"]["uckk_object_id"], "uckk:pub:42")
        self.assertEqual(len(port.publish_calls), 1)
        self.assertEqual(port.publish_calls[0]["artifact_ref"]["owner"]["system"], "mediatheque-koa")

    def test_publication_replay_is_idempotent(self):
        env = publication_envelope()
        port = FakePort()
        adapter = UckkKristalPublicationAdapter(port)
        first = adapter.handle(env)
        second = adapter.handle(env)
        self.assertEqual(first, second)
        self.assertEqual(len(port.publish_calls), 1)

    def test_idempotency_conflict_is_rejected(self):
        port = FakePort()
        adapter = UckkKristalPublicationAdapter(port)
        adapter.handle(publication_envelope(key="same-key", publication_id="pub-1"))
        with self.assertRaises(IKError) as ctx:
            adapter.handle(publication_envelope(key="same-key", publication_id="pub-2"))
        self.assertEqual(ctx.exception.code, "IK_IDEMPOTENCY_CONFLICT")

    def test_requires_integrity_and_locator(self):
        env = publication_envelope()
        env["artifact_refs"][0].pop("integrity")
        port = FakePort()
        adapter = UckkKristalPublicationAdapter(port)
        with self.assertRaises(IKError):
            adapter.handle(env)

    def test_revocation_profile_and_adapter(self):
        env = revocation_envelope()
        self.validator.validate_envelope(env)
        port = FakePort()
        adapter = UckkKristalPublicationAdapter(port)
        receipt = adapter.handle(env)
        self.validator.validate_receipt(receipt)
        self.assertEqual(receipt["data"]["state"], "revoked")
        self.assertEqual(len(port.revoke_calls), 1)
        self.assertEqual(port.revoke_calls[0]["replacement_publication_id"], "pub-2")


if __name__ == "__main__":
    unittest.main()
