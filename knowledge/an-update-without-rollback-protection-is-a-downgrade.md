---
id: an-update-without-rollback-protection-is-a-downgrade
title: An update without rollback protection is a downgrade
tags: firmware, update, rollback
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-update-sign.md
status: active
---
# An update without rollback protection is a downgrade

## Claim

A signed update that accepts an old version lets an attacker restore a version with a known bug.

## Test

Install the current version. Serve the previous signed image. Check the anti rollback counter and the accepted version.

## Proof

The old version installs.

## Failure modes

A monotonic counter blocks it. A recovery partition can be separate.
