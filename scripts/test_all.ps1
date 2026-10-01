$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root
$env:PYTHONPATH = "runtime/python/src"
python scripts/validate_repo.py
python scripts/verify_kristal_lock.py
if (Test-Path '/mnt/data/ik_build/src/konnaxion/backend/konnaxion/ethikos/orgo_bridge_contract.py') {
  python scripts/test_konnaxion_legacy_compat.py
} else {
  Write-Host 'Konnaxion legacy compatibility: SKIP (external snapshot not mounted)'
}
python -m unittest discover -s runtime/python/tests -v
Push-Location runtime/typescript
npm run build
npm test
Pop-Location
tsc --noEmit --strict --target ES2023 --module NodeNext --moduleResolution NodeNext adapters/orgo-typescript/orgo-ik-adapter.ts runtime/typescript/src/types.ts
python scripts/check_links.py
Write-Host "Interaction Kernel validation: PASS"
