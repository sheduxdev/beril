---
id: build-incremental
title: An incremental build is a cache keyed on inputs
tags: build, incremental, cache
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An incremental build is a cache keyed on inputs

## Claim

The key is the content of the inputs, not the timestamp. A wrong key gives a stale output.

## Test

Touch a file without changing it. Edit a transitive header. Check what rebuilt.

## Proof

A rebuild that changes only the affected outputs.

## Failure modes

A mtime-based key misses a content change. A cache without the compiler version poisons.
