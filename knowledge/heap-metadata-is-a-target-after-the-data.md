---
id: heap-metadata-is-a-target-after-the-data
title: Heap metadata is a target after the data
tags: pwn, heap, metadata
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-kernel.md, references/exploit-development.md
status: active
---
# Heap metadata is a target after the data

## Claim

A chunk header holds size, prev size and flags. An overflow into the next header changes consolidation and bin placement.

## Test

Map chunk headers around the target. Overflow one byte into the size. Free and inspect the bins.

## Proof

A controlled consolidation or unlink.

## Failure modes

Safe linking and size checks catch a wrong value. A different allocator changes the layout.
