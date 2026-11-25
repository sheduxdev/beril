---
id: a-vtable-call-is-a-control-target-in-c
title: A vtable call is a control target in C++
tags: pwn, vtable, cplusplus
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/re-cpp-rtti.md, references/exploit-development.md
status: active
---
# A vtable call is a control target in C++

## Claim

An object with a corrupted vtable pointer calls an attacker chosen slot on the next virtual method.

## Test

Find the object and its vtable. Overwrite the pointer with a fake table. Call a virtual method.

## Proof

Control reaches the chosen slot.

## Failure modes

A vtable guard or a relative offset in some builds changes the write.
