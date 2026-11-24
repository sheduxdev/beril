---
id: perf-profiling
title: Sampling measures where time goes; instrumentation measures counts
tags: performance, profiling, flamegraph
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Sampling measures where time goes; instrumentation measures counts

## Claim

A sampler interrupts at intervals and aggregates stacks. Instrumentation counts events but distorts the timeline.

## Test

Profile a hot endpoint. Compare a sampling flame graph with an instrumented trace.

## Proof

A flame graph whose widest frame matches the fix.

## Failure modes

A profiler without symbols is noise. An instrumented hot path measures itself.
