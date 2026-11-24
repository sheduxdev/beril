---
id: eng-backpressure
title: A queue without a limit is a memory leak
tags: engineering, queue, backpressure
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A queue without a limit is a memory leak

## Claim

Producers can outrun consumers. A bounded queue, a timeout and a load-shedding rule keep the system alive.

## Test

Measure arrival and service rate. Fill the queue. Check latency and drop behavior.

## Proof

A bounded latency and an explicit drop or slow-down.

## Failure modes

An unbounded queue hides the problem until OOM.
