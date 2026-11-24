---
id: comp-debug-info
title: Debug info maps machine state to source
tags: compiler, dwarf, debug
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Debug info maps machine state to source

## Claim

DWARF line tables and variable locations let a debugger show source. Optimization moves and removes both.

## Test

Break on an inlined function. Check the line and the variable availability.

## Proof

A correct source line or an explicit optimized-out marker.

## Failure modes

A variable optimized into a register may be unavailable. A wrong line misleads.
