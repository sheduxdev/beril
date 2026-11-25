---
id: zigbee-needs-the-network-key
title: Zigbee needs the network key
tags: ot, zigbee, iot
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# Zigbee needs the network key

## Claim

The network key protects the mesh. A default or a sniffed key lets an attacker join and send frames.

## Test

Capture the join and the key transport in a lab. Try the default key. Join and read a frame.

## Proof

A joined device and a valid frame.

## Failure modes

Install code joining blocks a default key. A coordinator allowlist limits the join.
