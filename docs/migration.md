# Migration

1. D0 — lock Core/Profile contracts and TCK.
2. D1 — wrap existing Orgo→Konnaxion bridge under `accountability.impact.publish` without behavior change.
3. D2 — implement immutable Konnaxion DecisionRecord handoff → Orgo Signal/workflow.
4. D3 — add ArtifactRef/ExportManifest and source-owned exports.
5. D4 — **completed in this snapshot:** migrate Da’at/IK from Kristal v5 RC assumptions to Kristal Standard v6.0.0 and Profile v2 surfaces.
6. D5 — reuse/upgrade Orgo BuildRecord/ReleaseRecord semantics.
7. D6 — route Runtime Pack activation through the single deployment activation owner.
8. D7 — deprecate bespoke paths only after conformance, observability and redrive validation.

The v6 migration changes knowledge semantics, not operational ownership: actionability in a Kristal artifact never bypasses the target system's authority/admission contract.
