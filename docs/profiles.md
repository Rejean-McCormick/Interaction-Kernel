# Profiles

Profiles carry use-case semantics. They pin payload schemas and define class, allowed participants, authority requirements, artifact requirements, reliability requirements and response expectations.

Implemented Profiles:

- `governance.decision.execute/1.0.0`
- `accountability.impact.publish/1.0.0`
- `operational.reconsideration.recommended/1.0.0`
- `kristal.build.request/2.0.0` — Kristal Standard 6.0.0 build request
- `kristal.artifact.ready/2.0.0` — Kristal v6 artifact event
- `kristal.revision.request/2.0.0`
- `knowledge.distribution.request/1.0.0`

The active profile registry selects the Kristal `2.0.0` build/artifact/revision surfaces. Kristal profile directories at `1.0.0` are retained only as legacy compatibility/history and must not be used to claim conformance with the active Kristal Standard `6.0.0` boundary.

See [`contracts/profiles/`](../contracts/profiles/).
