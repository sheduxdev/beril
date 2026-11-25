---
id: an-iommu-bounds-device-dma
title: An IOMMU bounds device DMA
tags: hv, iommu, dma
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# An IOMMU bounds device DMA

## Claim

The IOMMU maps a device to a domain. A missing mapping or a wide domain lets the device read host memory.

## Test

Read the IOMMU state and the domain. Attach a device. Read a physical range outside the guest.

## Proof

A DMA read outside the mapped range.

## Failure modes

A strict domain and a small mapping hold. A passthrough device needs the whole domain.
