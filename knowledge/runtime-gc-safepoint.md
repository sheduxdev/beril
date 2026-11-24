---
id: runtime-gc-safepoint
title: A safepoint is where the runtime can move or scan
tags: runtime, gc, safepoint
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A safepoint is where the runtime can move or scan

## Claim

Threads poll a safepoint so the collector can stop them. A long loop without a poll delays the pause.

## Test

Run a tight loop in a compiled method. Measure the time to safepoint.

## Proof

A bounded safepoint latency.

## Failure modes

A safepoint in a signal can deadlock. A counted loop poll is not free.
