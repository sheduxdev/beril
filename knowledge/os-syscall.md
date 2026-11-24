---
id: os-syscall
title: A syscall is an ABI with an error convention
tags: os, syscall, errno
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A syscall is an ABI with an error convention

## Claim

The number, arguments and return convention are fixed. A negative return carries errno; seccomp can deny the call.

## Test

Call with an invalid pointer and an invalid number. Check the errno and the seccomp log.

## Proof

A correct error and no crash.

## Failure modes

A raw syscall bypasses libc wrappers. A seccomp filter can kill the process.
