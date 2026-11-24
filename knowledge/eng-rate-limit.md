---
id: eng-rate-limit
title: A rate limiter needs a key, a cost and a fairness rule
tags: engineering, rate-limit, fairness
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A rate limiter needs a key, a cost and a fairness rule

## Claim

Token bucket allows bursts; leaky bucket smooths. The key decides who shares the budget.

## Test

Define the key and the burst. Test one noisy client against a quiet one.

## Proof

A noisy tenant throttled while the quiet one passes.

## Failure modes

A global limiter lets one client starve all. A per-IP key misses NAT.
