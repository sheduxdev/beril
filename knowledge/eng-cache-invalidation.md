---
id: eng-cache-invalidation
title: A cache needs a key, a TTL and an invalidation path
tags: engineering, cache, invalidation
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A cache needs a key, a TTL and an invalidation path

## Claim

A cache without an invalidation story serves stale data. The key and the invalidation event are the design.

## Test

Write a value, update the source, read again. Check the TTL and the invalidation.

## Proof

A read after a write returns the new value.

## Failure modes

A short TTL hides a missing invalidation until the write path is slow.
