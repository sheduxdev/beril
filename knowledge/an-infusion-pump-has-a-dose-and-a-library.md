---
id: an-infusion-pump-has-a-dose-and-a-library
title: An infusion pump has a dose and a library
tags: med, infusion, dose
confidence: low
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# An infusion pump has a dose and a library

## Claim

The pump trusts a drug library and a dose. A library write or a manual rate change alters the delivered volume.

## Test

Read the library source and the lock. Change one rate in a lab. Compare the delivered volume.

## Proof

A delivered volume change.

## Failure modes

A hard limit can clamp the rate. A pump can require a confirmation.
