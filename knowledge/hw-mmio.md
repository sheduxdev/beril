---
id: hw-mmio
title: MMIO needs volatile access and barriers
tags: hardware, mmio, barriers
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# MMIO needs volatile access and barriers

## Claim

A register read can be cached or reordered. A volatile access plus a barrier enforces the order the device expects.

## Test

Write a register then read the status. Check the generated instructions and the barrier.

## Proof

An access order that matches the datasheet.

## Failure modes

A plain pointer read is optimized away. A missing barrier lets the write arrive late.
