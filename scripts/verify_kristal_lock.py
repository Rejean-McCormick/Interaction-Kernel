from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
lock=json.loads((ROOT/'locks/kristal-v6.0.0.lock.json').read_text())
up=ROOT/'locks/kristal-v6.0.0-upstream'

def digest(path: Path) -> str:
    return 'sha256:' + hashlib.sha256(path.read_bytes()).hexdigest()

assert lock['format']=='kristal.consumer-lock/v2'
assert lock['version']=='6.0.0'
assert lock['canonicalization_profile']=='kristal.v6:jcs-rfc8785'
assert lock['canonicalization_version']=='1'
assert lock['standard_manifest_sha256']==digest(up/'manifest.sha256.json')
assert lock['contract_digests']['schemas/kristal-state.schema.json']==digest(up/'schemas/kristal-state.schema.json')
assert lock['contract_digests']['schemas/reader-policy.schema.json']==digest(up/'schemas/reader-policy.schema.json')
manifest=json.loads((up/'manifest.sha256.json').read_text())
assert manifest['standard_version']=='6.0.0'
assert manifest['files']['schemas/kristal-state.schema.json']==lock['contract_digests']['schemas/kristal-state.schema.json'].split(':',1)[1]
assert manifest['files']['schemas/reader-policy.schema.json']==lock['contract_digests']['schemas/reader-policy.schema.json'].split(':',1)[1]
print('Kristal v6 dependency lock: PASS')
