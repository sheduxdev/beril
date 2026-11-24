---
id: eng-load-test
title: A load model needs an open or closed loop
tags: engineering, load, testing
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A load model needs an open or closed loop

## Claim

Open-loop arrival rate exposes queueing. Closed-loop users hide latency behind think time.

## Test

Choose the model. Ramp to saturation. Measure latency and error rate.

## Proof

A saturation point and a latency curve.

## Failure modes

A closed loop at fixed concurrency understates queueing. A test from one host saturates the host first.
