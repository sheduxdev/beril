---
id: os-virtual-memory
title: Virtual memory is a translation and permission layer
tags: os, virtual-memory, paging
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Virtual memory is a translation and permission layer

## Claim

Page tables map virtual to physical; the TLB caches the translation. A permission bit is the boundary.

## Test

Trace a mapping. Check the flags. Touch a read-only page.

## Proof

A fault on the protected access.

## Failure modes

A huge page changes the TLB cost. A stale TLB entry hides a permission change.
