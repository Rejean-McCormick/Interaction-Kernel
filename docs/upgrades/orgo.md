# Upgrade guide — Orgo

## Objective

Faire d’Orgo l’implémentation de référence d’IK-Reliable en **réutilisant** son infrastructure actuelle plutôt qu’en créant un second bus/runtime de persistence.

## CURRENT — verified snapshot

| Element | Current state |
|---|---|
| `Signal` | persistence avec org/world/release, idempotency, external reference, request hash, correlation |
| `IntegrationOperation` | provider/operation/subject/idempotency/correlation/request metadata/receipt/error |
| `OutboxMessage` | `PENDING/PROCESSING/SUCCEEDED/DEAD`, attempts, locks, correlation/causation |
| `OutboxWorker` | at-least-once, backoff+jitter, dead state, provider adapters |
| `KonnaxionAdapter` | `HttpBridge`, allowlist publish/distribute |
| `KristalAdapter` | skeleton `HttpBridge`, allowlist validate |
| External boundary | port/adapter ACL; external types s’arrêtent à la frontière |
| Kristal workflow records | `TARGET` Kristal v5/kOA; pas présents comme implémentation complète dans snapshot |

## Target architecture

```text
Signal → Workflow → Case/Task
   ▲                 │
   │ IK inbound      │
   │                 ▼
IntegrationOperation + OutboxMessage
              │
           IK Adapter
       ┌──────┼────────┐
       │      │        │
 Konnaxion   Da'at   others
 profiles   profiles
       │
 existing OutboxWorker
       │
 transport binding
```

## Required changes

| ID | Change | Nature |
|---|---|---|
| `OR-01` | faire évoluer `IntegrationPort` ou ajouter façade `IkIntegrationPort` | refactor |
| `OR-02` | mapper `IntegrationOperation` → IK Command | refactor |
| `OR-03` | réutiliser `OutboxMessage/OutboxWorker` comme EmissionPort/DeliveryWorker | preserve |
| `OR-04` | ajouter inbound IK Konnaxion→Orgo avec Signal idempotent | new |
| `OR-05` | mapper `governance.decision.execute` vers Signal + workflow; jamais Case/Task direct | new |
| `OR-06` | ajouter `ArtifactLink` léger | new |
| `OR-07` | ajouter `OrgoExport v1` | new |
| `OR-08` | faire pointer KristalAdapter vers Da’at | refactor |
| `OR-09` | réutiliser/upgrader `BuildRecord` et `ReleaseRecord` kOA; pas de famille parallèle Kristal | implementation + upgrade |
| `OR-10` | séparer compile/review/validation/recognition/publication/distribution | new |
| `OR-11` | émettre Receipt/Event IK depuis transitions Orgo; aucun `ArtifactOutcome` | new |

## IntegrationOperation mapping

| IntegrationOperation | IK |
|---|---|
| `provider` | target/system route ou adapter selection |
| `operation` | Profile mapping + operation sémantique si nécessaire |
| `subject_type/id` | `subject` |
| `idempotency_key` | `idempotency_key` |
| `correlation_id` | `correlation_id` |
| `request_metadata` | `data + artifact_refs` après mapping |
| `receipt` | Receipt IK canonique + provider-local data |
| `external_reference` | external artifact/business ref |

La table existante reste Orgo-owned. Aucun schema IK universel n’est imposé.

## Inbound Konnaxion → Orgo

```text
IK Command governance.decision.execute
  ↓ authenticate + Profile/schema + authorization
  ↓ dedup via Signal idempotency boundary
Signal(source=konnaxion, external_reference=decision_ref)
  ↓ published WorkflowVersion
Case / Tasks / assignments
  ↓
Receipt + outcome Events
```

## OrgoExport v1

```yaml
profile: orgo.export/1.0.0
producer: orgo
subjects:
  - case_ref
  - task_ref
  - workflow_ref
artifact_refs:
  - observations
  - evidence
  - execution results
  - review refs
  - release/build refs
provenance:
  workflow_version: "..."
  correlation_id: "..."
privacy:
  redaction_profile: "..."
```

## Kristal workflow records

### BuildRecord

Réutiliser le contrat kOA existant et l’upgrader vers v5 : inputs pinnés, Kristal pin, stage statuses, outputs, reason codes, correlation. Les gates sont **par stage**, pas un pass/fail global.

### ReleaseRecord

Réutiliser le contrat kOA existant : build ref, artifacts, channels/cohorts, policies, rollout state, verification/activation outcomes, rollback/revocation refs.

### ArtifactLink

Projection locale légère vers un ArtifactRef externe; elle ne copie pas le payload Kristal.

## Impacted files

| Path | Action |
|---|---|
| `apps/api/src/orgo/integrations/port.ts` | façade/profile mapping IK; préserver `DeliveryError` |
| `apps/api/src/orgo/integrations/konnaxion/konnaxion.adapter.ts` | compatibility adapter puis profile-driven |
| `apps/api/src/orgo/integrations/kristal/kristal.adapter.ts` | gateway Da’at/Profile pack; alias migration possible |
| `apps/api/src/orgo/modules/integrations/operations.service.ts` | mapper/créer opérations IK sans changer ownership |
| `apps/api/src/orgo/platform/outbox/worker.service.ts` | réutiliser; ne pas dupliquer |
| `apps/api/src/orgo/modules/intake/*` | point d’arrivée des Commands après admission |
| `apps/api/prisma/schema.prisma` | ajouter uniquement persistence manquante pour Build/Release/ArtifactLink |

## Migration gates

| Phase | Deliverable | Gate |
|---|---|---|
| `OR-P0` | façade IK sur outbound actuel | J30 identique |
| `OR-P1` | inbound `governance.decision.execute` | direct KX→Orgo end-to-end |
| `OR-P2` | ArtifactRef + ArtifactLink + OrgoExport | aucun payload Kristal copié dans Case/Task |
| `OR-P3` | Da’at/Kristal Profiles | KristalAdapter ne reste pas validate-only |
| `OR-P4` | BuildRecord + ReleaseRecord v5 semantics | conformance Kristal Orgo Workflow Contract |
| `OR-P5` | feedback/revision/fork loops | aucune mutation in-place des Exchange |
