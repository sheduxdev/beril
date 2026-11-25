---
id: virtio-is-a-shared-ring-between-guest-and-host
title: Virtio is a shared ring between guest and host
tags: hv, virtio, ring
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# Virtio is a shared ring between guest and host

## Claim

The descriptor ring and the used ring are shared memory. A missing length check on a descriptor reaches the host device model.

## Test

Read the device type and the queue. Send a descriptor with a short and a long buffer. Watch the host and the guest.

## Proof

A host fault or a guest read outside the buffer.

## Failure modes

A vhost backend can check in the kernel. An IOMMU can bound the DMA.
