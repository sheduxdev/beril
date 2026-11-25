---
id: gps-spoofing-is-a-time-and-position-attack
title: GPS spoofing is a time and position attack
tags: sat, gps, spoof
confidence: low
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-radio.md
status: active
---
# GPS spoofing is a time and position attack

## Claim

A receiver that trusts the signal without the signature can be moved or time shifted. Many systems use it for time only.

## Test

Read the receiver and the use. Compare the time with a second source. Try a replay in a shielded lab.

## Proof

A position or time shift from the injected signal.

## Failure modes

A multi constellation receiver and a holdover oscillator resist it. A shielded lab is needed.
