---
id: coupons-need-stacking-reuse-and-scope-rules
title: Coupons need stacking, reuse and scope rules
tags: web, logic, coupon
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Coupons need stacking, reuse and scope rules

## Claim

A coupon applied twice, combined with another or used outside its product scope turns a discount into a payout.

## Test

Apply one coupon twice, stack two, use it on an excluded product and on a negative line.

## Proof

The total drops below the intended floor or the coupon survives the second use.

## Failure modes

A per user ledger prevents reuse. Some stacks are intended.
