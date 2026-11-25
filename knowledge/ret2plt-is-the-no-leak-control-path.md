---
id: ret2plt-is-the-no-leak-control-path
title: ret2plt is the no leak control path
tags: pwn, rop, plt
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# ret2plt is the no leak control path

## Claim

When the binary has no PIE or a known base, a PLT entry calls a libc function without a libc leak.

## Test

Check PIE and RELRO. Find a call site with a controlled first argument. Build a chain through the PLT.

## Proof

The chosen libc function runs with the argument you control.

## Failure modes

Full RELRO still leaves the PLT. A missing gadget blocks the argument setup.
