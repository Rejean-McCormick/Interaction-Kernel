from __future__ import annotations
from dataclasses import dataclass
import hashlib, json
from pathlib import Path

EXPECTED_VERSION = "6.0.0"
EXPECTED_PROFILE = "kristal.v6:jcs-rfc8785"
EXPECTED_MANIFEST = "sha256:1cc531c918d8c97c0caca8ced7560e54f9c8a98c5527fc90e32cb569dbdbb9b9"
EXPECTED_STATE_SCHEMA = "sha256:47e5cd7fd3a801adfd230a7591a70a62ff89a39d42023d87fe99851bc32725c5"
EXPECTED_READER_SCHEMA = "sha256:e5b8f8741a1736e8a7ce1204cf0ce1e0345b1a7e4b2fa19b19980b9b66e34599"

@dataclass(frozen=True)
class KristalLock:
    version: str
    canonicalization_profile: str
    standard_manifest_sha256: str
    contract_digests: dict[str, str]

def load_and_verify(path: str | Path) -> KristalLock:
    value=json.loads(Path(path).read_text(encoding="utf-8"))
    if value.get("format") != "kristal.consumer-lock/v2": raise ValueError("unexpected Kristal lock format")
    if value.get("version") != EXPECTED_VERSION: raise ValueError("unexpected Kristal standard version")
    if value.get("canonicalization_profile") != EXPECTED_PROFILE: raise ValueError("Kristal canonicalization profile mismatch")
    if value.get("standard_manifest_sha256") != EXPECTED_MANIFEST: raise ValueError("Kristal standard manifest mismatch")
    digests=value.get("contract_digests", {})
    if digests.get("schemas/kristal-state.schema.json") != EXPECTED_STATE_SCHEMA: raise ValueError("Kristal State schema mismatch")
    if digests.get("schemas/reader-policy.schema.json") != EXPECTED_READER_SCHEMA: raise ValueError("Reader Policy schema mismatch")
    return KristalLock(value["version"], value["canonicalization_profile"], value["standard_manifest_sha256"], dict(digests))
