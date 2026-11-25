---
id: ransomware-needs-an-offline-copy-and-a-restore-test
title: Ransomware needs an offline copy and a restore test
tags: ir, ransomware, backup
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-ransomware.md
status: active
---
# Ransomware needs an offline copy and a restore test

## Claim

A backup reachable with the production credentials is encrypted with it. The copy must be offline or immutable and restored before.

## Test

Map the backup path and the credential. Try to delete a snapshot as the production role. Restore one file.

## Proof

A restore succeeds after the production credential is assumed compromised.

## Failure modes

An air gap can still share the same identity. A restore test can be stale.
