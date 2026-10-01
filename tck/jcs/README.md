# JCS Test Vectors — Kristal v6

This directory is the Interaction Kernel cross-language golden suite for RFC 8785 canonicalization where IK must interoperate with Kristal v6 content-addressed artifacts.

The canonicalization profile is `kristal.v6:jcs-rfc8785`, version `1`. JCS behavior itself is RFC 8785; the Kristal-specific vectors exercise the v6 canonical surfaces that matter to downstream interoperability.

## Included fixtures

- empty and nested objects;
- Unicode/escaping and RFC 8785 numeric serialization;
- hash-reference shape;
- a `kristal_state` hash target excluding `state_id`, `content_hash`, and `signatures`;
- typed `valuations[]`, `record_role`, and `actionability`;
- array-order preservation and UTF-16 property ordering.

`unknown`, `not_applicable`, `indeterminate`, and `not_measured` are value states in Kristal v6, not numeric values. The vector suite therefore never coerces them to zero.

Python and TypeScript runtimes MUST produce the exact `expected_canonical` bytes for every vector.
