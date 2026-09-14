# Kristal and Da’at

Baseline: Da’at is the IK participant in front of Kristal. Kristal does not parse IK Envelopes.

Pinned release:

- version `5.0.0-rc.1`
- tag `v5.0.0-rc.1`
- commit `af703bf02ee04a69a5f2ad6694fa8b8e56ae2b19`
- canonicalization `kristal.v5:jcs-rfc8785`
- schema-set digest `sha256:7a94a1e8a91d5c5267b73b7f1e98977faa548324bc937bb491cd08d49fdc8c92`

Da’at applies explicit versioned mappings from Konnaxion/Orgo ExportManifests to Kristal-native inputs, invokes Kristal-native contracts, validates outputs, then emits IK Receipts/Events with Kristal-owned ArtifactRefs.
