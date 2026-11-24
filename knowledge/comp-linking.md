---
id: comp-linking
title: Linking resolves symbols and applies relocations
tags: compiler, linker, relocation
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Linking resolves symbols and applies relocations

## Claim

The linker maps sections, resolves symbols and rewrites addresses. Static and dynamic linking differ in when.

## Test

Inspect relocations and the symbol table. Compare a static and a dynamic build.

## Proof

A correct address and a resolved symbol.

## Failure modes

A duplicate symbol or a missing relocation is a load failure. Lazy binding hides cost until the first call.
