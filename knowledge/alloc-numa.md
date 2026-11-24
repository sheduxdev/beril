---
id: alloc-numa
title: NUMA locality is decided by first touch
tags: allocator, numa, memory
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# NUMA locality is decided by first touch

## Claim

A page lives on the node that first touched it. A remote access costs more than a local one.

## Test

Pin a thread to a node. Allocate and touch. Measure remote access and bandwidth.

## Proof

A local allocation policy and a lower remote ratio.

## Failure modes

A first touch on the wrong node follows the object. Migration is expensive.
