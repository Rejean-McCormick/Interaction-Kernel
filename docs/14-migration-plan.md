# Migration plan

La migration est incrémentale. Le principe est **wrapper first, extraction later**.

| Step | Systems | Goal | Exit gate |
|---|---|---|---|
| `D0 — Contract lock` | IK | figer Core 1.1 + Artifact Interchange + Profiles initiaux | Core schemas/TCK verts |
| `D1 — Preserve outbound` | Orgo + Konnaxion | wrapper le bridge J30 actuel sans changer son comportement | exactly-one impact effect toujours vert |
| `D2 — Direct decision handoff` | Konnaxion + Orgo | résoudre ADR-IK-03 puis direct KX→Orgo | source canonique + Signal/Workflow/Case/Tasks idempotents |
| `D3 — Artifact layer` | IK + KX + Orgo | ArtifactRef/ExportManifest + KonnaxionExport/OrgoExport | exports déterministes/minimisés |
| `D4 — Da’at v5` | Da’at + kOA + Kristal | pin v5, migration v4→v5, Profiles IK-Kristal | pin/schema/vectors/TCK verts |
| `D5 — Orgo Kristal workflow` | Orgo + Da’at | upgrader BuildRecord/ReleaseRecord + artifact loops | Orgo Workflow Contract v5 couvert |
| `D6 — Konnaxion distribution` | Konnaxion + kOA-Linux | verification Runtime Pack + activation ownership explicite | ADR-IK-01 résolue, aucun double activation state |
| `D7 — Deprecate bespoke` | tous | retirer uniquement ce qui est remplacé et observé | aucune route critique sans replacement/TCK |

## Recommended order

1. Ne pas attendre tous les bindings avant de brancher Konnaxion/Orgo.
2. Valider d’abord les deux directions réelles : Orgo→Konnaxion et Konnaxion→Orgo.
3. Ajouter Artifact Interchange ensuite.
4. Migrer Da’at vers Kristal v5 après stabilisation des records artifact.
5. Déprécier uniquement après conformance + observability + redrive.

## Why this order

Cette séquence évite de faire bouger simultanément :

- le protocole IK;
- les frontières Konnaxion/Orgo;
- la frontière Da’at;
- le modèle Kristal v4→v5.

Elle permet de prouver chaque abstraction avec un flux réel avant extraction de code partagé.
