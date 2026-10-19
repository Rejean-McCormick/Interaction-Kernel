# Tandem Konnaxion–Orgo — adopted IK contract gate

**Tour 4/8, 2026-10-19.** This is a read-only, repository-level conformance gate, **not** a production/runtime qualification. It does not publish interactions, touch tenant data, change a Profile version, or admit a live service.

## Adopted interfaces (unchanged)

| Profile | Version | Publisher → receiver | Purpose |
|---|---|---|---|
| `governance.decision.execute` | `1.0.0` | Konnaxion → Orgo | Governed execution |
| `accountability.impact.publish` | `1.0.0` | Orgo → Konnaxion | Aggregate impact publication |
| `operational.reconsideration.recommended` | `1.0.0` | Orgo → Konnaxion | Non-authoritative reconsideration event |

The first two are the Profile versions exercised by the local FakePlant IK E2E. The E2E `complete=true` is an externally recorded test outcome; this repository check **does not** reproduce or re-certify that running E2E.

- `contracts/profiles/index.json` is the active Profile index.
- `contracts/locks/konnaxion-orgo-adopted-v1.lock.json` pins the **raw file SHA-256** of the three descriptors and their payload schemas. These SHA-256 values detect unintentional local drift; **they are not signatures or a trusted release authorization**.
- `ProfileRegistry.from_contracts()` now registers only active indexed Profiles. In particular, historical Kristal `1.0.0` build/artifact/revision folders remain available for explicit migration inspection via `register_directory()` but are **not active by default**. Active portable Kristal profiles remain `2.0.0`.
- A new release changing any adopted Profile or schema MUST create a new version/lock through owner review, rather than silently rewriting these `1.0.0` files.

## Run locally, without databases or Docker

```powershell
cd 'C:\mycode\Interaction-Kernel\interaction_kernel'
python scripts/validate_repo.py
python scripts/verify_tandem_contract_lock.py
$env:PYTHONPATH='runtime/python/src'
python -m unittest discover -s runtime/python/tests -v
# TypeScript checks if Node.js and the repository's TypeScript compiler are installed:
Push-Location runtime/typescript
npm run build
npm test
npm run typecheck:adapter
Pop-Location
```

On CI, `scripts/test_all.ps1` and `scripts/test_all.sh` include the new lock gate. The TypeScript conformance suite independently checks the adopted hashes with Node.js, in addition to RFC 8785 JCS and semantic fingerprint vectors. The IK wire version is still `ik/1.1`, and the reference runtime remains `2.0.0-dev.2`; no protocol/version bump was made.

## Still open for Tandem 1.0 GA

The gate only validates repository contracts and reference runtimes. The receiving applications still have to prove authenticated tenant/World isolation, verified authorizations, durable idempotency under concurrency, outbox/retry/reconciliation, live Konnaxion/Orgo E2E, and deployment admission independently. No new service/actor credentials or shared databases are created by this gate.
