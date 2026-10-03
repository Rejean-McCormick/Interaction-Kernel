# v7 / v6 compatibility contract

A v7 implementation MUST accept valid v6 `kristal_state` unchanged and MUST NOT redefine v6 fields. Generated portable projections SHOULD remain `schema_version: 6.0`, `artifact_type: kristal_state`, with lineage under `extensions.kristal_v7`.
