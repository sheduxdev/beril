---
id: os-scheduler
title: A scheduler chooses runnable work under a policy
tags: os, scheduler, priority
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A scheduler chooses runnable work under a policy

## Claim

Priority, deadline, fair share and affinity decide the next thread. A busy system exposes starvation.

## Test

Run a CPU hog with a high-priority thread. Measure the low-priority latency.

## Proof

A bounded latency under the policy.

## Failure modes

A priority boost can invert the intent. A real-time class can starve everything else.
