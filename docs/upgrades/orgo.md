# Orgo upgrade

Reuse existing infrastructure rather than duplicating it:

- `IntegrationOperation` → IK semantic operation projection;
- `OutboxMessage/OutboxWorker` → IK-Reliable delivery implementation;
- inbound `governance.decision.execute` → idempotent Signal → published WorkflowVersion → Case/Tasks;
- `ArtifactLink` projection only, not artifact ownership;
- `OrgoExport v1`;
- Kristal adapter routes through Da’at;
- reuse/upgrade existing kOA BuildRecord/ReleaseRecord contracts.

Reference mapping: [`adapters/orgo-typescript/`](../../adapters/orgo-typescript/).
