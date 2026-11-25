---
id: msg-msg-is-the-kernel-heap-spray-primitive
title: msg_msg is the kernel heap spray primitive
tags: binary, kernel, heap
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# msg_msg is the kernel heap spray primitive

## Claim

A small `msg_msg` allocation lets a user control the data after the header and is a reliable spray and leak source in the kernel heap.

## Test

Send messages of the target size in a loop. Read back after a free. Check the header layout and the size class.

## Proof

A controlled object lands in the freed slot and a leak or write follows.

## Failure modes

A hardened slab allocator and random caches make it noisy. A tiny allocation uses a different cache.
