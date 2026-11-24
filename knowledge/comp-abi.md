---
id: comp-abi
title: An ABI is a contract between compiled units
tags: compiler, abi, calling-convention
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An ABI is a contract between compiled units

## Claim

Argument registers, stack alignment, red zone and return values are fixed. A mismatch is a silent corruption.

## Test

Compile a caller and callee from different units. Check the registers and alignment.

## Proof

A call that passes the argument and returns correctly.

## Failure modes

A variadic call differs. A struct return may use a hidden pointer.
