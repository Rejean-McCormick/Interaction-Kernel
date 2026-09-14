# Open architecture decisions

Ces ADRs doivent être résolues avant `spec-lock`.

| ADR | Decision | Gate |
|---|---|---|
| [ADR-IK-01](ADR-IK-01-runtime-pack-activation-owner.md) | owner de l’activation Runtime Pack sous kOA-Linux | un seul activation state autoritaire |
| [ADR-IK-02](ADR-IK-02-kristal-v5-pin.md) | pin Kristal v5 exact | commit/digest + schema set + vectors |
| [ADR-IK-03](ADR-IK-03-konnaxion-canonical-handoff-object.md) | objet canonique de handoff Konnaxion | model/service/event canonique avant outbound |
| [ADR-IK-04](ADR-IK-04-canonical-reliable-fingerprint.md) | fingerprint canonique IK-Reliable | golden vectors Python/TS |

## Status convention

- `Proposed`
- `Accepted`
- `Superseded`
- `Rejected`

Aucune ADR `Proposed` ne doit être interprétée comme une décision normative déjà prise.
