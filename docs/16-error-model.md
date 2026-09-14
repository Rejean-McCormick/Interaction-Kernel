# Error model

> **Status:** `IK PROPOSAL` pour la taxonomie détaillée ci-dessous. Les principes `fail-closed`, `accepted ≠ succeeded`, idempotency conflict et incompatibility rejection sont déjà partie de l’architecture 1.1-draft-r2.

## Principle

Les erreurs doivent rester machine-readable et distinguer :

- transport;
- protocol/schema/Profile;
- authentication/trust;
- authorization/admission;
- idempotency;
- receiver temporary failure;
- receiver permanent failure;
- business rejection;
- unknown outcome.

## Recommended categories

| Code | Default retry | Meaning |
|---|---:|---|
| `IK_INVALID_ENVELOPE` | no | Envelope mal formée |
| `IK_UNSUPPORTED_PROTOCOL` | no | protocol version non supportée |
| `IK_UNKNOWN_PROFILE` | no | Profile inconnu |
| `IK_INCOMPATIBLE_VERSION` | no | version Profile/artifact contract incompatible |
| `IK_SCHEMA_VALIDATION_FAILED` | no | payload/schema invalide |
| `IK_UNAUTHENTICATED` | no | credential absent/invalide |
| `IK_UNAUTHORIZED` | no | authority/policy refusée |
| `IK_BLOCKED` | contextual | prerequisite ou contexte bloque temporairement l’action |
| `IK_IDEMPOTENCY_CONFLICT` | no | même key, requête sémantique divergente |
| `IK_TARGET_NOT_FOUND` | no | target/scope inconnu |
| `IK_TARGET_NOT_READY` | maybe | target connu mais non prêt |
| `IK_PROVIDER_UNAVAILABLE` | yes | provider temporairement indisponible |
| `IK_RATE_LIMITED` | yes | backoff nécessaire |
| `IK_RECEIPT_CONFLICT` | no | terminal Receipt divergent déjà enregistré |
| `IK_UNKNOWN_OUTCOME` | reconcile | commit externe incertain |

## Retry rules

Retry ne doit jamais être décidé uniquement par le status HTTP. Le binding mappe la réponse vers une erreur/disposition IK, puis la delivery policy décide.

### Retryable

Typiquement :

- timeout avant réponse;
- `429`;
- provider/network temporairement indisponible;
- certains `5xx`.

### Non-retryable

Typiquement :

- schema invalide;
- unauthorized;
- unsupported Profile/version;
- idempotency conflict;
- permanent business rejection.

## Unknown outcome

Une coupure après l’envoi peut laisser le sender incapable de savoir si le receiver a commis l’effet.

Le sender doit :

1. **ne pas** créer une nouvelle idempotency identity;
2. tenter reconciliation/query/receipt lookup selon le Profile/binding;
3. redriver la même identité seulement lorsque sûr;
4. conserver un état local observable `unknown_outcome` ou équivalent.

## Error ownership

Le receiver définit les erreurs de son interface publique. Le sender ne corrige jamais directement la persistence du receiver après erreur.

Les adapters peuvent conserver le code local/provider dans `detail`/`data` lorsque la privacy policy le permet, sans exposer les modèles internes comme contrat IK.
