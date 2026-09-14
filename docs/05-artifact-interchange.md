# Artifact Interchange

Artifact Interchange permet aux interactions de référencer des données/artefacts externes sans transformer IK en document store.

## ArtifactRef

```yaml
artifact_ref:
  owner:
    system: "kristal"

  artifact_type: "kristal.runtime_pack"
  artifact_id: "kristal:runtime-pack:..."
  version: "5.0"

  integrity:
    algorithm: "sha256"
    digest: "abc..."

  locator:
    ref: "artifact-store://opaque-ref"

  content:
    media_type: "application/json"
    contract_ref: "pinned://kristal-v5/runtime-pack-manifest.schema.json"

  scope:
    organization: "uckk"

  provenance:
    source_refs: []
    generated_at: "..."

  access:
    classification: "internal"
```

### Rules

- `IK-ART-001` — **MUST NOT** : référencer un artefact ne transfère pas son ownership et ne prouve ni authority ni validation.
- `IK-ART-002` — **MUST** : `artifact_id` est défini par l’owner. Le digest n’est identité universelle que si le Profile le dit.
- `IK-ART-003` — **MUST NOT** : un locator ne contient pas de secret/credential embarqué.

## ExportManifest

Un ExportManifest est un snapshot source-owned destiné à consommation externe.

```yaml
export_manifest:
  id: "kx-export:D009:001"
  profile: "konnaxion.export/1.0.0"

  producer:
    system: "konnaxion"

  snapshot_at: "..."
  source_revision: "..."

  scope:
    organization: "uckk"
    world: "uckk-a014"

  subjects:
    - type: "decision"
      id: "D009"

  items:
    - type: "canonical_decision_artifact"
      ref: "konnaxion://decision/D009@revision"
      digest: "sha256:..."
    - type: "evidence"
      ref: "..."
      digest: "sha256:..."

  intended_use:
    - "kristal_compilation"

  provenance: {}
  integrity:
    algorithm: "sha256"
    digest: "..."
```

Le même squelette s’applique à `orgo.export/1.0.0`. Le contenu reste défini par le système producer.

`IK-ART-004` — **MUST** : un export destiné à reproduction/compilation référence des snapshots immuables ou pinne une revision/digest. Une URL mutable sans revision ne suffit pas.

## No ArtifactOutcome

IK ne définit pas de `ArtifactOutcome`.

```text
build Command
  → Receipt accepted/failed
  → Event kristal.artifact.ready
       + ArtifactRef[]
```

Cela évite un troisième mécanisme de résultat redondant.

## No central artifact store

`ArtifactRef.locator` peut référencer :

- un store Kristal;
- un store Konnaxion;
- un evidence store Orgo;
- object storage;
- content-addressed storage;
- un bundle offline.

IK ne possède pas les bytes.
