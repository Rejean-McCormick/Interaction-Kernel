# ADR-IK-03 — Konnaxion canonical handoff object

- **Status:** Proposed
- **Scope:** Konnaxion → Orgo

## Context

`DecisionRecord` est documenté dans la cible Kintsugi comme premier choix pour porter une décision finalisée, mais il n’est pas encore le modèle canonique implémenté dans le snapshot actuel.

IK ne doit pas émettre `governance.decision.execute` à partir d’un objet ambigu ou d’une projection non autoritaire.

## Decision required

Choisir et implémenter explicitement :

- `DecisionRecord`, **ou**
- un objet/service/event équivalent clairement désigné comme source canonique.

## Required properties

L’objet retenu doit fournir :

- business identity stable;
- finalization state explicite;
- revision/version;
- provenance/rationale refs nécessaires;
- event de finalisation transactionnel ou capturable;
- idempotency identity stable pour Orgo handoff.

## Acceptance gate

Aucun `governance.decision.execute` n’est produit tant que la source canonique n’est pas implémentée et testée.
