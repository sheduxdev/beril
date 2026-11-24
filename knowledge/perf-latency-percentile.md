---
id: perf-latency-percentile
title: A percentile hides the shape and coordinated omission
tags: performance, latency, percentile
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A percentile hides the shape and coordinated omission

## Claim

A p99 from a closed loop with think time understates the tail. The histogram shape matters more than one number.

## Test

Compare a fixed-rate load with a closed-loop test at the same throughput.

## Proof

A latency histogram from an open-loop load.

## Failure modes

An average hides the tail. A p99 without a histogram hides bimodality.
