---
id: uds-is-the-automotive-diagnostic-protocol
title: UDS is the automotive diagnostic protocol
tags: auto, uds, diagnostic
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# UDS is the automotive diagnostic protocol

## Claim

UDS services read and write the ECU. A session change and a security access unlock the write services.

## Test

Read the supported services with a tester. Request a session. Try the security access seed and key.

## Proof

A write service accepted after unlock.

## Failure modes

A locked ECU needs a seed key algorithm. A gateway can filter the service.
