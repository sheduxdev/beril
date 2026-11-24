---
id: eng-memory
title: Memory is virtual, cached and allocated in tiers
tags: engineering, os, memory
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Memory is virtual, cached and allocated in tiers

## Claim

Page tables, the page cache and the allocator decide cost. A leak is a retention graph, not a missing free.

## Test

Measure RSS, page faults and allocation rate. Take a heap profile.

## Proof

A profile that names the retaining path.

## Failure modes

RSS includes shared pages. A GC language can still leak through references.
