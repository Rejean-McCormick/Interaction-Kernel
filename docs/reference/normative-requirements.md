# Normative requirements

Ce document centralise les exigences normatives actuellement définies par la spec `1.1-draft-r2`.

| ID | Level | Requirement |
|---|---|---|
| `IK-ARCH-001` | MUST NOT | aucun flux Konnaxion↔Orgo ne transite obligatoirement par Kristal sauf knowledge gate explicite |
| `IK-ARCH-002` | MUST | Da’at est la frontière de référence entre IK et les contrats natifs Kristal |
| `IK-ARCH-003` | MUST | chaque participant garde sa source de vérité et mute uniquement son état autoritaire |
| `IK-CORE-001` | SHOULD | refuser d’ajouter au Core une notion exprimable par Profile/binding/adapter/module |
| `IK-ENV-001` | MUST | Command/Query durable possède un receiver concret avant émission durable |
| `IK-CAP-001` | MUST | mapping Profile/capability→receiver gouverné configuré/allowlisté localement |
| `IK-ART-001` | MUST NOT | ArtifactRef ne transfère ni ownership, authority ni validation |
| `IK-ART-002` | MUST | artifact ID owner-defined; digest universel seulement si Profile le déclare |
| `IK-ART-003` | MUST NOT | locator contenant secret/credential embarqué |
| `IK-ART-004` | MUST | export reproductible pinne snapshot/revision/digest immuable |
| `IK-KRISTAL-001` | MUST NOT | IK Admission présenté comme Kristal Validation |
| `IK-KRISTAL-002` | MUST NOT | IK authority claim projeté automatiquement en Kristal Authority Recognition |
| `IK-KRISTAL-003` | MUST | Da’at préserve working/reference, validation, recognition, certainty, scope, reader policy |
| `IK-KRISTAL-004` | MUST NOT | mapping générique ExportManifest→SES sans mapping Profile/version ou extractor déclaré |
| `IK-KRISTAL-005` | MUST | Da’at est sender/receiver IK devant Kristal; ArtifactRef préserve ownership Kristal |
| `IK-REL-001` | MUST | retry/redrive conserve idempotency identity |
| `IK-REL-002` | MUST | replay divergent sous même idempotency identity produit conflit explicite |
| `IK-REL-003` | MUST NOT | exiger une seconde Inbox/Outbox si host satisfait déjà les garanties |
| `IK-REL-004` | MUST | fingerprint déterministe de la requête sémantique + golden vectors multi-langage |
| `IK-REL-005` | MUST | aucun ordre global; ordre Profile-defined si requis |
| `IK-VERS-001` | MUST | Profile/schema publié immuable |
| `IK-VERS-002` | MUST | incompatibilité connue rejetée explicitement; pas de best-effort silencieux |
| `IK-CONF-001` | MUST NOT | un scénario métier particulier définir IK Core |

## Upgrade-specific requirements

### Kristal/Da’at

- `KR-UP-001` — **MUST NOT** : ajouter des champs IK dans les schemas core Kristal.
- `KR-UP-002` — **MUST** : Da’at traduit; Kristal reste normatif pour ses artifacts.
- `KR-UP-003` — **MUST** : upgrader le BuildRecord kOA existant plutôt que créer un record parallèle.
