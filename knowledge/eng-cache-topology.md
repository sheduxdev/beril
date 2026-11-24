---
id: eng-cache-topology
title: Cache placement decides the failure mode
tags: engineering, cache, topology
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Cache placement decides the failure mode

## Claim

Cache-aside is simple but stampedes. Write-through is consistent but slower. A local cache diverges per node.

## Test

Name the placement. Test a miss storm and a write.

## Proof

A stampede guard and a clear invalidation.

## Failure modes

A local cache without pub/sub is stale by design.
