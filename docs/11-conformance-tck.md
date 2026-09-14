# Conformance and TCK

IK utilise des **claims modulaires**. Une implémentation ne prétend supporter que les modules réellement testés.

| Claim | Minimal test surface |
|---|---|
| `IK-Core/1.1` | records, Envelope, Profile, versions, errors, Receipt/QueryResult, causality |
| `IK-Reliable/1` | idempotency, retry/redrive, unknown outcome, admission/dedup |
| `IK-HTTP/1` | auth, header/body consistency, status mapping |
| `IK-Artifact/1` | ArtifactRef owner/id/digest/locator; ExportManifest ownership/immutability |
| `IK-Kristal/1` | Da’at mapping, v5 pin/schema validation, validation≠recognition, artifact handoff |
| `IK-KX-ORGO/1` | direct KX→Orgo + Orgo→KX exactly-one business effect |

## Core TCK expectations

### Positive vectors

- valid Command / Query / Event;
- valid Receipt / QueryResult;
- compatible Profile versions;
- idempotent replay of identical semantic request.

### Negative vectors

- unknown protocol/Profile;
- schema failure;
- unauthorized request;
- same idempotency key with divergent semantic content;
- invalid ArtifactRef locator credentials;
- mutable export without revision/digest when reproducibility required.

## Reliable golden vectors

Python et TypeScript doivent calculer le même fingerprint pour la même requête sémantique. Les champs volatils (`time`, `trace`) sont exclus.

Voir [ADR-IK-04](adrs/ADR-IK-04-canonical-reliable-fingerprint.md).

## Scenario tests

UCKK-A014 peut rester un test end-to-end, mais :

`IK-CONF-001` — **MUST NOT** : un scénario métier particulier ne définit jamais IK Core.
