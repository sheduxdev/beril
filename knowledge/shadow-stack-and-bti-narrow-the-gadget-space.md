---
id: shadow-stack-and-bti-narrow-the-gadget-space
title: Shadow stack and BTI narrow the gadget space
tags: binary, jop, mitigation
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md, knowledge/binary-jit.md
status: active
---
# Shadow stack and BTI narrow the gadget space

## Claim

CET shadow stack checks the return address and BTI requires a landing pad, so a plain ret2libc or a mid instruction jump can fail.

## Test

Check the ELF notes for SHSTK and IBT. Try a mid instruction gadget and a return chain. Read the fault.

## Proof

The chain fails on a control protected binary and succeeds when the landing pad is fixed.

## Failure modes

CET can be off at runtime. A JOP chain with valid entries still works.
