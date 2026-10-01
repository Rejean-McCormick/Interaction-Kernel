from __future__ import annotations
import json, pathlib, sys
from jsonschema import Draft202012Validator
ROOT=pathlib.Path(__file__).resolve().parents[1]
errors=[]
for path in sorted((ROOT/'contracts/schemas').glob('*.json')):
    try: Draft202012Validator.check_schema(json.loads(path.read_text(encoding='utf-8')))
    except Exception as e: errors.append(f'{path}: {e}')
for path in sorted((ROOT/'contracts/profiles').glob('*/*/*/profile.json')):
    try:
        value=json.loads(path.read_text(encoding='utf-8'))
        schema=json.loads((ROOT/'contracts/schemas/profile.schema.json').read_text(encoding='utf-8'))
        Draft202012Validator(schema).validate(value)
        payload=path.parent/value['payload_schema']
        Draft202012Validator.check_schema(json.loads(payload.read_text(encoding='utf-8')))
    except Exception as e: errors.append(f'{path}: {e}')
lock=json.loads((ROOT/'locks/kristal-v6.0.0.lock.json').read_text())
if lock.get('format')!='kristal.consumer-lock/v2': errors.append('Kristal lock format mismatch')
if lock.get('version')!='6.0.0': errors.append('Kristal version mismatch')
if lock.get('canonicalization_profile')!='kristal.v6:jcs-rfc8785': errors.append('Kristal canonicalization profile mismatch')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('repository contracts: PASS')
