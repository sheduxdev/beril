---
id: re-jvm
title: JVM bytecode is a stack machine with metadata
tags: re, java, jvm
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/reverse-engineering.md
status: active
---
# JVM bytecode is a stack machine with metadata

## Claim

Class files keep names and descriptors, and JIT changes the runtime shape. Deserialization gadgets live in the classpath.

## Test

Decompile with jadx/CFR. Map the stack and descriptors. Check gadget libraries and readObject.

## Proof

A recovered class and a gadget path.

## Failure modes

An obfuscated jar hides names. A JIT crash is not a language bug.
