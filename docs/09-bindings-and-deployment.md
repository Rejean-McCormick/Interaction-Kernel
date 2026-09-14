# Bindings and deployment

## Conformance modules

| Module | Obligation |
|---|---|
| `IK-Core` | requis pour toute implémentation |
| `IK-Reliable` | requis pour Commands durables / effets garantis |
| `IK-HTTP` | optionnel; binding initial recommandé |
| `IK-Messaging` | optionnel |
| `IK-Offline` | optionnel |
| `IK-Artifact` | requis si `ArtifactRef`/`ExportManifest` utilisés |
| `IK-Kristal` | requis pour Da’at/participants exposant les Profiles Kristal |

## HTTP

Les paths HTTP ne sont **pas normatifs**. Un système peut conserver ses endpoints existants derrière un adapter.

La conformité porte sur :

- authentication;
- Envelope/Profile/schema;
- idempotency;
- correlation;
- disposition/Receipt;
- error mapping.

### Suggested status semantics

| HTTP | Meaning |
|---|---|
| `200/201` | final response disponible; vérifier le body |
| `202` | accepted non-terminal |
| `400/422` | validation/Profile/schema error |
| `401/403` | authentication/authorization failure |
| `409` | idempotency conflict ou state conflict |
| `429/5xx` | retryable selon policy |

HTTP 2xx n’est pas un business outcome universel.

## Messaging

Le broker ack reste un transport acknowledgement. Les redeliveries sont normales et doivent passer par admission/dedup.

## Offline

Offline ne baisse jamais les exigences de trust. Les contracts/profiles nécessaires doivent être pinnés localement et leur origine vérifiable.

## Deployment principle

Il n’existe pas de serveur IK central obligatoire.

```text
Konnaxion + local IK runtime  ⇄ transport ⇄ local IK runtime + Orgo
                                         ⇅
                                      Da’at
                                         ⇅
                                      Kristal
```
