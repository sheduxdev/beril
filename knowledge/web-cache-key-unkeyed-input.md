---
id: web-cache-key-unkeyed-input
title: Cache poisoning is an unkeyed input that changes the response
tags: web, cache, cdn
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Cache poisoning is an unkeyed input that changes the response

## Claim

A header, cookie or query changes the response but not the cache key. A shared cache then serves it to another user.

## Test

Map the key. Change one unkeyed input. Poison with a unique value and request from a clean session.

## Proof

A clean request returns the attacker value, with cache headers showing a hit.

## Failure modes

A hit for your own cookie is not global. Vary and normalization can invalidate the result.
