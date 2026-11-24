---
id: detection-threatintel
title: Threat intel ages and IOCs are easy to rotate
tags: detection, intel, ioc
confidence: medium
updated: 2026-11-24
uses: 0
sources: labs/detection
status: active
---
# Threat intel ages and IOCs are easy to rotate

## Claim

A hash or domain is a weak rule. Behavior and infrastructure patterns last longer.

## Test

Compare an IOC rule with a behavior rule on the same sample. Age the intel and retest.

## Proof

A behavior rule that still catches a rotated sample.

## Failure modes

A public IOC can be a false positive. Check the intel source.
