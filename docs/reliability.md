# Reliability

Reference semantics: **at-least-once delivery + idempotent processing + reconciliation**.

`idempotency_key` identifies the logical effect. `request_fingerprint` identifies the semantic request content.

```text
same key + same fingerprint     => replay, no new effect
same key + different fingerprint => IK_IDEMPOTENCY_CONFLICT
```

Fingerprint profile: `ik.request-fingerprint/jcs-rfc8785+sha256/v1`.

Semantic projection includes class/profile/source/target/subject/operation/authority/data_schema/data/governance/artifact_refs/evidence and excludes id/time/correlation/causation/trace/response/delivery metadata.

Orgo reuses its existing `IntegrationOperation`, `OutboxMessage` and worker. Konnaxion adds or reuses an equivalent durable emission boundary.
