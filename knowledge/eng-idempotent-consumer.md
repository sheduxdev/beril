---
id: eng-idempotent-consumer
title: At-least-once delivery needs an idempotent consumer
tags: engineering, queue, consumer
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# At-least-once delivery needs an idempotent consumer

## Claim

The queue can redeliver. The consumer must deduplicate by message id or a natural key.

## Test

Deliver the same message twice. Check the side effect. Kill the consumer mid-processing.

## Proof

One effect after a redelivery.

## Failure modes

A local set grows without bound. Store the dedup key with the effect.
