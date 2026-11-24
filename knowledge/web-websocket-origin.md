---
id: web-websocket-origin
title: WebSocket handshakes skip the same-origin policy
tags: web, websocket, origin
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# WebSocket handshakes skip the same-origin policy

## Claim

The upgrade handler authenticates the cookie but not the Origin, or accepts a token in the query.

## Test

Open a socket from a cross-origin page with the victim cookie. Send one privileged message.

## Proof

A cross-origin socket performs an authenticated action.

## Failure modes

A socket that requires a token in the first message may still be safe. Check message auth.
