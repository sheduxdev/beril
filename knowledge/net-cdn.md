---
id: net-cdn
title: A CDN is a cache with a key and a purge
tags: network, cdn, cache
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A CDN is a cache with a key and a purge

## Claim

The cache key decides the hit. A purge is eventual; a versioned URL is immediate.

## Test

Change a header that is not in the key. Purge and request. Check the hit ratio.

## Proof

A cache key that separates variants and a purge that works.

## Failure modes

A cookie in the key fragments the cache. A purge across POPs is not instant.
