---
id: the-central-gateway-is-the-network-boundary
title: The central gateway is the network boundary
tags: auto, gateway, network
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# The central gateway is the network boundary

## Claim

The gateway routes between CAN, LIN, FlexRay and Ethernet. A frame that crosses a domain is the interesting one.

## Test

Map the buses and the gateway. Capture both sides. Find a frame that crosses.

## Proof

A frame on the far side from the source.

## Failure modes

A gateway can filter by id. A domain can be isolated in a bench setup.
