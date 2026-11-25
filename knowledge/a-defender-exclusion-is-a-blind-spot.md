---
id: a-defender-exclusion-is-a-blind-spot
title: A Defender exclusion is a blind spot
tags: win, defender, exclusion
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A Defender exclusion is a blind spot

## Claim

A path, process or extension exclusion lets a payload sit and run without a scan.

## Test

Read the exclusion list with Get-MpPreference. Drop a known test file in an excluded path. Run it.

## Proof

The payload runs with real time protection on.

## Failure modes

A cloud block can still catch a known hash. A tamper protected config needs admin.
