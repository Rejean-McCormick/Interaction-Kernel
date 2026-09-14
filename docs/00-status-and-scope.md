# Status and scope

## Version

`1.1-draft-r2`

## Scope

Interaction Kernel couvre :

- le Core `Command / Query / Event`;
- `Receipt` et `QueryResult` comme records de protocole;
- Profiles et capabilities;
- delivery fiable par ports;
- Artifact Interchange avec `ArtifactRef` et `ExportManifest`;
- bindings optionnels;
- conformance/TCK;
- intégration Kristal via Da’at;
- plans d’upgrade Konnaxion, Orgo et Da’at/kOA.

## Participants IK de référence

- **Konnaxion**
- **Orgo**
- **Da’at**

Kristal reste derrière Da’at dans la baseline. Kristal ne doit pas parser l’Envelope IK.

## Status labels

| Label | Sens | Règle |
|---|---|---|
| `CURRENT` | Vérifié dans code/migrations/tests du snapshot fourni | Le code/test prévaut sur une doc plus ancienne en cas de drift |
| `TARGET` | Contrat ou responsabilité cible déjà documentée par le système owner | Traiter comme gap tant que non implémenté |
| `IK PROPOSAL` | Nouvelle décision introduite par IK | Devient normative seulement après Profile/schema/ADR/TCK approuvé |

## Rule of precedence

En cas de conflit entre deux owners, IK ne tranche pas implicitement. Une ADR de déploiement doit résoudre la frontière avant implémentation.

Exemple actuel : le contrat Kristal v5 cible Konnaxion pour distribution/activation, tandis que la documentation Konnaxion/kOA-Linux réserve l’activation host à kOA-Linux dans certains déploiements. Voir [ADR-IK-01](adrs/ADR-IK-01-runtime-pack-activation-owner.md).

## Spec-lock gates

La version stable exige :

- Core schemas stabilisés;
- Profiles initiaux stabilisés;
- golden vectors IK-Reliable;
- direct Konnaxion→Orgo validé;
- Orgo→Konnaxion exactly-one effect toujours vert;
- Kristal v5 pin explicite;
- les quatre ADRs ouvertes résolues.
