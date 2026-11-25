---
id: a-kernel-target-needs-a-qemu-or-a-vm-harness
title: A kernel target needs a QEMU or a VM harness
tags: fuzz, kernel, qemu
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A kernel target needs a QEMU or a VM harness

## Claim

A kernel parser crash can brick the host. The harness runs in a VM with a serial console and a snapshot.

## Test

Build the target and the disk. Boot with QEMU. Send the input over a device or a syscall. Capture the panic.

## Proof

A kernel panic with a stack and the input.

## Failure modes

A slow boot limits the rate. A hardware dependency needs a device model.
