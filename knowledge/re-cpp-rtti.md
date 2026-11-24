---
id: re-cpp-rtti
title: C++ RTTI and vtables reveal the class graph
tags: re, cpp, rtti
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/reverse-engineering.md
status: active
---
# C++ RTTI and vtables reveal the class graph

## Claim

RTTI descriptors, vtables and multiple inheritance encode types. A cast and a vtable slot explain dispatch.

## Test

Find the vtable xrefs. Map the RTTI names. Rebuild the class layout before reading methods.

## Proof

A recovered class and a correct vtable index.

## Failure modes

RTTI can be disabled. An obfuscated vtable needs manual mapping.
