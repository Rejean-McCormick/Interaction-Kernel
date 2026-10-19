"""Read-only adopted Konnaxion/Orgo profile integrity and active-index check."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "contracts/locks/konnaxion-orgo-adopted-v1.lock.json"
INDEX_PATH = ROOT / "contracts/profiles/index.json"
REQUIRED = {
    ("governance.decision.execute", "1.0.0", "command"),
    ("accountability.impact.publish", "1.0.0", "command"),
    ("operational.reconsideration.recommended", "1.0.0", "event"),
}


def verify(root: Path = ROOT) -> None:
    root = root.resolve()
    lock = json.loads((root / LOCK_PATH.relative_to(ROOT)).read_text(encoding="utf-8"))
    if lock.get("format") != "ik.adopted-profile-lock/1" or lock.get("scope") != "konnaxion-orgo" or lock.get("specversion") != "ik/1.1":
        raise ValueError("invalid Konnaxion-Orgo adopted contract lock metadata")
    index = json.loads((root / INDEX_PATH.relative_to(ROOT)).read_text(encoding="utf-8"))
    if index.get("format") != "ik.profile-index/1":
        raise ValueError("invalid IK active profile index format")
    actual = [(e["id"], e["version"], e["class"]) for e in index.get("profiles", [])]
    if len(actual) != len(set(actual)) or not REQUIRED.issubset(set(actual)):
        raise ValueError("missing or duplicate adopted active profile")
    expected_paths = {
        f"contracts/profiles/konnaxion-orgo/{name}/{version}/{filename}"
        for name, version, _ in REQUIRED for filename in ("profile.json", "payload.schema.json")
    }
    files = lock.get("files")
    if not isinstance(files, list) or {e.get("path") for e in files} != expected_paths or len(files) != len(expected_paths):
        raise ValueError("adopted contract lock has missing, extra or duplicate paths")
    for entry in files:
        relative = Path(entry["path"])
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f"adopted contract file missing or outside root: {relative}")
        sha = "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
        if entry.get("sha256") != sha:
            raise ValueError(f"adopted contract digest mismatch: {relative}")
        if relative.name == "profile.json":
            desc = json.loads(path.read_text(encoding="utf-8"))
            parts = relative.parts
            if (desc.get("id"), desc.get("version"), desc.get("class")) not in REQUIRED or desc.get("id") != parts[3] or desc.get("version") != parts[4]:
                raise ValueError(f"adopted descriptor metadata mismatch: {relative}")
    print("Konnaxion-Orgo adopted contract lock: PASS (three profiles, six immutable file digests)")


if __name__ == "__main__":
    try:
        verify()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"Konnaxion-Orgo adopted contract lock: FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
