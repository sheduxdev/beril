---
id: eng-performance-budget
title: Performance is a budget before it is an optimization
tags: engineering, performance, budget
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Performance is a budget before it is an optimization

## Claim

Name p50, p95, payload, memory and cost. Measure the same workload before and after.

## Test

Set the budget. Profile. Find the dominant term. Re-measure.

## Proof

A benchmark that fits the budget and runs in CI.

## Failure modes

A micro-optimization of a cold path is waste.
