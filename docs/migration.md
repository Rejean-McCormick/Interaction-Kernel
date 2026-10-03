# Migration

1. D0 — lock Core/Profile contracts and TCK.
2. D1 — wrap existing Orgo→Konnaxion bridge under `accountability.impact.publish` without behavior change.
3. D2 — implement immutable Konnaxion DecisionRecord handoff → Orgo Signal/workflow.
4. D3 — add ArtifactRef/ExportManifest and source-owned exports.
5. D4 — **completed:** migrate DaaT/IK from Kristal v5 RC assumptions to Kristal Standard v6.0.0 and Profile v2 portable surfaces.
6. D4.1 — **completed in this snapshot:** normalize the human name to DaaT (`daat` machine id), narrow DaaT to the IK↔Kristal contract boundary, and pin Kristal `7.0.0-draft.3.1` as an additive design baseline while retaining v6 portable compatibility.
7. D5 — reuse/upgrade Orgo BuildRecord/ReleaseRecord semantics.
8. D6 — route Runtime Pack activation through the single deployment activation owner.
9. D7 — deprecate bespoke paths only after conformance, observability and redrive validation.

The v6 migration changes knowledge semantics, not operational ownership: actionability in a Kristal artifact never bypasses the target system's authority/admission contract.
