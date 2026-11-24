---
id: key-management
title: Key management is where crypto bugs become data bugs
tags: crypto, keys, storage
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Key management is where crypto bugs become data bugs

## Claim

Keys are in source, in env, in a world-readable file, or reused across environments. Rotation is manual or absent.

## Test

Find every key path. Check file permissions, env exposure and git history. Test a rotated key.

## Proof

A key readable by a lower-privilege principal, or an old key still valid.

## Failure modes

A public key is not a secret. A key in a secret manager with narrow access is the goal.
