---
id: binary-windows-kernel
title: Windows kernel bugs are object and IRP lifetime bugs
tags: binary, windows, kernel
confidence: high
updated: 2026-11-25
uses: 0
sources: references/reverse-engineering.md
status: active
---
# Windows kernel bugs are object and IRP lifetime bugs

## Claim

Drivers parse IOCTL buffers, user pointers and object references. A wrong probe or a stale object is the primitive.

## Test

Map IOCTLs and methods. Check probe and capture. Fuzz the buffer. Inspect pool and IRQL.

## Proof

A controlled write or a privilege escalation in a VM.

## Failure modes

A crash can be a DoS only. Check the session and the integrity level.
