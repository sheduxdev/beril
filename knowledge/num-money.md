---
id: num-money
title: Money is an integer of minor units with an explicit rounding rule
tags: numerics, money, decimal
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Money is an integer of minor units with an explicit rounding rule

## Claim

Binary floats lose cents. Rounding half-up twice double-rounds. The currency scale is data.

## Test

Compute tax on a price with two rounding steps. Compare float and decimal.

## Proof

A total that matches the invoice to the cent.

## Failure modes

A float cent error compounds at scale. A banker's rounding choice changes the audit.
