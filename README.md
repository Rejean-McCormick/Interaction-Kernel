# Interaction Kernel

Interaction Kernel (IK) is a distributed interoperability protocol and reference implementation for autonomous systems. It is not an operational database, artifact store or distributed transaction coordinator.

**Status:** `v2.0-draft` reference implementation.

The repository contains:

- normative JSON Schemas for IK records and artifact interchange;
- versioned Profile descriptors and payload schemas;
- Python and TypeScript runtimes;
- RFC 8785 JCS + SHA-256 semantic request fingerprinting;
- a reusable admission pipeline;
- TCK/golden vectors shared across runtimes;
- Konnaxion, Orgo, Da’at/Kristal and kOA-Linux reference adapters;
- a pinned Kristal Standard `6.0.0` dependency lock;
- GitHub-native technical documentation.

## Architecture

```text
Konnaxion  <----------- IK ----------->  Orgo
    \                                   /
     \                                 /
      +---------- IK ---------->  Da'at
                                      |
                              Kristal-native contracts
                                      |
                                   Kristal
```

Konnaxion↔Orgo remains direct. Kristal is not a mandatory relay. Da’at is the baseline IK participant in front of Kristal.

## Quick checks

### Python

```bash
cd runtime/python
PYTHONPATH=src python -m unittest discover -s tests -v
```

On PowerShell, use `$env:PYTHONPATH = "src"` before the test command, or run the repository-level `scripts/test_all.ps1`.

### TypeScript

```bash
cd runtime/typescript
npm run build
npm test
```

The TypeScript runtime intentionally has no runtime dependencies.

## Repository map

```text
contracts/      IK schemas, Profiles and payload schemas
locks/          immutable downstream dependency locks
runtime/        Python + TypeScript reference runtimes
adapters/       Konnaxion / Orgo / Da’at / kOA-Linux reference adapters
tck/            cross-language golden vectors
scripts/        validation utilities
docs/           technical documentation + ADRs
```

## Accepted architecture decisions

- Runtime Pack: Konnaxion selects/requests; local platform activation is executed by the configured `RuntimePackActivationPort` owner (kOA-Linux when present).
- Kristal pin: Standard `6.0.0`, canonicalization `kristal.v6:jcs-rfc8785`, pinned by manifest and core-contract digests.
- Konnaxion handoff: `DecisionRecord` is the canonical immutable handoff contract.
- Request fingerprint: semantic projection → RFC 8785 JCS → SHA-256.
- State/artifact boundary: each participant owns its mutable operational state; IK transports interactions and references; Da’at maps source-owned snapshots into Kristal-native artifacts; no distributed cross-owner database transaction is required.

See [`docs/`](docs/README.md).
