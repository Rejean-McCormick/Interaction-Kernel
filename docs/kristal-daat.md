# Kristal/Kristall and DaaT

DaaT is the Interaction Kernel anti-corruption/admission boundary in front of Kristal/Kristall. Kristal does not parse IK Envelopes, and IK does not absorb Kristal/Kristall semantics into its transport model.

The stable machine identifier is `daat`; the human-facing name is **DaaT**.

## Compatibility baseline

IK intentionally carries two compatible pins:

- **portable contract:** Kristal Standard `6.0.0`, canonicalization `kristal.v6:jcs-rfc8785`;
- **current design baseline:** Kristal `7.0.0-draft.3.1`, where Kristall is additive above the unchanged portable `kristal_state/6.0` contract.

The exact portable v6 dependency bytes remain pinned only in `locks/kristal-v6.0.0.lock.json`. The v7 design baseline is pinned separately in `locks/kristal-v7.0.0-draft.3.1.lock.json` using v7 release/spec/meta-schema digests; it does not replace the exact v6 dependency lock.

`kristal.build.request/2.0.0` still requires portable contract set `6.0.0`. This is deliberate: v7 does not invalidate or replace v6 portable states. A future IK Profile that directly addresses Kristall v7 meta-artifacts must be introduced as a new explicit contract rather than silently changing this Profile.

## DaaT boundary

DaaT may:

- authenticate/admit an IK interaction;
- verify the pinned Kristal compatibility baseline;
- apply an explicit versioned contract mapping from an admitted `ExportManifest`/`ArtifactRef` to Kristal-native input;
- invoke the Kristal-native interface;
- validate returned artifacts and emit IK Receipts/Events preserving artifact ownership.

DaaT does **not**:

- discover, crawl or acquire external sources;
- store source bytes or become a media/source repository;
- perform general corpus cleaning, deduplication or normalization;
- own source applications' mutable operational state;
- mint or reinterpret Kristall KQ/KP/KA/KS identities;
- author Kristall Mesh, axes, source registries or crystallization semantics on behalf of Kristal.

Those semantic authorities remain inside Kristal/Kristall. Upstream acquisition/normalization remains outside DaaT.

## Portable v6 semantic boundary

Kristal v6 `kristal_state` remains the portable unit. Assertions may carry typed `valuations[]`, `coordinates`, `applicability`, `record_role`, and `actionability`. These fields describe knowledge, state, constraints and actionability; they do **not** transfer operational authority to Kristal or DaaT.

An `actionability.mode` of `automatic` means the represented action is eligible for automation under its declared policy. Actual execution still requires the receiving system's authority, IK Profile, admission and owner-local mutation rules.

Kristall v7 may ingest valid v6 Kristals, preserve their source identity, align them in its semantic space, and materialize new v6-compatible projections with v7 lineage. DaaT transports/maps across the IK boundary; it is not the authority that performs semantic identity resolution or crystallization.

## Authority flow

```text
source-owned operational state / prepared export
              |
              | ExportManifest / ArtifactRef
              v
             IK
              |
              v
            DaaT
              | explicit contract mapping
              v
      Kristal portable v6 interface
              |
              v
       Kristal / Kristall v7
              |
              | owner-preserving ArtifactRef
              v
     authorized local consumer
```

IK does not require a distributed transaction between a source database, DaaT and Kristal. Cross-boundary completion is expressed through durable delivery, Receipts, Events, ArtifactRefs and reconciliation.

See [ADR-IK-05](adrs/ADR-IK-05-operational-state-artifact-boundary.md) and [ADR-IK-07](adrs/ADR-IK-07-daat-kristal-v7-boundary.md).

## UCKK publication boundary

DaaT is also the IK-side boundary participant for publishing a Kristal release to UCKK. It does not need to own the publication bundle: `ArtifactRef.owner` may remain `mediatheque-koa` (or another authoritative artifact owner), while DaaT supplies the admitted interaction, authority context and pinned compatibility semantics.

The UCKK-specific mapping is implemented under `adapters/uckk/`. Publication, supersession and revocation change only the UCKK projection lifecycle.
