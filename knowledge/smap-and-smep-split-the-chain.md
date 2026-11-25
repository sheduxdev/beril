---
id: smap-and-smep-split-the-chain
title: SMAP and SMEP split the chain
tags: pwn, kernel, smap
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# SMAP and SMEP split the chain

## Claim

With SMEP the kernel cannot execute user pages, and with SMAP it cannot read them. A ret2usr chain fails.

## Test

Check the CPU flags and the CR4 bits. Try a user shellcode return. Move the chain to kernel memory.

## Proof

A kernel ROP chain runs where a user chain failed.

## Failure modes

A kernel that disables SMAP can accept the user chain. A KPTI trampoline is needed for return.
