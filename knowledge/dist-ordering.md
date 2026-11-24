---
id: dist-ordering
title: Exactly-once is at-least-once plus dedup
tags: distributed, ordering, dedup
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Exactly-once is at-least-once plus dedup

## Claim

The network duplicates and reorders. The consumer must dedup and tolerate order.

## Test

Redeliver and reorder messages. Check the consumer and the state.

## Proof

One effect per message id with a bounded dedup store.

## Failure modes

An unbounded dedup set is a leak. A sequence number without a gap policy is a stall.
