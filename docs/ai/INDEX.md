<!-- kOA Doc Server · Docs IA · lot 02 · rédaction dérivée d’une capture, à valider par le propriétaire -->
# Navigation IA — interaction_kernel

**Rôle observé :** Protocoles et implémentations de référence pour échanges typés entre produits autonomes.

**Autorité :** Chaque produit conserve son état opérationnel; IK définit enveloppes, profils et empreintes de requêtes.

**Provenance :** `SmartDump_20261120_221507.zip` → `interaction_kernel_Code_snapshot.zip` (20 novembre 2026). Cette capture ne prouve ni la présence actuelle du dossier Windows, ni un déploiement, ni une qualification.

## Ordre de lecture fondé sur les sources

1. [`README.md`](../../README.md) — source propriétaire présente dans le snapshot.
2. [`docs/README.md`](../../docs/README.md) — source propriétaire présente dans le snapshot.
3. [`docs/adrs/README.md`](../../docs/adrs/README.md) — source propriétaire présente dans le snapshot.
4. [`docs/architecture.md`](../../docs/architecture.md) — source propriétaire présente dans le snapshot.
5. [`docs/security-authority.md`](../../docs/security-authority.md) — source propriétaire présente dans le snapshot.
6. [`docs/adrs/ADR-IK-01-runtime-pack-activation-owner.md`](../../docs/adrs/ADR-IK-01-runtime-pack-activation-owner.md) — source propriétaire présente dans le snapshot.
7. [`docs/adrs/ADR-IK-02-kristal-pin.md`](../../docs/adrs/ADR-IK-02-kristal-pin.md) — source propriétaire présente dans le snapshot.
8. [`docs/adrs/ADR-IK-03-decision-record.md`](../../docs/adrs/ADR-IK-03-decision-record.md) — source propriétaire présente dans le snapshot.

## Pour une intervention IA

1. Définir le changement envisagé et relire les documents propriétaires ci-dessus.
2. Lire schémas et ADR, épingler les profils adoptés, exercer les vecteurs TCK/golden pour les runtimes.
3. Identifier les tests de la révision locale et préserver les traces avant de proposer une modification.
4. Présenter les limites de couverture et demander l’accord du propriétaire avant une opération à effet.

## Limites à ne pas perdre

- La conformité des enveloppes ne vaut pas autorisation métier ni transaction distribuée.
- L’overlay ne certifie pas le produit et n’autorise pas une écriture distante.
- Les contrats et `AGENTS.md` propriétaires priment sur cet index dérivé.
- Le Framework Kristal v11 est une cible documentaire facultative; toute adoption exige un profil explicitement épinglé.

## Aides complémentaires

- [`AI_CONTEXT.md`](AI_CONTEXT.md) — workflow et frontières de confiance propres au dépôt.
- `PROFIL_INGENIERIE.md` — facultatif, mesuré par RepoSurveyor sur le checkout local avec confirmation.
