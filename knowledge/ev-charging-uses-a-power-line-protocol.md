---
id: ev-charging-uses-a-power-line-protocol
title: EV charging uses a power line protocol
tags: auto, charging, plc
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# EV charging uses a power line protocol

## Claim

The charging session runs a PLC and a higher level protocol. The vehicle and the charger negotiate current and state.

## Test

Read the connector and the pilot signal. Capture the PLC. Identify the state transitions.

## Proof

A captured state transition.

## Failure modes

A bench charger is needed. A proprietary stack hides the layer.
