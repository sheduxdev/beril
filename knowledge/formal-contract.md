---
id: formal-contract
title: A contract is a precondition, a postcondition and an invariant
tags: formal, contract, runtime
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A contract is a precondition, a postcondition and an invariant

## Claim

The contract states what the caller and callee may assume. A runtime check catches a violation at the boundary.

## Test

Write the contract. Call with a violated precondition. Check the assertion.

## Proof

A clear failure at the boundary.

## Failure modes

A contract in a comment is not enforced. A debug-only check disappears in production.
