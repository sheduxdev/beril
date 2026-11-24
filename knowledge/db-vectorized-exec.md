---
id: db-vectorized-exec
title: Vectorized execution amortizes per-row cost
tags: database, vectorized, execution
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Vectorized execution amortizes per-row cost

## Claim

Operators process batches, improving cache and branch behavior. The batch size is a tradeoff.

## Test

Compare a row-at-a-time and a vectorized operator on the same data.

## Proof

A faster operator with a bounded batch memory.

## Failure modes

A batch that is too large spills the cache. A small batch loses the gain.
