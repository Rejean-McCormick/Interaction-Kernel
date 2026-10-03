from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "locks/kristal-v7.0.0-draft.3.1.lock.json"
UPSTREAM = ROOT / "locks/kristal-v7.0.0-draft.3.1-upstream"


def digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
assert lock["format"] == "interaction-kernel.kristal-baseline-lock/v1"
assert lock["version"] == "7.0.0-draft.3.1"
assert lock["portable_contract"] == {
    "artifact_type": "kristal_state",
    "schema_version": "6.0",
    "canonicalization_profile": "kristal.v6:jcs-rfc8785",
}
assert (UPSTREAM / "VERSION").read_text(encoding="utf-8").strip() == lock["version"]

for relative_path, expected in lock["contract_digests"].items():
    actual = digest(UPSTREAM / relative_path)
    assert actual == expected, f"Kristal v7 baseline digest mismatch: {relative_path}"

release = json.loads((UPSTREAM / "contracts/release.json").read_text(encoding="utf-8"))
assert release["version"] == lock["version"]
assert release["portable_contract"]["artifact_type"] == "kristal_state"
assert release["portable_contract"]["schema_version"] == "6.0"
assert release["portable_contract"]["schema"] == "schemas/v6/kristal-state.schema.json"

print("Kristal/Kristall v7 design baseline lock: PASS")
