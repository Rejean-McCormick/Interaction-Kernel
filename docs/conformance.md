# Conformance

Claims:

- `IK-Core/1.1`
- `IK-Reliable/1`
- `IK-HTTP/1` (optional binding)
- `IK-Artifact/1`
- `IK-Kristal/1`
- `IK-KX-ORGO/1`

The TCK contains the 9 pinned Kristal RFC 8785 JCS vectors and IK request-fingerprint vectors shared by Python and TypeScript runtimes.

Scenario fixtures such as UCKK-A014 are end-to-end conformance tests, not definitions of Core.

## Tandem Konnaxion–Orgo

The active versions of the three Konnaxion–Orgo Profiles are pinned with file digests and checked across Python and TypeScript. See [Tandem contract gate](tandem-konnaxion-orgo-conformance.md). This is a repository gate, not a live qualification.
