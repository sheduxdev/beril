---
id: a-stack-pivot-moves-rsp-to-controlled-memory
title: A stack pivot moves RSP to controlled memory
tags: pwn, stack-pivot, rop
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# A stack pivot moves RSP to controlled memory

## Claim

A leave ret or a xchg rsp gadget turns a short overwrite into a full chain in a buffer or a heap chunk.

## Test

Find the pivot. Put the chain at the target address. Return into the pivot and step through.

## Proof

RSP points at your chain and the first gadget runs.

## Failure modes

A canary or a stack limit blocks the first overwrite. The target memory can be non executable.
