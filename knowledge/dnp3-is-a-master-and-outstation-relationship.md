---
id: dnp3-is-a-master-and-outstation-relationship
title: DNP3 is a master and outstation relationship
tags: ot, dnp3, scada
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# DNP3 is a master and outstation relationship

## Claim

DNP3 has link layer addresses, an application function and optional secure auth. A direct outstation write skips the master.

## Test

Map the master and the outstation addresses. Read the class 0 data. Send one direct operate for a safe point.

## Proof

A point change accepted by the outstation.

## Failure modes

Secure authentication can require a challenge. A master can overwrite the point later.
