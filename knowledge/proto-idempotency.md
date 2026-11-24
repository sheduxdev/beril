---
id: proto-idempotency
title: A message id makes a retry safe
tags: protocol, idempotency, message-id
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A message id makes a retry safe

## Claim

The receiver dedups by id for a bounded window. A retry carries the same id.

## Test

Send the same id twice. Check the side effect and the dedup window.

## Proof

One effect and a duplicate acknowledgement.

## Failure modes

An unbounded dedup store leaks. A new id on retry doubles the effect.
