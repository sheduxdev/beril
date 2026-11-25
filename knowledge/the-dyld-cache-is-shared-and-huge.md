---
id: the-dyld-cache-is-shared-and-huge
title: The dyld cache is shared and huge
tags: ios, dyld, cache
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/mobile-reverse.md
status: active
---
# The dyld cache is shared and huge

## Claim

The cache holds the system libraries on iOS. A symbol lives in the cache, not in a file, so the offset base is fixed per build.

## Test

Locate the cache. Resolve the symbol offset with a tool. Compare two builds of the same version.

## Proof

A resolved symbol and the base offset.

## Failure modes

A cache can be split. A different build shifts every offset.
