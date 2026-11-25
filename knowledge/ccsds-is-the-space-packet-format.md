---
id: ccsds-is-the-space-packet-format
title: CCSDS is the space packet format
tags: sat, ccsds, packet
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# CCSDS is the space packet format

## Claim

The CCSDS packet has an APID, a sequence count and a length. The APID names the instrument and the service.

## Test

Read the packet header in a capture. Map the APIDs. Decode one payload.

## Proof

A decoded APID and payload.

## Failure modes

An encrypted payload blocks the decode. A custom secondary header can hide the fields.
