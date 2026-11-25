---
id: nested-virtualization-exposes-the-l1-hypervisor
title: Nested virtualization exposes the L1 hypervisor
tags: hv, nested, vmcs
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# Nested virtualization exposes the L1 hypervisor

## Claim

A guest that can run a hypervisor controls a nested VMCS and can attack the L1 through the virtual VMX.

## Test

Enable nested in L1. Run a small L2. Read the virtual VMCS fields. Try a nested exit path.

## Proof

A controlled L2 exit into L1.

## Failure modes

A blocked nested flag closes it. A different CPU vendor changes the fields.
