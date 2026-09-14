# Konnaxion upgrade

Preserve the existing `orgo_bridge_*` J30 implementation and `OrgoImpactPublication`. Wrap it with the IK Profile `accountability.impact.publish` first.

Add:

- IK inbound/outbound adapter boundary;
- immutable `DecisionRecord` contract/read-model;
- durable emission port tied to DecisionRecord finalization;
- `KonnaxionExport v1`;
- ArtifactRef support;
- RuntimePackActivationPort delegation (kOA-Linux owns host activation when present).

The reference compatibility adapter is in [`adapters/konnaxion-python/`](../../adapters/konnaxion-python/).
