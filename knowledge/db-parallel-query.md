---
id: db-parallel-query
title: A parallel plan needs even work and a worker limit
tags: database, parallel, skew
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A parallel plan needs even work and a worker limit

## Claim

Workers split the scan; a skewed key makes one worker the tail. The limit protects the host.

## Test

Run a plan with a skewed key. Measure the slowest worker.

## Proof

A plan with balanced workers and a bounded memory.

## Failure modes

More workers can increase contention. A parallel plan on a tiny table is overhead.
