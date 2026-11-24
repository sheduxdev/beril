---
id: runtime-exception
title: Exception tables describe where a throw may land
tags: runtime, exceptions, unwind
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Exception tables describe where a throw may land

## Claim

The compiler emits a table of protected ranges and landing pads. The unwinder walks it without a frame pointer chain.

## Test

Throw inside a protected range and outside it. Check the handler and the termination.

## Proof

The correct landing pad or a clean terminate.

## Failure modes

A missing table entry skips a handler. A catch of the wrong type terminates.
