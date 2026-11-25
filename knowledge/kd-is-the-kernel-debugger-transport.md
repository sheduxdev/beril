---
id: kd-is-the-kernel-debugger-transport
title: KD is the kernel debugger transport
tags: wink, kd, debug
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# KD is the kernel debugger transport

## Claim

A kernel debug connection can break, read and write. A VM with a named pipe is enough for a lab.

## Test

Start the VM with the debug flag. Connect with WinDbg. Break and read a symbol.

## Proof

A break and a symbol read.

## Failure modes

A production host needs a boot change. A network debug needs a second host.
