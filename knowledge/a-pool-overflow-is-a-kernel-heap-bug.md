---
id: a-pool-overflow-is-a-kernel-heap-bug
title: A pool overflow is a kernel heap bug
tags: wink, pool, overflow
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/binary-windows-kernel.md
status: active
---
# A pool overflow is a kernel heap bug

## Claim

A non paged pool allocation with a user length and a missing bound corrupts the next pool header.

## Test

Find the allocation and the copy. Send a length over the chunk. Enable pool tagging and special pool.

## Proof

A bugcheck with the pool address and the overwritten bytes.

## Failure modes

A guarded allocation closes it. A different pool type changes the layout.
