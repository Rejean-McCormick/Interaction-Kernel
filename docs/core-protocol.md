# Core protocol

Business classes are only `command`, `query`, and `event`.

- **Command**: asks a receiver to evaluate and possibly mutate receiver-owned state.
- **Query**: asks for a projection/read.
- **Event**: announces a fact already committed by the publisher.

Protocol records are `Receipt` and `QueryResult`. `accepted` does not mean `succeeded`.

Boundary value objects are `ArtifactRef` and `ExportManifest`. There is no separate `ArtifactOutcome`; artifact results are expressed by Receipt + Event + ArtifactRef.
