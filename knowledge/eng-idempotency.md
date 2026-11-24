---
id: eng-idempotency
title: Every retryable write needs a key
tags: engineering, idempotency, retry
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Every retryable write needs a key

## Claim

A client retry or a queue redelivery can duplicate a write. An idempotency key or a natural unique constraint makes it safe.

## Test

Send the same write twice. Check the side effect. Scope the key to the user and the operation.

## Proof

One effect after two identical requests.

## Failure modes

A key that is not stored has no effect. A key without a scope can collide.
