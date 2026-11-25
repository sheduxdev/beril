---
id: weak-random-tokens-are-predictable-from-the-clock
title: Weak random tokens are predictable from the clock
tags: crypto, random, token
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/crypto-weak-random.md
status: active
---
# Weak random tokens are predictable from the clock

## Claim

A token built with rand, time, a counter or Math.random can be predicted from a few samples and the server clock.

## Test

Collect twenty tokens. Check length, alphabet and changes over time. Sort by issue time and look for a sequence.

## Proof

A predicted token is accepted.

## Failure modes

A CSPRNG with enough entropy defeats it. A per request server nonce adds noise.
