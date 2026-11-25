---
id: modbus-has-no-auth-and-no-sequence
title: Modbus has no auth and no sequence
tags: ot, modbus, plc
confidence: high
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# Modbus has no auth and no sequence

## Claim

Modbus TCP carries a unit id, a function code and data with no session. Any host that can reach the port can read or write a register.

## Test

Read the unit id and the function map. Read a holding register. Write one safe register and read it back.

## Proof

A changed register from a write.

## Failure modes

A gateway can filter function codes. A PLC can protect a register in logic.
