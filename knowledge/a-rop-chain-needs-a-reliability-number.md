---
id: a-rop-chain-needs-a-reliability-number
title: A ROP chain needs a reliability number
tags: pwn, rop, reliability
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md, references/senior-bar.md
status: active
---
# A ROP chain needs a reliability number

## Claim

A chain that works once can depend on a lucky address, a heap state or a race. It is not a PoC until the rate is measured.

## Test

Run the chain twenty times from a clean start. Record crashes, misses and hits. Report the share.

## Proof

A written rate with the environment and the build hash.

## Failure modes

A deterministic chain still depends on the loader. A noisy host hides the real rate.
