# ADR-IK-02 — Kristal Standard pin

**Status:** Accepted (v6 replacement)

Pin Kristal Standard `6.0.0` using `kristal.consumer-lock/v2`. The lock records canonicalization `kristal.v6:jcs-rfc8785`, the standard-manifest SHA-256 and the core `kristal-state` / Reader Policy schema digests.

The previous Git-tag/commit-based v5 RC pin is retired because the v6 standard snapshot is identified directly by its published manifest and contract digests.
