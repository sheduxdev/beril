---
id: repair-read-repair
title: Read repair fixes a replica on the read path
tags: distributed-storage, read-repair, version
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Read repair fixes a replica on the read path

## Claim

The coordinator compares versions from the replicas and writes the newest back to the stale ones. A digest mismatch triggers it.

## Test

Write to one replica only. Read with a quorum. Check the stale replica's version after the read.

## Proof

All replicas converge after the read without a background job.

## Failure modes

A read repair without a version conflict rule picks a loser. A read from one replica never repairs.
