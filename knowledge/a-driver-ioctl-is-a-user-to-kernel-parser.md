---
id: a-driver-ioctl-is-a-user-to-kernel-parser
title: A driver IOCTL is a user to kernel parser
tags: wink, driver, ioctl
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-windows-kernel.md
status: active
---
# A driver IOCTL is a user to kernel parser

## Claim

The IOCTL code selects a handler and the input buffer is user controlled. The handler must copy and validate before use.

## Test

List the device and the codes. Send a small and a large buffer. Watch the fault and the copy.

## Proof

A kernel fault or a controlled read/write.

## Failure modes

A probe and lock wrapper can copy safely. A code can be unreachable without a right.
