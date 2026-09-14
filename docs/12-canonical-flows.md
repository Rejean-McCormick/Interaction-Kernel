# Canonical flows

## 1. Direct Konnaxion → Orgo

```mermaid
sequenceDiagram
  participant K as Konnaxion
  participant O as Orgo
  K->>O: Command governance.decision.execute
  O-->>K: Receipt accepted/rejected/blocked
  O->>O: Signal → WorkflowVersion → Case/Tasks
  O-->>K: final Receipt and/or outcome Event
```

Le sender ne crée jamais directement Case/Task.

## 2. Orgo → Konnaxion impact publication

```mermaid
sequenceDiagram
  participant O as Orgo
  participant K as Konnaxion
  O->>O: IntegrationOperation + Outbox
  O->>K: Command accountability.impact.publish
  K->>K: provider-owned validation + exactly-one effect
  K-->>O: Receipt succeeded / conflict / rejected
```

## 3. Knowledge enrichment

```mermaid
sequenceDiagram
  participant S as Konnaxion/Orgo
  participant D as Da'at
  participant K as Kristal
  S->>D: kristal.build.request + ExportManifest/ArtifactRefs
  D->>K: mapped Kristal-native input
  K-->>D: Exchange / RuntimePack / reports
  D-->>S: kristal.artifact.ready + ArtifactRefs
```

## 4. Runtime Pack distribution

```mermaid
sequenceDiagram
  participant D as Da'at
  participant O as Orgo/Governance
  participant T as Distribution Target
  participant A as Activation Owner
  D-->>O: kristal.artifact.ready + RuntimePack ArtifactRef
  O->>T: knowledge.distribution.request
  T->>T: verify manifest/hash/signature/trust/revocation/compatibility
  T->>A: RuntimePackActivationPort
  A-->>T: activation result
  T-->>O: Receipt/Event
```

Un seul activation state est autoritaire. Voir ADR-IK-01.

## 5. Reconsideration

Orgo ne rouvre pas une décision Konnaxion. Il publie un Event, par exemple :

```yaml
class: event
profile:
  id: operational.reconsideration.recommended
  version: 1.0.0
source:
  system: orgo
target:
  system: konnaxion
data:
  reconsideration_recommended: true
  authority_effect: none
```

Konnaxion décide localement de la suite.
