---
id: api-webhook-signature
title: A webhook without HMAC is an unauthenticated write
tags: api, webhook, hmac
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# A webhook without HMAC is an unauthenticated write

## Claim

The receiver trusts the body or a static token, or verifies HMAC without a timestamp and replay window.

## Test

Capture a delivery. Replay it. Change the body. Test a stale timestamp.

## Proof

A replayed or modified event changes state.

## Failure modes

An HMAC that covers only part of the body may still be bypassable. Timing-safe comparison matters.
