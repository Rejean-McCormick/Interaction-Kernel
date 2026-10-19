# Interaction Kernel — Tour 4/8 (P1) — adopted contracts

**Cible :** `C:\mycode\Interaction-Kernel\interaction_kernel` (racine véritable du dépôt du snapshot).

Cette mise à jour **ne change pas** la version `ik/1.1` ni le runtime `2.0.0-dev.2`. Elle verrouille les trois profils Konnaxion/Orgo déjà adoptés (6 fichiers existants) et empêche l'activation implicite, dans le registre Python, des 3 versions historiques Kristal `1.0.0`. Les versions Kristal `2.0.0` actives restent fonctionnelles. Tests Python, Node, TypeScript et empreintes.

## PowerShell 7

Extraire le ZIP **dans la racine du dépôt**, puis :

```powershell
cd 'C:\mycode\Interaction-Kernel\interaction_kernel'
.\PREVIEW_IK_TOUR_P1.cmd
.\INSTALL_IK_TOUR_P1.cmd
.\VERIFY_IK_TOUR_P1.cmd
```

Retour arrière, seulement si nécessaire : `.\ROLLBACK_IK_TOUR_P1.cmd`.

L'installateur vérifie les empreintes d'origine et de livraison, teste une **copie isolée**, garde une sauvegarde hors dépôt sous `C:\mycode\Interaction-Kernel\Tandem_Local\interaction_kernel_tour_p1\backups`, accepte les relances sans double écriture et refuse toute dérive locale. Il n'installe pas de dépendances et n'effectue aucune connexion réseau, aucun Docker, aucune migration ni publication IK.

Si `jsonschema`, Node.js ou TypeScript n'est pas installé sur la machine Windows, les tests correspondants indiquent **ATTENTE** plutôt que de simuler une réussite complète. Le contrôle d'empreintes sans dépendances est toujours exécuté.

**Limites :** il ne valide pas le runtime réel de Konnaxion ou Orgo, l'isolation intertenant, la persistance d'idempotence, l'authentification de service, Konfid, ni un E2E actif. Notre test FakePlant E2E précédent est conservé tel quel.
