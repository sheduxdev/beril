---
id: re-arm64
title: AArch64 has a calling convention, PAC and MTE
tags: re, arm64, pac
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/reverse-engineering.md
status: active
---
# AArch64 has a calling convention, PAC and MTE

## Claim

Arguments go in x0-x7, returns in x0. Pointer authentication signs pointers; MTE tags memory.

## Test

Map registers and stack. Check PAC instructions and MTE settings. Test a return address overwrite.

## Proof

A recovered prototype or a controlled return path.

## Failure modes

An emulator may not enforce PAC. MTE is optional per allocation.
