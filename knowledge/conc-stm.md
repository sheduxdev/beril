---
id: conc-stm
title: STM retries a transaction when a read value changed
tags: concurrency, stm, transaction
confidence: low
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# STM retries a transaction when a read value changed

## Claim

The runtime logs reads, validates on commit, and retries on conflict. A side effect inside the transaction repeats.

## Test

Conflict two transactions on the same variable. Count the retries and the side effects.

## Proof

A commit with side effects applied once.

## Failure modes

An IO inside a transaction repeats on retry. A long transaction starves under contention.
