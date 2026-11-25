---
id: a-uaf-becomes-type-confusion-when-the-slot-is-reused
title: A UAF becomes type confusion when the slot is reused
tags: binary, uaf, type-confusion
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/re-crash-triage-primitive.md, references/exploit-development.md
status: active
---
# A UAF becomes type confusion when the slot is reused

## Claim

Reallocating the freed slot with an object of another type gives the stale pointer a different vtable or length field.

## Test

Free object A. Allocate object B of the same size with a controlled field. Call A's method and watch the field B controls.

## Proof

A controlled value reaches a call or a length.

## Failure modes

A same type reuse keeps the layout. A hardened allocator quarantines the slot.
