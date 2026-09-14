# ADR-IK-01 — Runtime Pack activation owner

- **Status:** Proposed
- **Scope:** Konnaxion / kOA-Linux / Kristal distribution

## Context

Le contrat Kristal v5 cible Konnaxion pour distribution/activation, tandis que la documentation d’architecture Konnaxion actuelle réserve l’activation locale du Runtime Pack à kOA-Linux lorsqu’il héberge la plateforme.

Un double owner créerait deux activation states autoritaires et des conflits de rollback/revocation.

## Options

### A — Standalone Konnaxion owns activation

Konnaxion vérifie puis active le Runtime Pack localement.

### B — kOA-Linux owns host activation

Konnaxion vérifie/autorise au niveau applicatif puis délègue l’activation host via `RuntimePackActivationPort` à kOA-Linux.

## Required decision

Le deployment profile doit sélectionner exactement **un** owner d’activation.

## Acceptance gate

- un seul activation state autoritaire;
- rollback/revocation ont le même owner;
- Events indiquent l’owner réel;
- Konnaxion ne prétend pas posséder l’activation host si elle est déléguée.
