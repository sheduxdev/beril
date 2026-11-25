---
id: a-price-calculated-in-the-client-is-a-suggestion
title: A price calculated in the client is a suggestion
tags: web, logic, price
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md, references/specialist-program.md
status: active
---
# A price calculated in the client is a suggestion

## Claim

If the total, discount or currency arrives from the browser and the server does not recompute it, the client sets the price.

## Test

Change the amount, the currency and the discount field in the last request. Compare the charged total.

## Proof

The order total differs from the listed price.

## Failure modes

A server side recalculation ignores the field. A payment provider can be the real check.
