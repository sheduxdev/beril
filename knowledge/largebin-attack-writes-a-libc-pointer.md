---
id: largebin-attack-writes-a-libc-pointer
title: Largebin attack writes a libc pointer
tags: pwn, largebin, write
confidence: low
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# Largebin attack writes a libc pointer

## Claim

Largebin insertion writes a chunk address into a target, which can corrupt a function pointer or a global.

## Test

Place chunks in the largebin. Set bk_nextsize. Insert and read the target.

## Proof

The target address changes to the chunk address.

## Failure modes

A size check and a sort order guard block it. The glibc version matters.
