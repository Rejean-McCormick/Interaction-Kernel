# Versioning and compatibility

## Version axes

IK 1.1 sépare les axes suivants :

| Axis | Rule |
|---|---|
| IK protocol | validé/négocié explicitement, ex. `ik/1.1` |
| Profile | version sémantique du use case; breaking change → major |
| Payload schema | pinné par le Profile; pas de négociation indépendante en 1.1 |
| Artifact schema | possédé par l'artifact owner; ex. Kristal schemas pinnés par Da’at |
| Runtime implementation | diagnostique seulement; ne change pas le sens d’un record conforme |

## Immutability

`IK-VERS-001` — **MUST** : une version publiée de Profile/schema est immuable.

Un changement sémantique ne modifie pas une version existante. Il produit une nouvelle version.

## Compatibility failure

`IK-VERS-002` — **MUST** : une incompatibilité connue est rejetée explicitement. Aucune interprétation best-effort silencieuse.

Examples :

- protocol version non supportée;
- Profile major non supportée;
- artifact contract/pin non compatible;
- required extension inconnue.

## Recommended semantic versioning policy

> **IK PROPOSAL** — convention de repository, à confirmer au spec-lock.

- `MAJOR` — changement breaking de sémantique ou obligation;
- `MINOR` — capacité additive backward-compatible;
- `PATCH` — clarification/correction sans changement de compatibilité runtime.

## Profile and schema pinning

Un Profile publié référence un schema déterminé :

```yaml
profile:
  id: governance.decision.execute
  version: 1.2.0
payload_schema:
  ref: schemas/governance.decision.execute/1.2.0.json
```

IK 1.1 évite volontairement une négociation indépendante de plages Profile × Schema.

## Artifact compatibility

Les artifacts externes ne sont pas re-versionnés par IK. Un `ArtifactRef` porte :

- owner-defined artifact ID;
- artifact type/version;
- integrity digest;
- contract/schema reference lorsque nécessaire.

Pour Kristal, Da’at pinne le set v5 exact retenu par [ADR-IK-02](adrs/ADR-IK-02-kristal-v5-pin.md).

## Deprecation

Une ancienne route, adapter ou Profile n’est supprimé que lorsque :

1. replacement opérationnel;
2. conformance tests verts;
3. observability disponible;
4. redrive/reconciliation validés;
5. aucun consumer actif non migré connu.
