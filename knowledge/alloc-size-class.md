---
id: alloc-size-class
title: Size classes trade internal fragmentation for speed
tags: allocator, size-class, fragmentation
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Size classes trade internal fragmentation for speed

## Claim

Rounding a request to a class makes the free list O(1) and wastes the delta. A large delta is internal fragmentation.

## Test

Allocate sizes around a class boundary. Measure the RSS delta and the class distribution.

## Proof

A class layout with a bounded waste.

## Failure modes

A class that is too coarse wastes memory. A perfect-fit list is slow.
