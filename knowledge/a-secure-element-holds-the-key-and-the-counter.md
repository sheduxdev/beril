---
id: a-secure-element-holds-the-key-and-the-counter
title: A secure element holds the key and the counter
tags: hardware, secure-element, key
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-update-sign.md
status: active
---
# A secure element holds the key and the counter

## Claim

A secure element performs the crypto without exposing the key, and a monotonic counter blocks a rollback.

## Test

Read the part number. Identify the protocol. Ask for a signature. Try an old image after a counter increment.

## Proof

A signature from the element and a counter refusal.

## Failure modes

A poorly configured element can expose a debug command. A missing counter allows rollback.
