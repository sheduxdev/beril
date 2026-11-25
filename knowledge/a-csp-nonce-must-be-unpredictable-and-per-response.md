---
id: a-csp-nonce-must-be-unpredictable-and-per-response
title: A CSP nonce must be unpredictable and per response
tags: browser, csp, nonce
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-csp-bypass.md
status: active
---
# A CSP nonce must be unpredictable and per response

## Claim

A reused, short or static nonce lets an injected script carry the valid value. A base tag can also move relative script loads.

## Test

Load two responses and compare the nonce. Inject a script with the same nonce. Try a base tag before a relative script.

## Proof

The injected script runs.

## Failure modes

A strict dynamic policy and a base-uri directive close it. A nonce with enough entropy holds.
