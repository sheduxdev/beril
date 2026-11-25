---
id: hvci-runs-the-kernel-in-a-virtual-layer
title: HVCI runs the kernel in a virtual layer
tags: wink, hvci, virtualization
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# HVCI runs the kernel in a virtual layer

## Claim

Hypervisor protected code integrity checks kernel pages with a second layer. A kernel write to code can need a different step.

## Test

Read the HVCI state. Try a classic code patch. Check whether the page is executable after the write.

## Proof

A patch that fails under HVCI and works after a proper remap.

## Failure modes

A data only patch works. A vulnerable signed driver can carry the code.
