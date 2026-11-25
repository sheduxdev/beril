---
id: a-grammar-reaches-deep-structure
title: A grammar reaches deep structure
tags: fuzz, grammar, structure
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A grammar reaches deep structure

## Claim

A byte fuzzer rarely builds a valid nested document. A grammar seeds valid structure and mutates inside it.

## Test

Write the grammar for one node. Generate seeds. Mutate a field and keep the structure. Check the depth reached.

## Proof

Inputs that reach a nested parser branch.

## Failure modes

A grammar can miss a semantic rule. A strict validator rejects the mutation.
