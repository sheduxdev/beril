---
id: srop-sets-every-register-from-a-fake-frame
title: SROP sets every register from a fake frame
tags: pwn, srop, sigreturn
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# SROP sets every register from a fake frame

## Claim

A sigreturn frame lets the attacker set rax and every register, then call execve without a full ROP chain.

## Test

Map a writable frame. Set rax to 15 and the syscall, point rsp at the frame, trigger sigreturn.

## Proof

The execve syscall runs from the frame values.

## Failure modes

A seccomp filter can block the syscall. The frame size can exceed the buffer.
