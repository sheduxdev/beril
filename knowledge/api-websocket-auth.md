---
id: api-websocket-auth
title: WebSocket authorization is per message and per channel
tags: api, websocket, auth
confidence: high
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# WebSocket authorization is per message and per channel

## Claim

The handshake checks a token, but a subscribe or join message trusts a channel id from the client.

## Test

Open two sockets with different users. Join the other channel. Send a privileged message.

## Proof

A message or event from another user's channel.

## Failure modes

A public channel is not a leak. A reconnect may reauth.
