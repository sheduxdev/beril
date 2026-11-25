---
id: io-uring-is-a-shared-ring
title: io_uring is a shared ring
tags: link, io-uring, kernel
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# io_uring is a shared ring

## Claim

The submission and completion rings are shared memory. A missing validation of the opcode or the buffer reaches kernel parsers.

## Test

Read the opcodes and the registered buffers. Send a crafted submission. Watch the completion and the kernel log.

## Proof

A kernel fault or a controlled read from a submission.

## Failure modes

A restriction mode narrows the opcodes. A kernel version can lack the feature.
