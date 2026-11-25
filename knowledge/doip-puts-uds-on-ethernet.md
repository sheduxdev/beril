---
id: doip-puts-uds-on-ethernet
title: DoIP puts UDS on Ethernet
tags: auto, doip, ethernet
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# DoIP puts UDS on Ethernet

## Claim

The DoIP header carries the logical address and the payload type. A routing activation opens the UDS channel.

## Test

Find the DoIP port and the addresses. Send a routing activation. Send one UDS read.

## Proof

A UDS response over DoIP.

## Failure modes

A gateway can require a TLS or a tester address. A firewall can block the port.
