# IK Core Protocol

## Semantic classes

IK Core définit exactement trois classes métier.

| Class | Meaning | Mutation distante |
|---|---|---|
| `command` | demande au receiver d’évaluer puis éventuellement muter son état | possible après admission/authorization |
| `query` | demande de lecture/projection | non par sémantique de la Query |
| `event` | annonce d’un fait déjà commis par le publisher | le consumer peut réagir localement |

### Command

Une Command exprime une **intention**. Elle ne prouve ni l’autorité, ni l’acceptation, ni l’exécution.

### Query

Une Query demande une projection. Elle ne doit pas être transformée en Event simplement pour obtenir une réponse.

### Event

Un Event décrit un fait déjà commis. Il ne doit pas être utilisé comme une Command déguisée.

## Protocol records

### Receipt

Un `Receipt` représente la disposition d’une Interaction :

```yaml
receipt:
  interaction_id: "01J..."
  status: "accepted" # accepted | rejected | blocked | succeeded | failed
  code: null
  retryable: false
  external_reference: null
  data: {}
```

`accepted` n’est pas nécessairement terminal.

### QueryResult

Un `QueryResult` répond à une Query. Il représente une projection, pas un Domain Event.

## Boundary objects

IK 1.1 définit deux objets de frontière :

- `ArtifactRef`
- `ExportManifest`

Il **ne définit pas** de record `ArtifactOutcome` séparé. Une Command de build utilise un Receipt pour sa disposition, puis un Event métier comme `kristal.artifact.ready` pour annoncer un résultat réutilisable.

## Core admission rule

Le Core reste volontairement petit.

`IK-CORE-001` — **SHOULD** : une nouvelle notion ne doit entrer dans IK Core que si elle est nécessaire à l’interopérabilité de plusieurs systèmes et ne peut pas être exprimée par Profile, binding, adapter ou module optionnel.
