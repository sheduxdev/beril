---
id: hw-dma
title: DMA bypasses the CPU cache and needs ownership rules
tags: hardware, dma, coherency
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# DMA bypasses the CPU cache and needs ownership rules

## Claim

The device writes memory the CPU may have cached. A coherent mapping or an explicit flush keeps them in sync.

## Test

Start a DMA transfer. Read the buffer immediately. Check for stale data.

## Proof

A buffer with a correct flush or a coherent mapping.

## Failure modes

A non-coherent platform returns stale cache lines. A buffer freed during DMA corrupts memory.
