# Artifact Interchange

`ArtifactRef` references an owner-defined artifact identity, optional SHA-256 integrity digest, opaque locator and contract metadata. It never transfers ownership.

`ExportManifest` is source-owned and pins snapshots/revisions/digests for reproducible external consumption.

Locators must not embed credentials. IK is not an artifact store.
