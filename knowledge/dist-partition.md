---
id: dist-partition
title: A partition forces a choice between availability and consistency
tags: distributed, partition, cap
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A partition forces a choice between availability and consistency

## Claim

During a partition, a node can serve stale data or refuse. The choice is per operation, not per system.

## Test

Partition a replica. Read and write on both sides. Check the consistency and the error.

## Proof

A documented choice with the read/write behavior under partition.

## Failure modes

A system that claims both without a partition story is marketing.
