---
id: web-postmessage
title: postMessage is a bug when the receiver trusts any origin or sends to any origin
tags: web, postmessage, client-side
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# postMessage is a bug when the receiver trusts any origin or sends to any origin

## Claim

A listener does not check event.origin, or a sender uses targetOrigin '*'. A cross-origin page can read or trigger an action.

## Test

Find listeners. Send a message from an attacker page with a distinctive payload. Try targetOrigin '*' on the sender.

## Proof

A cross-origin message changes state or leaks data.

## Failure modes

A listener that validates the origin is safe. A message with no sensitive action is low.
