from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from .errors import IKError

@dataclass(frozen=True)
class RegisteredProfile:
    descriptor: dict[str, Any]
    payload_schema: dict[str, Any]
    root: Path

class ProfileRegistry:
    def __init__(self) -> None:
        self._profiles: dict[tuple[str, str], RegisteredProfile] = {}

    def register_directory(self, path: str | Path) -> RegisteredProfile:
        root = Path(path)
        descriptor = json.loads((root / "profile.json").read_text(encoding="utf-8"))
        payload_schema = json.loads((root / descriptor["payload_schema"]).read_text(encoding="utf-8"))
        key = (descriptor["id"], descriptor["version"])
        if key in self._profiles:
            raise IKError("IK_PROFILE_CONFLICT", f"profile already registered: {key}")
        registered = RegisteredProfile(descriptor, payload_schema, root)
        self._profiles[key] = registered
        return registered

    def get(self, profile_id: str, version: str) -> RegisteredProfile:
        try:
            return self._profiles[(profile_id, version)]
        except KeyError as exc:
            raise IKError("IK_UNKNOWN_PROFILE", f"unknown profile {profile_id}@{version}") from exc

    @classmethod
    def from_contracts(cls, contracts_root: str | Path) -> "ProfileRegistry":
        registry = cls()
        contracts = Path(contracts_root)
        index_path = contracts / "profiles" / "index.json"
        index = json.loads(index_path.read_text(encoding="utf-8"))
        if index.get("format") != "ik.profile-index/1" or not isinstance(index.get("profiles"), list):
            raise IKError("IK_PROFILE_CONFLICT", "invalid active profile index")

        # The index is authoritative. Versioned directories not listed here are
        # retained as historical contracts but MUST NOT be automatically admitted.
        candidates: dict[tuple[str, str], Path] = {}
        for p in sorted((contracts / "profiles").glob("*/*/*/profile.json")):
            descriptor = json.loads(p.read_text(encoding="utf-8"))
            key = (descriptor["id"], descriptor["version"])
            if key in candidates:
                raise IKError("IK_PROFILE_CONFLICT", f"duplicate profile directory: {key}")
            candidates[key] = p.parent

        seen: set[tuple[str, str]] = set()
        for entry in index["profiles"]:
            if not isinstance(entry, dict) or not all(isinstance(entry.get(k), str) for k in ("id", "version", "class")):
                raise IKError("IK_PROFILE_CONFLICT", "invalid indexed profile entry")
            key = (entry["id"], entry["version"])
            if key in seen:
                raise IKError("IK_PROFILE_CONFLICT", f"duplicate active profile: {key}")
            seen.add(key)
            root = candidates.get(key)
            if root is None:
                raise IKError("IK_UNKNOWN_PROFILE", f"indexed profile missing from contracts: {key}")
            registered = registry.register_directory(root)
            if registered.descriptor["class"] != entry["class"]:
                raise IKError("IK_PROFILE_CONFLICT", f"class mismatch in active profile index: {key}")
        return registry
