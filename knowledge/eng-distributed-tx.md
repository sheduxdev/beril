---
id: eng-distributed-tx
title: A saga is a sequence with compensation
tags: engineering, distributed, transaction
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A saga is a sequence with compensation

## Claim

A distributed write has no single transaction. Each step needs a compensating action and a retry policy.

## Test

Fail a middle step. Check the compensation and the final state.

## Proof

A consistent final state after a partial failure.

## Failure modes

A compensation that is not idempotent can double-refund.
