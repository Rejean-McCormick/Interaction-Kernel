# Upgrade guide — Kristal / Da’at

## Decision

**Ne pas modifier le core Kristal v5 pour IK.**

Le travail principal est dans Da’at et dans la documentation/conformance kOA encore v4-centric.

## Kristal core remains normative

Les schemas/core Kristal continuent de définir :

- Structured Epistemic State;
- Exchange;
- validation;
- authority recognition;
- certainty/status;
- Runtime Pack;
- Query Contract;
- signatures/trust roots;
- federation/revocation.

`KR-UP-001` — **MUST NOT** : ajouter des champs IK (`interaction_id`, `target`, Receipt, etc.) aux schemas core Kristal.

`KR-UP-002` — **MUST** : Da’at traduit les modèles; Kristal reste normatif pour ses artifacts.

## Main gap: kOA/Da’at v4 → Kristal v5

Les docs kOA `40-integration/kristal-v4/*` et la logique Da’at associée doivent être migrées vers un pin v5 explicite.

### v4 → v5 differences

| Current assumption | Target |
|---|---|
| Claim-IR/Resolved Claim-IR central | Structured Epistemic State normative; Claim-IR optional |
| global no-compile-on-fail | compile, validation, recognition séparés; Profile/workflow définit les gates |
| Exchange/Runtime Pack focus | working/reference + validation report + recognition + reader policy + federation + revocation |
| floating/legacy v4 pin | exact v5 commit/digest + schemas + vectors |

## Da’at target layout

```text
daat-kristal-gateway/
├── ik/
│   ├── admission/
│   ├── profiles/
│   ├── export-manifest/
│   └── artifact-ref/
├── kristal/
│   └── v5/
│       ├── pinned-contracts/
│       ├── mapper/
│       ├── compiler-client/
│       ├── verifier/
│       └── query-client/
├── provenance/
└── conformance/
```

## IK-Kristal Profiles

| Profile | Class | Meaning |
|---|---|---|
| `kristal.build.request` | command | demander à Da’at un build/compile à partir d’exports/ArtifactRefs |
| `kristal.artifact.ready` | event | artifact Kristal produit/vérifié; refs seulement |
| `kristal.revision.request` | command | créer un nouveau cycle/revision; jamais mutation in-place |
| `knowledge.distribution.request` | command | demander au target de vérifier puis déléguer/appeler le RuntimePackActivationPort |

## Working/reference gates

Un Working Exchange peut être produit avant validation/recognition finale si le Profile l’autorise. La promotion vers Reference/release/distribution reste fail-closed selon les exigences de validation, recognition et policy.

## Source identity

Dans IK :

```yaml
source:
  system: daat

artifact_refs:
  - owner:
      system: kristal
```

## kOA documentation upgrade

| Current | Target |
|---|---|
| `40-integration/kristal-v4/` | `kristal-v5/` ou chemin version-neutral + pin v5 |
| `Integration-Kristal-v4.md` | v5 |
| Da’at v4 role | Da’at IK gateway + Kristal v5 ACL |
| v4 contract pointers | v5 core/schemas/query/security/integration pointers |
| v4 profile | v5 SES, working/reference, validation/recognition, reader policy, federation |
| v4 conformance | v5 + IK-Kristal TCK |

## Kristal repository changes

| Area | Recommendation |
|---|---|
| core spec/schemas | aucun changement IK |
| integration docs | optional interop note describing Da’at mapping as non-normative |
| golden vectors | reuse directly in Da’at conformance |
| Query Contract | use directly for local/runtime query |
| version pin | publish/identify stable version/digest for Da’at/kOA |

## Tests

- same ExportManifest + mapping profile + pin/policy → same canonical handoff where Kristal guarantees determinism;
- incompatible export profile/schema rejected before compile;
- invalid output schema/hash/signature → quarantine/reject;
- working artifact never presented as reference without corresponding status/recognition;
- validation and authority recognition remain distinct;
- feedback creates revision/fork workflow, never in-place Exchange mutation;
- Runtime Pack ready does not activate anything by itself.
