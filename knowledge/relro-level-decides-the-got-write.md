---
id: relro-level-decides-the-got-write
title: RELRO level decides the GOT write
tags: binary, relro, got
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# RELRO level decides the GOT write

## Claim

No RELRO leaves the GOT writable. Partial RELRO protects the section after the lazy binding slots. Full RELRO leaves nothing to overwrite.

## Test

Read the checksec output. Write a GOT slot in a debugger. Try the same write after a full RELRO build.

## Proof

A GOT overwrite changes the called function.

## Failure modes

A function called before the write can already be resolved. BIND_NOW closes it.
