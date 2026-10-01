# Kristal v6 and Da’at

Baseline: Da’at is the IK participant in front of Kristal. Kristal does not parse IK Envelopes.

Pinned standard:

- standard version `6.0.0`;
- canonicalization `kristal.v6:jcs-rfc8785`;
- canonicalization version `1`;
- pin identity: standard-manifest digest plus the `kristal-state` and Reader Policy schema digests in `locks/kristal-v6.0.0.lock.json`.

Da’at applies explicit versioned mappings from Konnaxion/Orgo ExportManifests to Kristal-native inputs, invokes Kristal-native contracts, validates outputs, then emits IK Receipts/Events with Kristal-owned ArtifactRefs. `kristal.build.request/2.0.0` explicitly requires contract set `6.0.0`.

## v6 semantic boundary

Kristal v6 generalizes the former Structured Epistemic State into `kristal_state`. Assertions may carry typed `valuations[]`, `coordinates`, `applicability`, `record_role`, and `actionability`. These fields describe knowledge, state, constraints and actionability; they do **not** transfer operational authority to Kristal or Da’at.

An `actionability.mode` of `automatic` means the represented action is eligible for automation under its declared policy. Actual execution still requires the receiving system's authority, IK Profile, admission and owner-local mutation rules.

## Authority boundary

Konnaxion and Orgo do not write their mutable operational databases into Kristal and do not grant Da’at ownership of that state. They provide source-owned snapshots/revisions suitable for mapping.

```text
source operational DB
       |
       | source-owned snapshot / ExportManifest
       v
      Da'at
       |
       | versioned mapping
       v
Kristal v6 state / derived artifact
       |
       | ArtifactRef
       v
source/local consumer projection or authorized action request
```

Kristal owns its native knowledge artifacts. A Runtime Pack or database-like query materialization derived from a Kristal artifact remains a materialization; it does not become the source application's operational system of record.

IK does not require a distributed transaction between the source database, Da’at and Kristal. Cross-boundary completion is expressed through durable delivery, Receipts, Events, ArtifactRefs and reconciliation.

See [ADR-IK-05](adrs/ADR-IK-05-operational-state-artifact-boundary.md).
