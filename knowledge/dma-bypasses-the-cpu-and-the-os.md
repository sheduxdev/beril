---
id: dma-bypasses-the-cpu-and-the-os
title: DMA bypasses the CPU and the OS
tags: wink, dma, hardware
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# DMA bypasses the CPU and the OS

## Claim

A device with bus master DMA reads memory without the kernel. IOMMU and VT-d decide whether it is contained.

## Test

Check the IOMMU state. Attach a DMA capable device. Read a known physical range.

## Proof

A memory read over DMA.

## Failure modes

An IOMMU with a strict domain blocks it. A Thunderbolt port can be disabled.
