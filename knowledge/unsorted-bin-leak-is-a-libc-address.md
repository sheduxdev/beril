---
id: unsorted-bin-leak-is-a-libc-address
title: Unsorted bin leak is a libc address
tags: pwn, unsorted-bin, leak
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# Unsorted bin leak is a libc address

## Claim

A freed chunk in the unsorted bin holds a main arena pointer. Reading it leaks libc if the chunk is readable.

## Test

Free a chunk outside tcache. Read its fd. Compare the offset with the libc base.

## Proof

The leaked value maps to a known libc symbol.

## Failure modes

Tcache size and count catch the free. A zeroed pointer hides it.
