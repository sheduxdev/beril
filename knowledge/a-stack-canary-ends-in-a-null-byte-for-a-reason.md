---
id: a-stack-canary-ends-in-a-null-byte-for-a-reason
title: A stack canary ends in a null byte for a reason
tags: binary, canary, stack
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md, knowledge/re-crash-triage-primitive.md
status: active
---
# A stack canary ends in a null byte for a reason

## Claim

The low null byte stops a string overflow from leaking the canary, so a leak must start one byte later or come from another bug.

## Test

Overflow a buffer with a long string and read back. Look for the null at the start of the canary. Try an off by one or a format string.

## Proof

The canary value is recovered and the overwrite reaches the return address.

## Failure modes

A canary without the null is easier. A fork server keeps the same canary and one leak is enough.
