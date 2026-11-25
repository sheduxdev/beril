---
id: obd-is-a-legal-diagnostic-port
title: OBD is a legal diagnostic port
tags: auto, obd, diagnostic
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# OBD is a legal diagnostic port

## Claim

The OBD port exposes the bus and a set of standard PIDs. It is the easiest physical entry in a car.

## Test

Connect a tester. Read the supported PIDs. Capture the bus and identify the non diagnostic traffic.

## Proof

A live PID and a captured frame.

## Failure modes

A gateway can isolate the port. A locked car can cut the power.
