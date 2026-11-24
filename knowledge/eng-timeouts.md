---
id: eng-timeouts
title: A call without a deadline can hang a pool
tags: engineering, timeouts, reliability
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A call without a deadline can hang a pool

## Claim

Every network call needs a deadline, a retry budget and a cancellation path. A retry without jitter amplifies load.

## Test

Kill a dependency. Watch the caller. Check pool exhaustion and retry storms.

## Proof

A bounded failure with a clear error.

## Failure modes

A retry on a non-idempotent call duplicates work.
