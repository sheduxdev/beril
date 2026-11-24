---
id: api-idempotency
title: Retries need an idempotency key at the write
tags: api, idempotency, retry
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Retries need an idempotency key at the write

## Claim

The client retries a create or pay call and the server has no idempotency key or unique constraint.

## Test

Send the same request twice with and without the key. Compare row counts and side effects.

## Proof

One effect with the key, two without it.

## Failure modes

A GET retry is harmless. A key that is not scoped to the user can collide.
