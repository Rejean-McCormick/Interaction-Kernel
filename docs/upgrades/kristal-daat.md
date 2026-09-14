# Kristal / Da’at upgrade

Do not add IK fields to Kristal core schemas.

Upgrade Da’at/kOA integration from v4-centric assumptions to the pinned v5 release candidate. Replace global `no compile on fail` with stage-specific gates: Working Exchange compilation may precede final validation/recognition when the Profile permits; Reference/release/distribution remain fail-closed according to policy.

Da’at is responsible for pin verification, versioned mapping profiles, native Kristal invocation, output validation and IK artifact handoff.
