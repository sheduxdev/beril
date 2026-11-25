---
id: printnightmare-is-a-spooler-driver-load
title: PrintNightmare is a spooler driver load
tags: win, printnightmare, spooler
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# PrintNightmare is a spooler driver load

## Claim

The spooler loads a driver from a remote path as SYSTEM when the point and print policy allows it.

## Test

Check the spooler service and the policy. Run the print driver check with a remote DLL. Watch the load.

## Proof

The DLL loads as SYSTEM.

## Failure modes

The policy can require a signed driver. A disabled spooler closes it.
