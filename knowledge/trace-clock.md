---
id: trace-clock
title: Span duration needs a monotonic clock, not wall time
tags: observability, clock, tracing
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Span duration needs a monotonic clock, not wall time

## Claim

Wall clocks skew between hosts; durations from wall timestamps can be negative. A monotonic source fixes duration.

## Test

Compare a parent duration with the sum of children across hosts.

## Proof

A duration that is positive and consistent with the children.

## Failure modes

A negative span duration is a clock bug. A wall-clock ordering of spans misleads.
