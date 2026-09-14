# ADR-IK-02 — Exact Kristal v5 pin

- **Status:** Proposed
- **Scope:** Da’at / kOA / IK-Kristal

## Context

Le repository fourni est Kristal v5, mais les contrats/core sont encore marqués Draft et la documentation kOA pointe vers `kristal-v4`.

## Decision required

Da’at/kOA doivent pinner un ensemble immuable :

- Kristal repository commit/digest;
- core spec version;
- schema set;
- integration contract versions;
- golden vectors;
- security/profile artifacts nécessaires.

## Non-goal

Aucune référence `latest`, branche flottante ou chemin v5 non versionné dans une release de production.

## Acceptance gate

Un bundle/pin exact peut être vérifié offline et produit la même conformance surface sur tous les nodes.
