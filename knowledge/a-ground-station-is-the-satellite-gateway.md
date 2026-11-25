---
id: a-ground-station-is-the-satellite-gateway
title: A ground station is the satellite gateway
tags: sat, ground, gateway
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# A ground station is the satellite gateway

## Claim

The ground segment schedules the passes and sends the commands. A compromise there reaches the spacecraft.

## Test

Map the ground hosts and the pass schedule. Find the command path. Check the operator roles.

## Proof

A command path from the ground to the spacecraft.

## Failure modes

A separate mission network can isolate it. A manual approval can block a command.
