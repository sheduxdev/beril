---
id: the-dyld-shared-cache-is-a-map-of-every-library
title: The dyld shared cache is a map of every library
tags: macos, dyld, library
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# The dyld shared cache is a map of every library

## Claim

The cache holds the system libraries. The load order and the insert path decide whether a proxy library wins.

## Test

Find the cache and the load paths. Check `DYLD_INSERT_LIBRARIES` and the hardened runtime. Place a proxy and observe.

## Proof

A proxy library loaded into the target.

## Failure modes

A hard runtime and a restricted binary ignore the variable. A signed library can be required.
