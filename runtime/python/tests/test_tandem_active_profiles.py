"""Regression tests for the adopted IK contract and active-profile boundary."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest

from _paths import CONTRACTS, TCK
from interaction_kernel.errors import IKError
from interaction_kernel.profile_registry import ProfileRegistry
from interaction_kernel.validator import ContractValidator


class TandemActiveProfileTests(unittest.TestCase):
    def test_all_three_adopted_tandem_profiles_active(self):
        registry = ProfileRegistry.from_contracts(CONTRACTS)
        for profile in (
            'governance.decision.execute',
            'accountability.impact.publish',
            'operational.reconsideration.recommended',
        ):
            self.assertIsNotNone(registry.get(profile, '1.0.0'))

    def test_legacy_kristal_profiles_are_not_auto_admitted(self):
        registry = ProfileRegistry.from_contracts(CONTRACTS)
        for profile in ('kristal.build.request', 'kristal.artifact.ready', 'kristal.revision.request'):
            with self.assertRaises(IKError) as ctx:
                registry.get(profile, '1.0.0')
            self.assertEqual(ctx.exception.code, 'IK_UNKNOWN_PROFILE')
            self.assertIsNotNone(registry.get(profile, '2.0.0'))

    def test_unknown_adopted_version_fail_closed(self):
        registry = ProfileRegistry.from_contracts(CONTRACTS)
        with self.assertRaises(IKError):
            registry.get('governance.decision.execute', '1.0.1')

    def test_index_duplicate_and_class_drift_fail_closed(self):
        index = json.loads((CONTRACTS/'profiles/index.json').read_text(encoding='utf-8'))
        # Use an isolated contracts copy so this test never changes the source tree.
        import shutil
        for edit in ('duplicate', 'class'):
            with self.subTest(edit=edit), tempfile.TemporaryDirectory() as tmp:
                test_root = Path(tmp)/'contracts'
                shutil.copytree(CONTRACTS/'profiles', test_root/'profiles')
                modified = copy.deepcopy(index)
                if edit == 'duplicate':
                    modified['profiles'].append(copy.deepcopy(modified['profiles'][0]))
                else:
                    modified['profiles'][0]['class'] = 'query'
                (test_root/'profiles/index.json').write_text(json.dumps(modified), encoding='utf-8')
                with self.assertRaises(IKError):
                    ProfileRegistry.from_contracts(test_root)

    def test_contract_lock_detects_mutated_payload(self):
        import runpy
        import shutil
        verifier = runpy.run_path(str(CONTRACTS.parent / 'scripts/verify_tandem_contract_lock.py'))['verify']
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(CONTRACTS/'profiles', root/'contracts/profiles')
            shutil.copytree(CONTRACTS/'locks', root/'contracts/locks')
            candidate = root/'contracts/profiles/konnaxion-orgo/governance.decision.execute/1.0.0/payload.schema.json'
            candidate.write_bytes(candidate.read_bytes() + b'\n')
            with self.assertRaisesRegex(ValueError, 'digest mismatch'):
                verifier(root)

    def test_adopted_tandem_payloads_remain_valid(self):
        validator = ContractValidator(CONTRACTS)
        vectors = json.loads((TCK/'fingerprint/vectors.json').read_text(encoding='utf-8'))['vectors']
        for vector in vectors[:2]:  # The third TCK vector deliberately exercises non-profile payload values.
            validator.validate_envelope(vector['envelope'])


if __name__ == '__main__':
    unittest.main()
