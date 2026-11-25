---
id: a-got-overwrite-needs-a-call-after-the-write
title: A GOT overwrite needs a call after the write
tags: pwn, got, partial-relro
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# A GOT overwrite needs a call after the write

## Claim

Overwriting a GOT slot only matters if the function is called again after the write and before exit.

## Test

Pick a function with a later call. Write the slot. Call the path and watch the target.

## Proof

The redirected function runs.

## Failure modes

Full RELRO or an early resolved call removes the window.
