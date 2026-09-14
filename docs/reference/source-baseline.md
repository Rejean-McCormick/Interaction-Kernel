# Source baseline and traceability

Cette documentation est dérivée des snapshots fournis et distingue l’état actuel des propositions.

## Konnaxion

Principales références :

- `backend/konnaxion/ethikos/orgo_bridge_contract.py`
- `backend/konnaxion/ethikos/orgo_bridge_views.py`
- `backend/konnaxion/ethikos/models.py`
- Kintsugi ownership/data model/canonical object/event documentation

### Verified implications

- bridge Orgo→Konnaxion déjà implémenté;
- idempotency/correlation/provider-owned persistence déjà présentes;
- World/Release fail-closed existe;
- `DecisionRecord` reste une cible documentée, pas un modèle canonique vérifié dans le snapshot courant;
- aucun outbox générique Konnaxion confirmé dans le snapshot.

## Orgo

Principales références :

- `docs/Technical-Reference/TARGET_ARCHITECTURE.md`
- `docs/Technical-Reference/BOUNDARIES_AND_OWNERSHIP.md`
- `apps/api/src/orgo/modules/integrations/operations.service.ts`
- `apps/api/src/orgo/platform/outbox/worker.service.ts`
- `apps/api/src/orgo/integrations/port.ts`
- `apps/api/prisma/schema.prisma`

### Verified implications

- `IntegrationOperation`, Outbox and worker already separate external-operation state from delivery state;
- adapters stop external types at the boundary;
- Orgo is the best initial host for IK-Reliable reuse;
- BuildRecord/ReleaseRecord semantics should be mapped to the kOA/Kristal contracts, not re-invented.

## kOA Digital Ecosystem

Principales références :

- `docs/2-Technical-Reference/20-nodes/daat-kristal-bridge.md`
- `docs/2-Technical-Reference/40-integration/orgo-konnaxion/index.md`
- `docs/2-Technical-Reference/40-integration/kristal-v4/*`
- artifact contracts such as `build-record`, `release-record`, `orgo-case`, `orgo-task`, `konnaxion-state`

### Verified implications

- Da’at exists already as the Kristal boundary;
- current Kristal integration documentation is still v4-centric;
- artifact/build/release contracts already exist and should be upgraded, not duplicated.

## Kristal v5

Principales références :

- `01-core-spec/kristal-v5-core-spec.md`
- `01-core-spec/structured-epistemic-state.md`
- `06-integration/orgo-workflow-contract.md`
- `06-integration/konnaxion-distribution-contract.md`
- `04-query/query-contract.md`
- schemas, security docs, golden vectors

### Verified implications

- Kristal owns epistemic artifacts, not workflow/governance;
- validation, certainty and authority recognition are distinct;
- Orgo is workflow control plane for Kristal-related operations;
- Konnaxion distribution responsibilities exist in the Kristal contract but activation ownership under kOA-Linux remains an integration ADR;
- local Query Contract should not be replaced by IK Query without a real inter-system boundary.

## Traceability summary

| Target decision | Source evidence | IK action |
|---|---|---|
| owner unique / no cross-write | Orgo/Konnaxion ownership docs | normative Core invariant |
| Command/Query/Event | kOA/Orgo integration doctrine | formalize Core |
| Outbox + IntegrationOperation separate | Orgo code | reuse in IK-Reliable |
| KX inbound impact bridge | Konnaxion bridge code/tests | wrap as Profile |
| KX direct decision handoff | target gap | resolve ADR-IK-03 + implement |
| Da’at Kristal boundary | kOA node docs | upgrade to IK gateway + v5 ACL |
| Kristal v5 ownership split | Kristal core/integration contracts | preserve core; adapt boundaries |
| Runtime Pack activation | conflicting owner responsibilities | ADR-IK-01 + ActivationPort |
