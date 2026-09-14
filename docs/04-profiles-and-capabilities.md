# Profiles and capabilities

## Profile

Le Profile est l’unité principale d’extension sémantique. Il définit :

- classe (`command/query/event`);
- schema de payload;
- claims d’autorité acceptables;
- artifacts requis/optionnels;
- capability cible;
- durabilité et idempotence;
- receipts attendus;
- outcome Events attendus;
- privacy/governance constraints.

Le Profile pinne ses schemas afin d’éviter une négociation indépendante `Profile × Schema`.

## Example — Kristal-gated deployment

```yaml
profile:
  id: "regulated.protocol.deploy"
  version: "1.0.0"
  class: "command"

  target_capability: "governed-work"

  authority:
    accepted_kinds:
      - "governance-mandate"

  artifacts:
    kristal:
      requirement: "required" # none | optional | required
      accepts:
        - type: "kristal.runtime_pack"
          source_status:
            - "reference"

  delivery:
    durability: "durable"
    idempotency: "required"

  response:
    acceptance_receipt: "required"
    final_receipt: "required"
```

## Capabilities

Capabilities appartiennent au **control plane**. Elles servent à vérifier/configurer qu’un participant accepte certains Profiles. Elles ne donnent jamais :

- trust;
- authority;
- permission de routage automatique.

`IK-CAP-001` — **MUST** : pour une Command gouvernée, le mapping `Profile/capability → receiver` est configuré/allowlisté localement.

## Initial profile families

### Konnaxion ↔ Orgo

- `governance.decision.execute`
- `accountability.impact.publish`
- `operational.reconsideration.recommended`

### Da’at / Kristal

- `kristal.build.request`
- `kristal.artifact.ready`
- `kristal.revision.request`
- `knowledge.distribution.request`

Les Profiles Kristal parlent à **Da’at**. Kristal reste derrière l’ACL/gateway.
