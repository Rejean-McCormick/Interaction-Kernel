$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root
$env:PYTHONPATH = "runtime/python/src"
python scripts/validate_repo.py
python scripts/verify_kristal_lock.py
python scripts/verify_kristal_v7_baseline.py
if (Test-Path '/mnt/data/ik_build/src/konnaxion/backend/konnaxion/ethikos/orgo_bridge_contract.py') {
  python scripts/test_konnaxion_legacy_compat.py
} else {
  Write-Host 'Konnaxion legacy compatibility: SKIP (external snapshot not mounted)'
}
python -m unittest discover -s runtime/python/tests -v
Push-Location runtime/typescript
npm run build
npm test
npm run typecheck:adapter
Pop-Location
python scripts/check_links.py
Write-Host "Interaction Kernel validation: PASS"
