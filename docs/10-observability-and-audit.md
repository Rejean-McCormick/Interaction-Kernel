# Observability and audit

## Distinct planes

Observability technique et audit métier peuvent partager des IDs, mais restent conceptuellement séparés.

| Signal | Recommended fields |
|---|---|
| logs | `interaction_id`, Profile, participant, `correlation_id`, disposition/error; aucun secret |
| metrics | emit/receive, receipt latency, retry/dead, dedup hits, validation failures, incompatible versions |
| traces | transport → admission → adapter → domain handler |
| audit | qui a tenté/accepté/muté quoi, selon le receiver owner |
| provenance | source refs, artifact hashes, lineage |

## Correlation vs causation vs trace

- `correlation_id` : conversation/processus métier partagé;
- `causation_id` : interaction directe ayant causé le record courant;
- `traceparent/tracestate` : trace technique distribuée.

Ne pas utiliser une trace technique comme remplacement de la causalité métier.

## Sensitive logging

Les logs ne doivent pas contenir :

- bearer token;
- signature/private key;
- credentials Artifact locator;
- payload sensible non nécessaire au diagnostic.

## Reliability metrics

Au minimum :

- delivery attempts;
- retry rate;
- dead rate;
- idempotent replay hits;
- idempotency conflicts;
- unknown outcome backlog;
- receipt latency;
- Profile/schema incompatibilities.
