---
id: crash-dedup-needs-the-stack-and-the-root-cause
title: Crash dedup needs the stack and the root cause
tags: fuzz, dedup, triage
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md, knowledge/re-crash-triage-primitive.md
status: active
---
# Crash dedup needs the stack and the root cause

## Claim

Grouping by the top frame and the fault address is a start. The real dedup is the root cause and the fix.

## Test

Hash the stack and the fault. Read each group. Merge groups that share the missing check.

## Proof

A group per root cause with one representative input.

## Failure modes

Inlining and symbols change the stack. A generic crash site can hide two causes.
