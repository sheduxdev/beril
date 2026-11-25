---
id: wasm-memory-bounds-are-checked-per-access
title: WASM memory bounds are checked per access
tags: binary, wasm, bounds
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-wasm.md
status: active
---
# WASM memory bounds are checked per access

## Claim

Linear memory access is bounds checked, so the bug moves to the host imports, the table and the JIT boundary.

## Test

Read the imports and the exported functions. Send an out of range offset. Then attack a host call that copies or indexes.

## Proof

A host side out of bounds or a type confusion across the boundary.

## Failure modes

A memory safe host with checked imports holds. A JIT bug can bypass the model.
