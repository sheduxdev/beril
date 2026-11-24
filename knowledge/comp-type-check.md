---
id: comp-type-check
title: Type checking proves a property before runtime
tags: compiler, types, soundness
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Type checking proves a property before runtime

## Claim

The checker rejects programs that violate the type rules. Soundness means no well-typed program gets stuck.

## Test

Write a bad program. Check the error location. Compare with a gradual type escape.

## Proof

A rejection with a rule and a location.

## Failure modes

An `any` escape moves the proof to runtime. An unsound cast hides it.
