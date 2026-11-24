---
id: binary-kernel
title: A kernel bug is an object lifetime bug with a user buffer
tags: binary, kernel, driver
confidence: high
updated: 2026-11-24
uses: 0
sources: references/reverse-engineering.md
status: active
---
# A kernel bug is an object lifetime bug with a user buffer

## Claim

An IOCTL trusts a user pointer or size, or an object is freed while a callback still references it.

## Test

Map the IOCTL codes. Check METHOD_NEITHER and probe calls. Fuzz the buffer and watch pool corruption.

## Proof

A controlled write or a privilege escalation in a VM.

## Failure modes

A crash in a driver can be a bug but not exploitable. Check the pool and the IRQL.
