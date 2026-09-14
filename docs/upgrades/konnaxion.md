# Upgrade guide — Konnaxion

## Objective

Adapter Konnaxion à IK **à la frontière** sans réécrire Ethikos/Korum/Smart Vote/impact/accountability.

## CURRENT — verified snapshot

| Element | Current state |
|---|---|
| Orgo→Konnaxion bridge | implémenté via `backend/konnaxion/ethikos/orgo_bridge_*.py` |
| Contract | `operation=publish`, `subject=case`, `artifact_type=impact_update`; idempotency/correlation obligatoires |
| Privacy | clés student/private explicitement rejetées |
| Persistence | `OrgoImpactPublication`; Orgo IDs comme refs, jamais FK |
| World/Release | résolution du World courant; maintenance/archive/not-ready fail-closed |
| DecisionRecord | `TARGET` Kintsugi; non présent dans `models.py` du snapshot |
| Generic outbound reliable delivery | aucun outbox générique détecté |
| Kristal Runtime Pack runtime | non détecté dans Konnaxion snapshot |

## Target architecture

```text
Konnaxion domain
├── ethiKos / Korum / Smart Vote / Impact
│
├── integrations/interaction_kernel/
│   ├── inbound_adapter.py
│   ├── outbound_adapter.py
│   ├── profiles.py
│   ├── admission.py
│   ├── emission.py
│   └── exports.py
│
├── existing Orgo bridge compatibility surface
│   └── wraps accountability.impact.publish
│
└── kristal_consumption/
    ├── artifact/pack verification adapter
    ├── reader-policy/application projection
    └── activation port → Konnaxion-local OR delegated kOA-Linux
```

## Required changes

| ID | Change | Nature |
|---|---|---|
| `KX-01` | créer adapter IK inbound vers services Konnaxion owner-owned | new |
| `KX-02` | wrapper le bridge actuel comme `accountability.impact.publish` | low refactor |
| `KX-03` | implémenter/désigner l’objet canonique de décision avant `governance.decision.execute` | domain decision |
| `KX-04` | ajouter un `EmissionPort` durable transactionnel | new |
| `KX-05` | émettre le handoff depuis la décision canonique finalisée avec IDs stables | new |
| `KX-06` | ajouter `KonnaxionExport v1` | new |
| `KX-07` | supporter `ArtifactRef`/`ExportManifest` sans copier Kristal dans l’état civique | small |
| `KX-08` | ajouter verification Kristal v5 + `RuntimePackActivationPort` | boundary + ADR |
| `KX-09` | émettre Events depuis le véritable activation owner | new |
| `KX-10` | préserver World/Release scoping et fail-closed | preserve |

## Reliable outbound handoff

```text
finalize canonical decision object
  ├─ domain commit
  └─ durable InteractionEmission
       profile = governance.decision.execute
       idempotency = decision:<id>:orgo:execute:v1
       correlation = decision/process correlation
       target = orgo
       ↓ worker
       ↓ IK Command
```

L’intention d’émission doit être atomiquement liée à la finalisation, ou capturée par un mécanisme de commit équivalent.

## KonnaxionExport v1

```yaml
profile: konnaxion.export/1.0.0
producer: konnaxion
subjects:
  - decision_ref
artifact_refs:
  - canonical_decision_artifact
  - baseline_result
  - reading_results
  - rationale/evidence refs
  - impact/accountability refs
provenance:
  world/release: "..."
  source_event_refs: []
integrity:
  canonical_export_hash: "..."
```

Le type concret de l’objet de décision dépend de [ADR-IK-03](../adrs/ADR-IK-03-konnaxion-canonical-handoff-object.md).

## Impacted files

| Path | Action |
|---|---|
| `backend/konnaxion/ethikos/orgo_bridge_contract.py` | conserver comme compatibility mapper; migrer les règles use-case vers Profile/adapter |
| `backend/konnaxion/ethikos/orgo_bridge_views.py` | déléguer admission/mutation au nouvel adapter sans casser la route initialement |
| `backend/konnaxion/ethikos/models.py` | conserver `OrgoImpactPublication`; ajouter uniquement les modèles réellement nécessaires |
| `backend/konnaxion/integrations/interaction_kernel/*` | nouveau package cible |
| `backend/konnaxion/integrations/kristal_distribution/*` | seulement si Konnaxion remplit directement ce rôle |

## Migration gates

| Phase | Deliverable | Gate |
|---|---|---|
| `KX-P0` | tests bridge actuels verts | aucune régression J30 |
| `KX-P1` | Profile wrapper impact publish | même Receipt + exactly-one effect |
| `KX-P2` | objet décision canonique + event finalisé | source d’autorité explicite |
| `KX-P3` | EmissionPort + direct KX→Orgo | retry sans double Case/effect |
| `KX-P4` | KonnaxionExport + ArtifactRefs | export déterministe/source-owned |
| `KX-P5` | Runtime Pack consumption/activation boundary | ADR activation owner + Kristal Distribution conformance |
