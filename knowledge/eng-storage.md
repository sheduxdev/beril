---
id: eng-storage
title: Storage engines trade read cost for write cost
tags: engineering, database, storage
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Storage engines trade read cost for write cost

## Claim

B-trees optimize reads with in-place pages. LSM trees optimize writes with sorted runs and compaction.

## Test

Read the engine docs. Measure write amplification and read latency under load.

## Proof

A workload fit that names the amplification.

## Failure modes

An LSM with heavy compaction can stall reads. A B-tree random write can fragment.
