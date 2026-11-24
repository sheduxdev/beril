---
id: alloc-fragmentation
title: External fragmentation grows when live objects pin pages
tags: allocator, fragmentation, memory
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# External fragmentation grows when live objects pin pages

## Claim

Free memory exists but is split into unusable holes. An arena or a compacting GC reduces it.

## Test

Run a mixed allocation workload. Measure the largest free block and RSS.

## Proof

A stable largest block under load.

## Failure modes

Internal fragmentation is rounding. External is layout. A size-class tweak helps one, not the other.
