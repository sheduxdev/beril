---
id: medical-mqtt-is-a-device-bus
title: Medical MQTT is a device bus
tags: med, mqtt, device
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# Medical MQTT is a device bus

## Claim

A device topic carries observations and commands. A wildcard subscription or a command write changes the device state.

## Test

Connect with a test client. Subscribe to `#`. Publish a command topic and read the ack.

## Proof

A command accepted by the device.

## Failure modes

An ACL per topic closes it. A TLS only broker still needs the ACL.
