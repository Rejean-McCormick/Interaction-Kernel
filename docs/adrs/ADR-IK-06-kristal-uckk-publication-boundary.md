# ADR-IK-06 — Kristal → UCKK publication boundary

**Status:** Accepted  
**Date:** 2026-10-02

## Decision

UCKK publication is an Interaction Kernel participant integration, implemented as a UCKK adapter and versioned IK Profiles. It is not a Kristal Framework transport concern and not an IK artifact store.

The canonical Kristal and its source/corpus bytes remain owned by their authoritative systems. In the reference deployment, the kOA Mediatheque may own immutable publication bundle bytes. Da'at emits an IK command carrying an `ArtifactRef` to that bundle. UCKK resolves/imports the referenced immutable artifact, creates its own local publication object, and returns a Receipt and/or outcome Event.

## Profiles

- `kristal.publication.request/1.0.0`
- `kristal.publication.available/1.0.0`
- `kristal.publication.revoke.request/1.0.0`
- `kristal.publication.revoked/1.0.0`

Publication replacement uses `supersedes_publication_id`. Revocation is explicit and preserves historical provenance. Neither operation mutates the canonical Kristal corpus.

## Consequences

1. UCKK-specific mapping lives under `adapters/uckk/`.
2. Kristal Framework remains independent of UCKK implementation details.
3. IK carries references, authority context and lifecycle acknowledgements; it does not persist publication payloads.
4. The kOA Mediatheque can remain the artifact owner while Da'at remains the IK boundary participant.
5. Production UCKK implementations must persist idempotency and publication state locally; the reference adapter only demonstrates the semantics.
