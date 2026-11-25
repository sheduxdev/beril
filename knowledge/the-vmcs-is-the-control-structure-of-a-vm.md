---
id: the-vmcs-is-the-control-structure-of-a-vm
title: The VMCS is the control structure of a VM
tags: hv, vmcs, cpu
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-hypervisor.md
status: active
---
# The VMCS is the control structure of a VM

## Claim

The VMCS holds the exit controls, the host state and the guest state. A write to it changes where an exit lands.

## Test

Read the VMCS fields with a debug tool. Change one host field. Trigger an exit and read the stack.

## Proof

An exit with the changed host state.

## Failure modes

A cached VMCS needs a sync. A nested VMCS is a different structure.
