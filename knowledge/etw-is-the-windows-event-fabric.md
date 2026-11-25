---
id: etw-is-the-windows-event-fabric
title: ETW is the Windows event fabric
tags: wink, etw, telemetry
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-edr.md
status: active
---
# ETW is the Windows event fabric

## Claim

Providers emit events to a session and a consumer. A missing provider or a disabled session is a blind spot.

## Test

List the sessions and the providers. Enable a security provider. Generate an event and read it.

## Proof

An event with the provider and the process.

## Failure modes

A patched provider can lie. A high volume session drops events.
