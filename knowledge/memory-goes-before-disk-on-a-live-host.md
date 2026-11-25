---
id: memory-goes-before-disk-on-a-live-host
title: Memory goes before disk on a live host
tags: ir, memory, order
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-memory.md
status: active
---
# Memory goes before disk on a live host

## Claim

Rebooting or pulling power loses keys, sessions and injected code. Volatile collection comes first when the host is live.

## Test

Write the order on one page. Collect memory, then network state, then disk. Note what each step costs.

## Proof

A memory image with the volatile artifacts and a documented order.

## Failure modes

A memory capture can crash a fragile host. A hypervisor snapshot can replace it.
