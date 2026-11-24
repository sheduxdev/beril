---
id: trace-sampling
title: Sampling must be consistent or the trace is partial
tags: observability, sampling, tracing
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Sampling must be consistent or the trace is partial

## Claim

Head sampling decides at the root and propagates the flag. Tail sampling buffers and decides on the whole trace.

## Test

Sample at 1%. Check that all spans of a sampled trace appear.

## Proof

A complete or absent trace, never a partial one.

## Failure modes

Independent per-service sampling produces orphan spans. Tail sampling costs memory.
