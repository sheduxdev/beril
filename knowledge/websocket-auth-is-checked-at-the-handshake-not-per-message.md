---
id: websocket-auth-is-checked-at-the-handshake-not-per-message
title: WebSocket auth is checked at the handshake, not per message
tags: api, websocket, auth
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/api-websocket-auth.md, knowledge/web-websocket-origin.md
status: active
---
# WebSocket auth is checked at the handshake, not per message

## Claim

If the token is only checked when the socket opens, a role change or logout does not affect the live socket.

## Test

Open a socket with a low privilege token. Change the role or log out. Send a privileged message on the same socket.

## Proof

The message succeeds after the role change or logout.

## Failure modes

A server that rechecks per message is safe. Short lived sockets limit the window.
