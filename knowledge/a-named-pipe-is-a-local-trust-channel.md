---
id: a-named-pipe-is-a-local-trust-channel
title: A named pipe is a local trust channel
tags: win, named-pipe, relay
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/win-token-privileges.md
status: active
---
# A named pipe is a local trust channel

## Claim

A privileged service that connects to a predictable pipe can be coerced and relayed or impersonated.

## Test

List pipes and their DACLs. Find a client that connects as SYSTEM. Run a pipe relay or a spoofed server.

## Proof

A SYSTEM token or an authenticated relay.

## Failure modes

A pipe with a random suffix is harder. A signing requirement blocks relay.
