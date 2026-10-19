#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PYTHONPATH=runtime/python/src python scripts/validate_repo.py
PYTHONPATH=runtime/python/src python scripts/verify_kristal_lock.py
python scripts/verify_kristal_v7_baseline.py
python scripts/verify_tandem_contract_lock.py
if [[ -f /mnt/data/ik_build/src/konnaxion/backend/konnaxion/ethikos/orgo_bridge_contract.py ]]; then
  python scripts/test_konnaxion_legacy_compat.py
else
  echo 'Konnaxion legacy compatibility: SKIP (external snapshot not mounted)'
fi
PYTHONPATH=runtime/python/src python -m unittest discover -s runtime/python/tests -v
( cd runtime/typescript && npm run build && npm test && npm run typecheck:adapter )
python scripts/check_links.py
printf '\nInteraction Kernel validation: PASS\n'
