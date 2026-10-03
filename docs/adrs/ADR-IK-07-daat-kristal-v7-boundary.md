# ADR-IK-07 — DaaT boundary and Kristal v7 compatibility

**Status:** Accepted  
**Date:** 2026-10-03

## Decision

The human-facing participant name is **DaaT** and its machine identifier is **`daat`**. Previous human-facing variants are retired.

DaaT is the Interaction Kernel anti-corruption/admission boundary for Kristal/Kristall. It may perform only explicit, versioned contract mapping needed to translate an admitted IK interaction into Kristal-native input and to translate returned artifact references into IK Receipts/Events.

DaaT is not a source-acquisition system, artifact store, corpus normalizer, semantic identity authority, or independent knowledge compiler. It MUST NOT mint or reinterpret Kristall KQ/KP/KA/KS identities and MUST NOT treat external identifiers as Kristall semantic identity.

Kristal `7.0.0-draft.3.1` is the current design baseline. The v7 architecture is additive above the unchanged portable `kristal_state/6.0` contract. Therefore:

- existing IK `kristal.build.request/2.0.0` and `kristal.artifact.ready/2.0.0` remain v6 portable-artifact surfaces;
- the existing `kristal.consumer-lock/v2` continues to pin the exact portable v6 dependency used by those surfaces;
- IK additionally pins the Kristal v7 design baseline in `locks/kristal-v7.0.0-draft.3.1.lock.json`;
- a future IK Profile that directly addresses Kristall v7 meta-artifacts requires its own explicit versioned contract rather than silently changing the v6 build profile.

## Consequences

1. Existing `daat` wire identifiers, directories and route checks remain stable.
2. Human documentation and descriptions use `DaaT`.
3. Upstream acquisition/normalization remains outside DaaT.
4. v7 semantic identity, Mesh, axes, source registries and crystallization remain Kristal/Kristall-owned.
5. v6 portable compatibility is preserved while IK can verify which v7 design baseline it was aligned against.
