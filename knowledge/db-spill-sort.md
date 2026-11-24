---
id: db-spill-sort
title: External sort spills sorted runs and merges them
tags: database, sort, spill
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# External sort spills sorted runs and merges them

## Claim

Memory fills, runs are written to disk and a merge follows. The spill path is the cost.

## Test

Sort more rows than the memory limit. Measure spill bytes and merge time.

## Proof

A sorted result within the disk budget.

## Failure modes

A spill to a slow disk stalls the query. A merge with too many runs hits the file limit.
