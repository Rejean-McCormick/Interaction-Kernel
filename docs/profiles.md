# Profiles

Profiles carry use-case semantics. They pin payload schemas and define class, allowed participants, authority requirements, artifact requirements, reliability requirements and response expectations.

Implemented Profiles:

- `governance.decision.execute/1.0.0`
- `accountability.impact.publish/1.0.0`
- `operational.reconsideration.recommended/1.0.0`
- `kristal.build.request/2.0.0` — DaaT-mediated portable Kristal `6.0.0` build request
- `kristal.artifact.ready/2.0.0` — Kristal v6 artifact event
- `kristal.revision.request/2.0.0`
- `knowledge.distribution.request/1.0.0`
- `kristal.publication.request/1.0.0` — publish an immutable Kristal publication bundle to UCKK
- `kristal.publication.available/1.0.0` — UCKK publication outcome event
- `kristal.publication.revoke.request/1.0.0` — revoke a UCKK projection without deleting Kristal provenance
- `kristal.publication.revoked/1.0.0` — UCKK revocation outcome event

The active profile registry selects the Kristal `2.0.0` build/artifact/revision surfaces. These remain portable v6 surfaces even though IK is aligned to the additive Kristal/Kristall `7.0.0-draft.3.1` design baseline. New direct v7 meta-artifact transport requires a new explicit Profile. The older `1.0.0` build/artifact/revision directories are retained only as legacy compatibility/history. The Kristal→UCKK publication profiles are a separate active `1.0.0` family.

See [`contracts/profiles/`](../contracts/profiles/).
