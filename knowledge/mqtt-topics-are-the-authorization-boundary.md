---
id: mqtt-topics-are-the-authorization-boundary
title: MQTT topics are the authorization boundary
tags: ot, mqtt, iot
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# MQTT topics are the authorization boundary

## Claim

A broker that allows a wildcard subscription or a topic write leaks every device message or lets a client impersonate a device.

## Test

Connect with a test client. Subscribe to `#`. Publish to a device topic and read it back.

## Proof

A wildcard read or a device topic write.

## Failure modes

An ACL per topic and a client id check close it. A TLS only broker still needs the ACL.
