# Glossary

| Term | Definition |
|---|---|
| Interaction | record métier IK de classe Command, Query ou Event |
| Command | intention adressée à un receiver; peut mener à mutation receiver-owned |
| Query | demande de projection/lecture |
| Event | fait déjà commis chez le publisher |
| Receipt | disposition protocolaire liée à une Interaction |
| QueryResult | réponse à une Query, pas un Domain Event |
| Profile | contrat use-case versionné spécialisant IK Core |
| Capability | description control-plane de ce qu’un participant sait accepter/produire |
| ArtifactRef | référence vérifiable vers un artefact possédé ailleurs |
| ExportManifest | snapshot/export source-owned destiné à consommation externe |
| Participant | système autonome qui parle IK |
| Owner | système qui possède l’état autoritaire concerné |
| Adapter / ACL | Anti-Corruption Layer entre IK et un bounded context local |
| Da’at | participant/gateway IK et ACL vers Kristal v5 dans la baseline |
| Kristal | knowledge/epistemic system; non participant IK direct dans la baseline |
| Admission | validation/authorization/dedup d’une Interaction au receiver |
| Kristal Validation | validation épistémique Kristal; distincte de l’admission IK |
| Authority claim | droit revendiqué par une Interaction |
| Authority Recognition | reconnaissance épistémique Kristal; distincte de l’autorisation IK |
| Correlation | conversation/processus métier partagé |
| Causation | lien direct de cause entre interactions |
| Trace | contexte technique d’observabilité |
| Idempotency identity | identité stable d’un effet logique pour replay/retry |
| Redrive | reprise explicite d’une interaction existante avec même identité logique |
| World / Release | contexte de déploiement/version possédé par les Worlds Konnaxion/Orgo |
| RuntimePackActivationPort | frontière abstraite vers l’owner réel de l’activation Runtime Pack |
