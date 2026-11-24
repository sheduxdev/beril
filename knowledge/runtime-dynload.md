---
id: runtime-dynload
title: Dynamic loading runs initializers before main
tags: runtime, dynload, init-order
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Dynamic loading runs initializers before main

## Claim

The loader maps the library, resolves symbols and runs constructors in dependency order. Interposition changes the target.

## Test

Load a plugin with a constructor. Check the order and the symbol that resolves.

## Proof

A predictable init order and a resolved symbol.

## Failure modes

A constructor that depends on another library's state is fragile. An interposed symbol changes behavior silently.
