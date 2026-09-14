# Architecture

IK is a distributed protocol, not a central server.

```text
Konnaxion  <---------- IK ----------> Orgo
    \                                /
     +----------- IK ----------> Da'at
                                   |
                           Kristal-native contracts
                                   |
                                Kristal
```

## Ownership

| Plane | Owner | Examples |
|---|---|---|
| civic/governance | Konnaxion | deliberation, DecisionRecord, impact/accountability |
| operational/work | Orgo | Signal, Workflow, Case, Task, IntegrationOperation |
| knowledge/epistemic | Kristal | Structured Epistemic State, Exchange, ValidationReport, AuthorityRecognition, Runtime Pack |
| Kristal boundary | Da’at | IK admission, mapping profile, Kristal pin, handoff |
| host activation | kOA-Linux when present | verify/stage/activate/rollback Runtime Pack |

Invariants: unique authoritative owner, no cross-system DB writes, Konnaxion↔Orgo direct by default, Kristal optional by Profile, delivery lifecycle separate from domain lifecycle.
