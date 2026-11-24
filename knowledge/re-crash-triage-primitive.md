---
id: re-crash-triage-primitive
title: A crash is a lead; the primitive is the finding
tags: re, triage, crash
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md, labs/binary
status: active
---
# A crash is a lead; the primitive is the finding

## Claim

A crash becomes a finding when you can name the controlled bytes, the fault address, the instruction pointer and the blocking mitigation.

## Test

Reproduce outside the fuzzer. Read registers and stack. Classify the fault. Minimize. Check mitigations.

## Proof

A controlled address or RIP, or a bounded leak, with a repeatable input.

## Failure modes

A null dereference is low. A crash under ASAN only can still be real but needs reachability.
