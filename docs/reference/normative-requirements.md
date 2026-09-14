# Normative requirements

- **IK-ARCH-001 MUST NOT** force Konnaxion↔Orgo through Kristal unless a Profile explicitly gates on Kristal.
- **IK-ARCH-002 MUST** use Da’at as baseline IK↔Kristal ACL.
- **IK-ARCH-003 MUST** preserve participant-owned authoritative state.
- **IK-ENV-001 MUST** resolve durable Command/Query to a concrete receiver.
- **IK-ART-001 MUST NOT** interpret ArtifactRef as ownership/authority/validation transfer.
- **IK-ART-003 MUST NOT** embed credentials in ArtifactRef locators.
- **IK-REL-001 MUST** preserve idempotency identity across retry/redrive.
- **IK-REL-002 MUST** reject divergent replays under the same idempotency key.
- **IK-REL-004 MUST** use deterministic cross-language semantic fingerprints.
- **IK-REL-005 MUST NOT** assume global ordering.
- **IK-VERS-001 MUST** keep published Profile/schema versions immutable.
- **IK-VERS-002 MUST** reject known incompatibility explicitly.
