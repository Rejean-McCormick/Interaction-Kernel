# ADR-IK-04 — Canonical IK-Reliable fingerprint

- **Status:** Proposed
- **Scope:** IK-Reliable Python / TypeScript

## Context

Même idempotency identity + contenu sémantique divergent doit produire un conflit. Le fingerprint doit donc être identique entre runtimes malgré :

- sérialisation JSON différente;
- ordre de clés;
- timestamps différents;
- traces différentes;
- représentation Python/TypeScript.

## Semantic input

Le fingerprint couvre au minimum :

```text
class
profile
target
subject
authority
data
artifact_refs
```

Il exclut les champs volatils :

```text
time
trace
transport headers
retry metadata
```

## Decision required

Figer :

1. canonical JSON representation;
2. normalization rules;
3. hash algorithm;
4. null/absent semantics;
5. ordering rules pour arrays lorsque la sémantique le permet;
6. golden vectors communs.

## Acceptance gate

Les runtimes Python et TypeScript produisent le même fingerprint pour tous les golden vectors TCK.
