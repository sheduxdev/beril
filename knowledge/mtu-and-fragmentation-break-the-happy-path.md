---
id: mtu-and-fragmentation-break-the-happy-path
title: MTU and fragmentation break the happy path
tags: network, mtu, frag
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-toolkit.md
status: active
---
# MTU and fragmentation break the happy path

## Claim

A tunnel or a VLAN lowers the usable MTU. Large packets drop while small ones pass, which looks like an app bug.

## Test

Send a large ping with the DF bit. Lower the size until it passes. Compare across the path.

## Proof

A size threshold where the drop starts.

## Failure modes

PMTUD can fix it. A proxy can reassemble.
