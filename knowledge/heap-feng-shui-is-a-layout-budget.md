---
id: heap-feng-shui-is-a-layout-budget
title: Heap feng shui is a layout budget
tags: binary, heap, layout
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# Heap feng shui is a layout budget

## Claim

Allocation size, order and count decide which free chunk is reused. A stable exploit spends the budget before the trigger.

## Test

Log every allocation size. Build a sequence that opens the target slot, then trigger. Repeat and record layout drift.

## Proof

The target slot is reused in a stable share of runs.

## Failure modes

A background thread or a random cache breaks the order. A different allocator changes every step.
