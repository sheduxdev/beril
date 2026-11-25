---
id: a-c2-profile-is-a-traffic-shape
title: A C2 profile is a traffic shape
tags: red, c2, traffic
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-beacon.md
status: active
---
# A C2 profile is a traffic shape

## Claim

The URI, the header order, the jitter and the message size are the profile. A profile that looks like the local traffic survives longer.

## Test

Capture the profile against a known app. Compare the fields and the timing. Tune one field and re capture.

## Proof

A profile that matches the cover traffic on the field list.

## Failure modes

A deep packet inspector can still see the beacon. A cover app update changes the shape.
