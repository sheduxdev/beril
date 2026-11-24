---
id: storage-compaction
title: Compaction trades space and read speed for write stalls
tags: storage, compaction, lsm, write, stall, sorted-runs
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Compaction trades space and read speed for write stalls

## Claim

Merging sorted runs removes tombstones and stale versions. The write path stalls when compaction falls behind.

## Test

Measure write stall and read amplification under a steady write load.

## Proof

A compaction policy that keeps stalls under the budget.

## Failure modes

A full compaction on a large store takes hours. A tombstone dropped too early resurrects data.
