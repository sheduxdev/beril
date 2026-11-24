---
id: api-batch
title: A batch endpoint checks the envelope, not each item
tags: api, batch, auth
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# A batch endpoint checks the envelope, not each item

## Claim

The batch handler authenticates once and applies items by id without per-item authorization or partial-failure reporting.

## Test

Send a batch with one allowed and one forbidden item. Check the response and the side effects.

## Proof

A forbidden item succeeds, or the error hides which item failed.

## Failure modes

A batch that stops on the first error is safer. Check idempotency too.
