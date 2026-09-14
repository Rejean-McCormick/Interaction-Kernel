# Identity, trust, authority, security and privacy

## Separation of concerns

| Concept | Question |
|---|---|
| Identity | Qui envoie/agît ? |
| Authentication | Peut-il prouver cette identité ? |
| Trust | Cette identité est-elle reconnue ici ? |
| Authority claim | Quel droit est revendiqué ? |
| Policy / admission | Le receiver autorise-t-il cette action maintenant ? |
| Ownership | Qui peut muter la source autoritaire ? |
| Kristal authority recognition | Quelle autorité épistémique reconnaît une assertion/artefact ? |

## Receiver-owned admission

Le sender transporte des claims. Le receiver :

1. authentifie;
2. résout trust/context;
3. valide protocol/Profile/schema;
4. évalue authority/policy;
5. déduplique;
6. accepte/rejette/bloque;
7. appelle ses propres services de domaine.

Un `authority.kind=governance-mandate` n’accorde jamais automatiquement le droit de muter.

## Kristal separation

Deux séparations sont normatives :

- **IK Admission ≠ Kristal Validation**
- **IK Authority Claim ≠ Kristal Authority Recognition**

Da’at doit préserver ces distinctions.

## Transport authentication

Les bearer tokens existants peuvent rester pendant la migration. Ils peuvent être remplacés par mTLS/workload identity sans changer la sémantique IK.

Secrets, trust roots et route allowlists restent locaux au déploiement.

## Privacy

Le Profile doit définir la minimisation applicable. Une règle métier existante, comme le rejet de champs student/private dans le bridge d’impact Konnaxion, doit rester une policy spécifique au use case et ne pas devenir une blacklist universelle IK.

## Fail-closed

Une incertitude sur :

- protocol/Profile compatibility;
- schema;
- trust;
- authority;
- artifact integrity requise;

ne doit pas produire une mutation autoritaire optimiste.
