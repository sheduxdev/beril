---
id: wasm-jit-bugs-cross-the-browser-sandbox
title: WASM JIT bugs cross the browser sandbox
tags: browser, wasm, jit
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-wasm.md, knowledge/binary-browser.md
status: active
---
# WASM JIT bugs cross the browser sandbox

## Claim

A JIT bug gives read and write in the renderer, and a second bug or a feature escapes the sandbox.

## Test

Read the wasm flags and the compiler. Fuzz an exported function. Check the memory and the table.

## Proof

A controlled read outside the linear memory.

## Failure modes

A bounds check and a hardened JIT catch it. A non JIT path is slower and safer.
