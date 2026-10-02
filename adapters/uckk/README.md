# UCKK Kristal publication adapter

This adapter is the UCKK-specific edge of the Kristal publication flow. It belongs in Interaction Kernel because it maps an IK interaction to a participant-specific publication operation; it does **not** move artifact ownership into IK.

## Ownership boundary

- Kristal defines the canonical knowledge artifact and release semantics.
- The kOA Mediatheque may own the immutable publication bundle bytes and expose them through an opaque `ArtifactRef` locator.
- Da'at is the IK participant that admits/orchestrates the Kristal boundary and emits `kristal.publication.request`.
- UCKK owns its local publication object and returns an IK Receipt / publication event.
- IK transports the command, artifact reference and receipts. IK is never the artifact store or canonical Kristal authority.

## Profiles

- `kristal.publication.request/1.0.0`
- `kristal.publication.available/1.0.0`
- `kristal.publication.revoke.request/1.0.0`
- `kristal.publication.revoked/1.0.0`

A publication request must carry exactly one `kristal.publication_bundle` ArtifactRef with SHA-256 integrity and an opaque locator. `supersedes_publication_id` handles replacement without deleting history. Revocation preserves provenance and may point at a replacement publication.

`UckkKristalPublicationAdapter` is intentionally port-based. A production UCKK integration implements `UckkKristalPublicationPort` and persists its own publication/idempotency state. The reference adapter keeps only an in-memory replay ledger for executable semantics and tests.
