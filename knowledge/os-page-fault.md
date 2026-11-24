---
id: os-page-fault
title: A page fault is a trap, not always a disk read
tags: os, page-fault, memory
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A page fault is a trap, not always a disk read

## Claim

A minor fault maps an existing page; a major fault reads from disk. Both cost a trap and a TLB change.

## Test

Measure minor and major faults under a workload. Touch a cold mapping.

## Proof

A fault profile and a lower major rate.

## Failure modes

A major fault in a hot loop destroys latency. Prefaulting helps only a known working set.
