# Validation report

Validated on 2026-10-03 for Interaction Kernel `2.0.0-dev.2` after the DaaT boundary cleanup and Kristal/Kristall v7 alignment.

## Passing gates

- repository JSON Schemas/Profile schemas: **PASS**;
- Kristal v6 portable consumer lock v2 + manifest/core-schema digests: **PASS**;
- Kristal/Kristall `7.0.0-draft.3.1` design-baseline content-digest lock: **PASS**;
- Kristal v6 / RFC 8785 JCS vectors: **9/9 PASS** in Python and TypeScript;
- IK semantic fingerprint vectors: **3/3 PASS** in Python and TypeScript;
- Python admission/fingerprint/JCS/validation/UCKK adapter suite: **13 tests PASS**;
- UCKK publication adapter: publish, replay, divergent replay rejection, ArtifactRef integrity requirement and revocation: **PASS**;
- TypeScript admission/idempotency suite: **PASS**;
- TypeScript Orgo reference adapter static typecheck: **PASS**;
- Markdown relative links: **PASS**.

## Optional external gate

The Konnaxion legacy bridge compatibility test requires an external Konnaxion source tree at `/mnt/data/ik_build/src/konnaxion/...`. The standalone SmartSnap does not contain that tree, so `scripts/test_all.*` reports an explicit **SKIP** when it is absent instead of failing the self-contained repository validation.

## Kristal compatibility pins

### Portable v6

- standard `6.0.0`;
- canonicalization `kristal.v6:jcs-rfc8785`;
- standard manifest `sha256:1cc531c918d8c97c0caca8ced7560e54f9c8a98c5527fc90e32cb569dbdbb9b9`;
- Kristal State schema `sha256:47e5cd7fd3a801adfd230a7591a70a62ff89a39d42023d87fe99851bc32725c5`;
- Reader Policy schema `sha256:e5b8f8741a1736e8a7ce1204cf0ce1e0345b1a7e4b2fa19b19980b9b66e34599`.

### Additive v7 design baseline

- Kristal/Kristall `7.0.0-draft.3.1`;
- portable contract remains `artifact_type = kristal_state`, `schema_version = 6.0`;
- baseline lock format `interaction-kernel.kristal-baseline-lock/v1`;
- release-contract digest `sha256:ab34bc000a15b6b87c811b77831a120f0ed5bc1d8a7bf948daa18fa6c6b48b09`;
- v7 core-spec digest `sha256:36f3ea743cc9a44d88981198714bc29a028898eacf4b83431d37f8c44e92b9ed`.

## DaaT authority invariant

DaaT (`daat`) is the IK↔Kristal anti-corruption/admission and explicit contract-mapping boundary. It is not the authority for source acquisition, artifact storage, general corpus normalization, or Kristall KQ/KP/KA/KS identity.

Kristal v6 `record_role` and `actionability` enrich artifact semantics only. `actionability.mode = automatic` does not authorize a cross-system mutation; execution remains subject to the receiving owner's explicit contract/Profile, identity/authority check, admission policy and owner-local state transition.

UCKK publication likewise creates only a participant-local projection. The canonical Kristal/Kristall knowledge and publication bundle remain owned upstream; a successful UCKK Receipt proves the UCKK-local operation, not a transfer of authority.
