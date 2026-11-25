---
id: jit-spray-turns-immediates-into-code
title: JIT spray turns immediates into code
tags: pwn, jit, spray
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-jit.md
status: active
---
# JIT spray turns immediates into code

## Claim

A JIT compiler emits attacker constants into executable memory. Chained constants can encode a small payload.

## Test

Find a JIT path with a controllable constant. Disassemble the emitted region. Chain a jump.

## Proof

The emitted region contains your instruction sequence.

## Failure modes

A large constant or a filter removes control. W^X can block a direct jump.
