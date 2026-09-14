# Repository and package model

## Target repository

```text
interaction-kernel/
├── README.md
├── CONTRIBUTING.md
├── spec/
│   ├── core/
│   ├── reliable/
│   ├── artifacts/
│   ├── authority/
│   ├── errors/
│   └── bindings/
├── contracts/
│   ├── profiles/
│   │   ├── konnaxion-orgo/
│   │   └── kristal/
│   ├── schemas/
│   ├── capabilities/
│   └── compatibility/
├── runtime/
│   ├── python/
│   └── typescript/
├── adapters/
│   ├── konnaxion/
│   ├── orgo/
│   └── daat/
├── bindings/
│   ├── http/
│   ├── messaging/
│   └── offline/
├── conformance/
│   ├── core-tck/
│   ├── module-tck/
│   └── scenario-tests/
└── docs/
```

## Package boundaries

### `ik-contracts`

Schemas, Profile definitions, descriptors et generated types. Aucun service central obligatoire.

### `ik-runtime-py`

Runtime/ports pour participants Python. Doit réutiliser les stores/workers du host lorsque possible.

### `ik-runtime-ts`

Runtime/ports pour participants TypeScript. Côté Orgo, il se branche sur `IntegrationOperation/Outbox/worker` plutôt que de les dupliquer.

### `ik-adapter-konnaxion`

ACL entre IK et les services Konnaxion. Ne possède aucun état civique.

### `ik-adapter-orgo`

ACL entre IK et Signal/Workflow/Case/Task/IntegrationOperation. Ne redéfinit pas leurs lifecycles.

### `ik-adapter-daat`

Gateway IK vers les contrats natifs Kristal v5.

## Non-goals du repository

Ne pas inclure :

- Kristal core;
- modèles métier Konnaxion/Orgo;
- secrets/trust roots production;
- artifact store global;
- policy database globale.
