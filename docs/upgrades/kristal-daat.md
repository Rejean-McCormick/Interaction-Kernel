# Kristal / Da’at v6 upgrade

Da’at now targets the final Kristal Standard `6.0.0`. Do not add IK transport fields to Kristal core schemas.

Required mapping changes:

- `structured_epistemic_state` → `kristal_state`;
- `certainty_level` + `uncertainty` → typed `valuations[]`;
- `qualifiers` → `coordinates`;
- `scope` → `applicability`;
- preserve `record_role` and `actionability` when source mappings can support them;
- never infer `automatic` merely from a high valuation; actionability requires policy semantics distinct from measurement.

Da’at remains responsible for pin verification, versioned mapping profiles, native Kristal invocation, output validation and IK artifact handoff. Source applications keep mutable operational records in their own databases. Kristal actionability can inform routing, but execution occurs only through an authorized owner boundary.
