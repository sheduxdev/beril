---
id: repair-quorum
title: Degraded mode trades consistency for availability
tags: distributed-storage, quorum, degraded
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Degraded mode trades consistency for availability

## Claim

With fewer than the required replicas the cluster can serve reads, reject writes, or accept weakened durability by policy.

## Test

Kill replicas below the write quorum. Read and write. Check the documented behavior.

## Proof

A documented degraded mode with a recovery path.

## Failure modes

A silent weakened write is data loss on the next failure. A read-only mode surprises writers.
