---
id: s7comm-needs-a-rack-and-a-slot
title: S7comm needs a rack and a slot
tags: ot, s7, siemens
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# S7comm needs a rack and a slot

## Claim

The S7 session starts with a COTP connection to a rack and slot, then a setup communication. The address is part of the request.

## Test

Identify the CPU and the rack. Connect with a known client. Read one data block before a write.

## Proof

A read block from the PLC.

## Failure modes

A protected CPU can require a password. A firewall can allow only one master.
