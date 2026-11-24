---
id: crypto-weak-random
title: Predictable randomness is a key recovery bug
tags: crypto, random, predictability
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Predictable randomness is a key recovery bug

## Claim

A token, nonce or key comes from time, a weak PRNG, or a seed reused across processes.

## Test

Collect many outputs. Check the seed source. Try to predict the next value from the timestamp or PID.

## Proof

A predicted token accepted by the server.

## Failure modes

A random-looking string is not proof. Check the generator and the seed.
