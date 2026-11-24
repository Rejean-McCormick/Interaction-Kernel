<!-- kOA Doc Server · Docs IA · lot 02 · rédaction dérivée d’une capture, à valider par le propriétaire -->
# Navigation IA — interaction_kernel

**Rôle observé :** Protocoles et implémentations de référence pour échanges typés entre produits autonomes.

**Autorité :** Chaque produit conserve son état opérationnel; IK définit enveloppes, profils et empreintes de requêtes.

**Provenance :** `SmartDump_20261120_221507.zip` → `interaction_kernel_Code_snapshot.zip` (20 novembre 2026). Cette capture ne prouve ni la présence actuelle du dossier Windows, ni un déploiement, ni une qualification.

## Objet et état de cette fiche

La description ci-dessous est rattachée au `README.md` du snapshot; vérifier le code actif sur le poste. Cette fiche est un **guide de navigation**, non une spécification normative ni une validation de maturité.

## Processus conseillé

1. **Identifier la source et le profil.** Lire schémas et ADR, épingler les profils adoptés, exercer les vecteurs TCK/golden pour les runtimes.
2. **Contrôler l’autorité.** Chaque produit conserve son état opérationnel; IK définit enveloppes, profils et empreintes de requêtes.
3. **Préparer un environnement de test.** Utiliser les fichiers réels de la révision étudiée et des données fictives ou autorisées.
4. **Vérifier sans promouvoir.** Documenter commandes, périmètre, résultat, chemins et empreintes; ne jamais transformer une observation locale en preuve historique validée.
5. **Revue propriétaire.** Une publication, activation, import ou effet externe nécessite l’accord du propriétaire et les gates correspondants.

## Garde-fous particuliers

- La conformité des enveloppes ne vaut pas autorisation métier ni transaction distribuée.
- N’inclure aucun secret, donnée personnelle, sauvegarde privée ou sortie de diagnostic non autorisée dans les exports Doc Server.
- Préserver l’intégrité des sources et des états historiques; éviter toute réécriture automatique des références.

## Sources d’orientation vérifiables dans le snapshot

1. [`README.md`](../../README.md) — source propriétaire présente dans le snapshot.
2. [`docs/README.md`](../../docs/README.md) — source propriétaire présente dans le snapshot.
3. [`docs/adrs/README.md`](../../docs/adrs/README.md) — source propriétaire présente dans le snapshot.
4. [`docs/architecture.md`](../../docs/architecture.md) — source propriétaire présente dans le snapshot.
5. [`docs/security-authority.md`](../../docs/security-authority.md) — source propriétaire présente dans le snapshot.
6. [`docs/adrs/ADR-IK-01-runtime-pack-activation-owner.md`](../../docs/adrs/ADR-IK-01-runtime-pack-activation-owner.md) — source propriétaire présente dans le snapshot.
7. [`docs/adrs/ADR-IK-02-kristal-pin.md`](../../docs/adrs/ADR-IK-02-kristal-pin.md) — source propriétaire présente dans le snapshot.
8. [`docs/adrs/ADR-IK-03-decision-record.md`](../../docs/adrs/ADR-IK-03-decision-record.md) — source propriétaire présente dans le snapshot.

## Compatibilité Framework

S’il y a une dépendance Kristal, lire la révision du Framework et le profil **effectivement adoptés** par ce dépôt. Les nouvelles conventions v11 (identités sémantiques, dictionnaires séparés, provenance) servent de référence lorsque compatibles; **ne pas bloquer** la navigation IA ni imposer la migration de données historiques pour cette seule raison.
