---
id: telematics-is-a-cellular-linux-box
title: Telematics is a cellular Linux box
tags: auto, telematics, cellular
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# Telematics is a cellular Linux box

## Claim

The unit runs a Linux stack with a modem and a CAN bridge. The exposed modem and the debug port are the surface.

## Test

Find the unit and the debug pads. Read the running services. Check the modem and the CAN path.

## Proof

A shell or a CAN frame from the unit.

## Failure modes

A locked modem and a potted board block it. A private APN can hide the modem.
