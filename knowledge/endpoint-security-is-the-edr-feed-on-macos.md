---
id: endpoint-security-is-the-edr-feed-on-macos
title: Endpoint Security is the EDR feed on macOS
tags: macos, endpoint-security, edr
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-edr.md
status: active
---
# Endpoint Security is the EDR feed on macOS

## Claim

The ES framework delivers process, file and network events to a signed client with the entitlement. The feed is the detection surface.

## Test

List the ES clients. Read the event types. Generate one event and find it in the log.

## Proof

An event with the process and the path.

## Failure modes

A client with a narrow event mask misses it. A user can approve a client.
