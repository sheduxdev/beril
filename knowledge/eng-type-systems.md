---
id: eng-type-systems
title: Types are a proof the compiler can check
tags: engineering, types, compiler
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Types are a proof the compiler can check

## Claim

Sum types, variance and exhaustiveness remove whole classes of invalid state.

## Test

Model the state as a sum type. Make illegal states unrepresentable. Add an exhaustive match.

## Proof

A compiler error on the missing case.

## Failure modes

A cast or any type can erase the proof. Runtime data still needs validation.
