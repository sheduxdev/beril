---
id: bacnet-is-a-building-broadcast-protocol
title: BACnet is a building broadcast protocol
tags: ot, bacnet, building
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# BACnet is a building broadcast protocol

## Claim

BACnet uses object identifiers and services over UDP with little auth. A read property or a write property crosses the building.

## Test

List the device object and the analog inputs. Read one. Write a safe setpoint and read it back.

## Proof

A changed setpoint.

## Failure modes

A BBMD and a firewall can segment it. A write can be overridden by a schedule.
