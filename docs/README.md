# Interaction Kernel technical documentation

1. [Architecture](architecture.md)
2. [Core protocol](core-protocol.md)
3. [Envelope](envelope.md)
4. [Profiles](profiles.md)
5. [Artifact interchange](artifact-interchange.md)
6. [Reliability](reliability.md)
7. [Security and authority](security-authority.md)
8. [Kristal / DaaT](kristal-daat.md)
9. [Conformance](conformance.md)
10. [Migration](migration.md)
11. [Upgrade Konnaxion](upgrades/konnaxion.md)
12. [Upgrade Orgo](upgrades/orgo.md)
13. [Upgrade Kristal/DaaT](upgrades/kristal-daat.md)
14. [Kristal publication to UCKK](uckk-kristal-publication.md)
15. [Accepted ADRs](adrs/README.md)
16. [Normative requirements](reference/normative-requirements.md)

The cross-system state/artifact boundary is normative: participant operational state remains participant-owned; IK carries commands, queries, events and artifact references; DaaT is the narrow contract-mapping boundary to Kristal/Kristall. See [ADR-IK-05](adrs/ADR-IK-05-operational-state-artifact-boundary.md) and [ADR-IK-07](adrs/ADR-IK-07-daat-kristal-v7-boundary.md).

