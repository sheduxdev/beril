---
id: slub-is-a-per-cpu-cache
title: SLUB is a per CPU cache
tags: link, slub, heap
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md
status: active
---
# SLUB is a per CPU cache

## Claim

Objects come from a per CPU freelist. A free and a reallocation on the same CPU are predictable, across CPUs are not.

## Test

Read the cache and the CPU count. Free an object. Allocate on the same and on another CPU. Compare the addresses.

## Proof

A reused slot on the same CPU.

## Failure modes

An interrupt can migrate the thread. A hardened allocator adds random.
