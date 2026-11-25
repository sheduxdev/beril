---
id: a-device-model-is-the-host-attack-surface
title: A device model is the host attack surface
tags: hv, device-model, qemu
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# A device model is the host attack surface

## Claim

An emulated NIC, disk or GPU parses guest bytes in the host process. The parser and the DMA are the bug surface.

## Test

List the emulated devices. Pick the least common. Send malformed config and data. Watch the host process.

## Proof

A host crash or a host memory read.

## Failure modes

A passthrough device moves the surface to hardware. A hardened model can check more.
