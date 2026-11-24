---
id: hw-irq
title: An interrupt handler must be short and defer the rest
tags: hardware, interrupt, latency
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An interrupt handler must be short and defer the rest

## Claim

The top half masks the line and acknowledges; the bottom half does the work. A long top half adds latency.

## Test

Measure interrupt latency under load. Move work to the bottom half.

## Proof

A bounded latency with the work deferred.

## Failure modes

A blocking call in the handler stalls the system. A missed acknowledgement floods interrupts.
