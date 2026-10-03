# DaaT reference adapter

DaaT is the Interaction Kernel anti-corruption boundary in front of Kristal/Kristall. Its machine system identifier is `daat`.

DaaT authenticates and admits IK interactions, verifies pinned Kristal compatibility, applies an explicit versioned **contract mapping**, invokes Kristal-native interfaces, validates returned artifacts, then emits IK Receipts/Events carrying owner-preserving `ArtifactRef`s.

DaaT is deliberately narrow. It does **not** crawl or acquire sources, store source bytes, deduplicate corpora, perform general content normalization, own source applications' operational state, or become a semantic authority. In particular, DaaT does not mint Kristall KQ/KP/KA/KS identities or author Kristall registries on behalf of Kristal. Those semantics remain Kristal/Kristall-owned.

The active IK build surface remains the portable Kristal v6 contract (`kristal_state/6.0`). Kristal v7 is additive above that portable contract: v6 artifacts remain unchanged inputs/projections while Kristall owns v7 meta-orchestration.

Cross-boundary completion is asynchronous and reference-based.
