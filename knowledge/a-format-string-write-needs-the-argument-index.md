---
id: a-format-string-write-needs-the-argument-index
title: A format string write needs the argument index
tags: binary, format-string, write
confidence: high
updated: 2026-11-26
uses: 0
sources: references/exploit-development.md
status: active
---
# A format string write needs the argument index

## Claim

`%n` writes the printed count. The right positional argument and a controlled count turn a read into an arbitrary write.

## Test

Find the offset with AAAA and `%p`. Use `%<n>c%<offset>$n` with a target address on the stack or a known pointer.

## Proof

The target address changes to the chosen value.

## Failure modes

A stack limit caps the width. A pointer must be placed at a known offset.
