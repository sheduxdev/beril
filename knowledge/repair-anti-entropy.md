---
id: repair-anti-entropy
title: Anti-entropy compares digests and repairs the delta
tags: distributed-storage, repair, merkle
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Anti-entropy compares digests and repairs the delta

## Claim

Merkle trees summarize ranges. A mismatch descends to the leaf and the missing key is repaired.

## Test

Compare two replica trees. Corrupt one range. Watch the repair scope.

## Proof

A repaired range without a full scan.

## Failure modes

A digest collision hides a mismatch. A full-tree build is expensive.
