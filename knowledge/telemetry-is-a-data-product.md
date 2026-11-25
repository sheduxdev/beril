---
id: telemetry-is-a-data-product
title: Telemetry is a data product
tags: sat, telemetry, data
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# Telemetry is a data product

## Claim

The telemetry carries the health and the state. A decode gives the mode, the temperatures and the fault flags.

## Test

Read the field list and the scale. Decode one frame. Map the mode bits.

## Proof

A decoded field with the scale.

## Failure modes

A compressed or an encrypted frame blocks it. A custom scale can mislead.
