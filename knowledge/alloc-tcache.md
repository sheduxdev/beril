---
id: alloc-tcache
title: Thread caches reduce contention and create remote frees
tags: allocator, tcache, threads
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Thread caches reduce contention and create remote frees

## Claim

Per-thread caches avoid a global lock, but a free from another thread goes to a remote list and causes imbalance.

## Test

Allocate on one thread, free on another. Measure cache growth and remote free.

## Proof

A bounded cache with a drain path.

## Failure modes

An unbounded tcache grows by thread count. A false sharing bug hides in the cache line.
