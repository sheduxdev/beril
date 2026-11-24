---
id: crypto-nonce
title: A nonce is unique per key by construction or by count
tags: cryptography, nonce, collision
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A nonce is unique per key by construction or by count

## Claim

A counter is exact; random has a birthday bound. The nonce width bounds the safe message count.

## Test

Generate random 96-bit nonces for a workload. Compute the collision probability at the message count.

## Proof

A nonce scheme with a stated bound or an exact counter.

## Failure modes

A 64-bit random nonce collides far earlier than expected. A counter that resets on restart repeats.
