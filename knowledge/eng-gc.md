---
id: eng-gc
title: A GC trades throughput for pause and space
tags: engineering, gc, allocation
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A GC trades throughput for pause and space

## Claim

Generational, concurrent and compacting collectors change pause and CPU. Allocation rate is the input.

## Test

Measure allocation rate and pause. Reduce churn. Check the collector flags.

## Proof

A lower allocation rate and a shorter p99 pause.

## Failure modes

A GC language can still leak through references. A bigger heap hides a leak.
