# Architecture

IK is a distributed protocol, not a central server, database, artifact store or distributed transaction coordinator.

```text
Konnaxion  <---------- IK ----------> Orgo
    \                                /
     +----------- IK ----------> DaaT ---------- IK ----------> UCKK
                                   |
                    portable v6 / pinned v7 baseline
                                   |
                          Kristal / Kristall
```

## Ownership

| Plane | Owner | Examples |
|---|---|---|
| civic/governance | Konnaxion | deliberation, DecisionRecord, impact/accountability |
| operational/work | Orgo | Signal, Workflow, Case, Task, IntegrationOperation |
| knowledge/state | Kristal/Kristall | portable Kristal states plus v7 semantic identity, Mesh, axes, registries and crystallization |
| Kristal boundary | DaaT | IK admission, explicit contract mapping, compatibility-pin verification, handoff; no acquisition/storage/semantic identity authority |
| host activation | kOA-Linux when present | verify/stage/activate/rollback Runtime Pack |
| Kristal publication projection | UCKK | UCKK-local published representation and lifecycle |
| publication artifact bytes | source artifact owner (for example kOA Mediatheque) | immutable Kristal publication bundle |

## State and artifact flow

The normal cross-boundary flow is one-way with respect to authoritative ownership:

```text
participant-owned operational state
              |
              | committed local state
              v
    source-owned snapshot/export
              |
              | ExportManifest / ArtifactRef
              v
             IK
              |
              v
            DaaT
              |
              | explicit contract mapping
              v
   Kristal/Kristall-owned artifact
              |
              | ArtifactRef / Event
              v
   participant-local projection
```

A local projection, cache, index or Runtime Pack activation does not acquire ownership of the source system's operational state.

## Transaction boundary

IK does not require or define a transaction spanning participant databases. A participant commits its own state locally, then uses durable emission, idempotent processing and reconciliation for cross-owner effects. An Event announces a fact already committed by its publisher.

Invariants: unique authoritative owner, no cross-system DB writes, no distributed cross-owner commit requirement, Konnaxion↔Orgo direct by default, Kristal optional by Profile, delivery lifecycle separate from domain lifecycle, artifact reference separate from artifact ownership.

See [ADR-IK-05](adrs/ADR-IK-05-operational-state-artifact-boundary.md) and [ADR-IK-07](adrs/ADR-IK-07-daat-kristal-v7-boundary.md).

## Kristal publication to UCKK

UCKK is an optional IK participant, not part of the Kristal canonical authority plane. The normal publication path is:

```text
kOA Mediatheque (artifact owner)
        |
        | immutable kristal.publication_bundle ArtifactRef
        v
      DaaT
        |
        | kristal.publication.request
        v
       IK
        |
        v
  UCKK adapter / UCKK
        |
        | Receipt + kristal.publication.available
        v
      DaaT
```

Supersession creates a new UCKK publication linked to the earlier publication. Revocation changes the UCKK-local publication lifecycle but does not delete or mutate the canonical Kristal corpus. See [ADR-IK-06](adrs/ADR-IK-06-kristal-uckk-publication-boundary.md).
