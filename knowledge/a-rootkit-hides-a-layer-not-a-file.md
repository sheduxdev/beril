---
id: a-rootkit-hides-a-layer-not-a-file
title: A rootkit hides a layer, not a file
tags: malware, rootkit, kernel
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# A rootkit hides a layer, not a file

## Claim

A user mode rootkit hooks APIs. A kernel rootkit changes the structures the APIs read. The detection layer moves with it.

## Test

Compare the API view with a raw artifact view. Check the SSDT, the IDT and the driver list. Use a cross view tool.

## Proof

A file or a process visible in one view and absent in the other.

## Failure modes

A firmware rootkit is below the OS view. A hypervisor rootkit is below the kernel.
