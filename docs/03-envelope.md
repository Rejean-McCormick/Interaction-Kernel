# Interaction Envelope

## Canonical shape

```yaml
specversion: "ik/1.1"
id: "01J..."
class: "command"
time: "2026-09-13T20:15:00Z"

profile:
  id: "governance.decision.execute"
  version: "1.0.0"

source:
  system: "konnaxion"
  organization: "uckk"

target:
  system: "orgo"
  organization: "uckk"
  world: "uckk-a014"

subject:
  type: "decision"
  id: "D009"

authority:
  kind: "governance-mandate"
  claims:
    - "authority://konnaxion/decision/D009"

correlation_id: "corr:D009"
causation_id: null
idempotency_key: "decision:D009:orgo:execute:v1"

data_schema: "ik://profiles/governance.decision.execute/1.0.0/schema"
data: {}

artifact_refs: []

response:
  acceptance_receipt: true
  final_receipt: true

governance:
  sensitivity: "internal"
  purposes: ["governed_execution"]

trace:
  traceparent: null
  tracestate: null
```

## Field semantics

| Field | Rule |
|---|---|
| `specversion` | version du protocole IK |
| `id` | ID unique du record; stable pour retry/redrive du même record |
| `class` | `command`, `query`, `event` |
| `profile` | porte la sémantique use-case |
| `source` | émetteur authentique du record; un gateway reste la source technique réelle |
| `target` | receiver concret pour Command/Query durable |
| `subject` | référence métier, jamais FK cross-system implicite |
| `correlation_id` | processus/conversation métier |
| `causation_id` | interaction causale directe |
| `idempotency_key` | requise pour mutation durable retryable |
| `authority` | claims évalués localement par le receiver/Profile |
| `data` | payload minimal défini par le Profile |
| `artifact_refs` | références externes; les bytes restent hors Envelope par défaut |
| `response` | receipts/outcomes attendus |
| `governance` | sensitivity, purpose, expiry, policy refs |
| `trace` | observabilité technique, distincte de la correlation métier |

## Concrete receiver

`IK-ENV-001` — **MUST** : une Command ou Query durable possède un receiver concret avant l’émission durable. Une capability peut aider à résoudre ce receiver mais ne remplace pas la destination.

## Gateway identity

Dans la baseline Kristal :

```yaml
source:
  system: daat

artifact_refs:
  - owner:
      system: kristal
```

Da’at ne se fait pas passer pour Kristal au niveau transport. L’ownership de l’artefact reste explicite dans `ArtifactRef` et sa provenance.
