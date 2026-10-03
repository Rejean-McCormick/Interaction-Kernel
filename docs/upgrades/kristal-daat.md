# Kristal/Kristall + DaaT alignment

DaaT uses **DaaT** as the human-facing name and `daat` as the stable machine identifier.

The active portable IK build surface remains Kristal Standard `6.0.0`; Kristal `7.0.0-draft.3.1` is pinned as the additive Kristall design baseline. Do not add IK transport fields to Kristal core schemas and do not reinterpret v7 as a replacement wire format for v6 portable states.

Required v6 mapping rules remain:

- `structured_epistemic_state` → `kristal_state`;
- `certainty_level` + `uncertainty` → typed `valuations[]`;
- `qualifiers` → `coordinates`;
- `scope` → `applicability`;
- preserve `record_role` and `actionability` when source mappings can support them;
- never infer `automatic` merely from a high valuation; actionability requires policy semantics distinct from measurement.

For v7 alignment:

- preserve valid v6 source artifact identity;
- treat v7 as Kristall-owned meta-orchestration above v6;
- keep external IDs as mappings, never as KQ/KP/KA/KS identity;
- do not make DaaT responsible for Mesh, axes, source registries, semantic entity resolution or crystallization;
- add a new versioned IK Profile before transporting any new v7 meta-artifact family directly.

DaaT remains responsible only for pin verification, explicit versioned contract mapping, native Kristal invocation, output validation and IK artifact handoff. Source applications keep mutable operational records in their own databases.
