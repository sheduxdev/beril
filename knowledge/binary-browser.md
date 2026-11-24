---
id: binary-browser
title: Browser exploitation needs a renderer bug and a sandbox path
tags: binary, browser, jit
confidence: high
updated: 2026-11-24
uses: 0
sources: references/exploit-development.md
status: active
---
# Browser exploitation needs a renderer bug and a sandbox path

## Claim

A JIT or DOM bug gives read/write in the renderer; a second bug or a feature escapes the sandbox.

## Test

Map the bug to a primitive. Build addrof/fakeobj. Chain to a write. Then look for a sandbox escape.

## Proof

A controlled read/write in the renderer and a host action outside it.

## Failure modes

A renderer crash is not a full chain. The sandbox is a separate boundary.
