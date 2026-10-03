# ADR-IK-02 — Kristal portable-contract pin

**Status:** Accepted (v6 portable contract retained)

Pin the active portable Kristal contract at Standard `6.0.0` using `kristal.consumer-lock/v2`. The lock records canonicalization `kristal.v6:jcs-rfc8785`, the standard-manifest SHA-256 and the core `kristal-state` / Reader Policy schema digests.

Kristal v7 is additive above this portable contract, so the v6 pin is not superseded by v7. The current v7 design baseline is pinned separately and its architectural boundary is defined by [ADR-IK-07](ADR-IK-07-daat-kristal-v7-boundary.md).

The previous Git-tag/commit-based v5 RC pin is retired because the v6 portable snapshot is identified directly by its published manifest and contract digests.
