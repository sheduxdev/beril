---
id: ransomware-is-a-key-and-a-deletion-race
title: Ransomware is a key and a deletion race
tags: malware, ransomware, recovery
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-ransomware.md
status: active
---
# Ransomware is a key and a deletion race

## Claim

The encryption key, the shadow copy deletion and the backup reach decide whether recovery is possible.

## Test

Read the key material and the deletion commands. Check the shadow copies and the backup path. Restore one file.

## Proof

A restore attempt and the key state.

## Failure modes

A stolen key can leak later. A partial encryption can leave a restore point.
