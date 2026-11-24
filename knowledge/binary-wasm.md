---
id: binary-wasm
title: Wasm modules have validation and a host boundary
tags: binary, wasm, sandbox
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/reverse-engineering.md
status: active
---
# Wasm modules have validation and a host boundary

## Claim

The validator enforces types and stack rules; imports are the host surface. A JIT bug or a broad import breaks the sandbox.

## Test

Inspect the imports and memory. Try a malformed module. Check the host calls and the JIT flags.

## Proof

A host call or memory access outside the module's grant.

## Failure modes

A pure compute module with no imports is low risk. The host wrapper matters.
