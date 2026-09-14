# Contributing to Interaction Kernel

Interaction Kernel est une **specification-first architecture**. Les changements sont acceptés selon leur niveau de responsabilité.

## 1. Choisir le bon niveau de changement

Avant d’ajouter une notion au Core, vérifier si elle peut vivre dans :

1. un **Profile** — sémantique use-case;
2. un **binding** — HTTP, messaging, offline;
3. un **adapter** — traduction participant/domain;
4. un **module optionnel** — Reliable, Artifact, Kristal;
5. le **Core** seulement si l’interopérabilité multi-systèmes l’exige réellement.

> Une notion ne doit entrer dans IK Core que si elle est nécessaire à plusieurs systèmes et impossible à exprimer proprement ailleurs.

## 2. Normative changes

Toute nouvelle règle normative doit :

- utiliser `MUST`, `MUST NOT`, `SHOULD`, `MAY` de façon explicite;
- recevoir un identifiant stable `IK-<AREA>-NNN`;
- préciser le module de conformité concerné;
- avoir au moins un test TCK positif et un test négatif lorsque testable;
- ne pas modifier rétroactivement une version publiée de Profile/schema.

## 3. Ownership changes

Toute proposition qui change l’owner d’un état autoritaire exige une ADR. Sont notamment interdits sans ADR :

- déplacer un lifecycle Orgo dans IK;
- faire de Da’at l’owner d’un artifact Kristal;
- faire de Kristal l’owner d’un état Konnaxion/Orgo;
- dupliquer l’état d’activation Runtime Pack;
- ajouter une base IK centrale qui deviendrait source de vérité.

## 4. Source status labels

Utiliser ces labels dans les docs d’upgrade :

- **CURRENT** — vérifié dans code/migrations/tests du snapshot;
- **TARGET** — contrat/architecture cible déjà documenté par l’owner;
- **IK PROPOSAL** — nouveau choix introduit par IK.

Ne jamais présenter un `TARGET` comme un état implémenté.

## 5. Profiles

Un Profile doit être :

- petit;
- versionné;
- orienté use-case;
- indépendant des tables internes;
- explicite sur authority, artifacts, durability, receipts et outcomes;
- lié à un schema de payload déterminé.

## 6. Compatibility

- Un Profile/schema publié est immuable.
- Breaking change → nouvelle version majeure.
- Incompatibilité connue → rejet explicite.
- Aucun best-effort silencieux.

## 7. Pull request checklist

- [ ] Le changement respecte l’ownership existant.
- [ ] Le Core n’est pas enrichi inutilement.
- [ ] Les docs CURRENT/TARGET/IK PROPOSAL sont exactes.
- [ ] Les Profiles/schemas impactés sont versionnés.
- [ ] Les TCK/fixtures sont ajoutés ou mis à jour.
- [ ] Aucun secret/trust root de production n’est commité.
- [ ] Les ADRs impactées sont mises à jour.
