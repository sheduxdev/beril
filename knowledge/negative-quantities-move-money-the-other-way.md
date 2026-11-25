---
id: negative-quantities-move-money-the-other-way
title: Negative quantities move money the other way
tags: web, logic, quantity
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Negative quantities move money the other way

## Claim

A cart that accepts a negative quantity can create a credit line that offsets the paid total.

## Test

Add a cheap item with quantity minus one, then a second item. Try a negative price or a decimal quantity.

## Proof

The total goes negative or the order credits the account.

## Failure modes

Validation at checkout blocks it. A refund path can produce the same effect by design.
