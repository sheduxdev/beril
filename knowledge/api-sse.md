---
id: api-sse
title: Server-sent events need per-connection auth
tags: api, sse, stream
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Server-sent events need per-connection auth

## Claim

The event stream authenticates at connect time and never rechecks, or shares a channel across users.

## Test

Open the stream with two accounts. Check events after a role change or logout. Try a reconnect.

## Proof

An event for another user or after logout.

## Failure modes

A public stream is not a leak. A reconnect that reauths is safer.
