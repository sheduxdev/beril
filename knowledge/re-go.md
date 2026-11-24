---
id: re-go
title: Go binaries carry pclntab and interface metadata
tags: re, go, language
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/reverse-engineering.md
status: active
---
# Go binaries carry pclntab and interface metadata

## Claim

Function names, file paths and type information survive in pclntab and itab structures, even when stripped.

## Test

Use GoReSym or redress. Recover functions and build info. Map interface calls through itab.

## Proof

Named functions and a recovered interface dispatch.

## Failure modes

The symbol table can be stripped. pclntab may still be there.
