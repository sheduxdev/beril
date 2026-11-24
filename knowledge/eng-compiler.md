---
id: eng-compiler
title: A compiler is a pipeline of representations
tags: engineering, compiler, parsing
confidence: low
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A compiler is a pipeline of representations

## Claim

Lex, parse, lower to IR, optimize, emit. Each stage has an invariant and a test.

## Test

Write the AST and the invariant. Test one stage at a time.

## Proof

A minimal program through every stage.

## Failure modes

An optimizer without a semantics test changes behavior.
