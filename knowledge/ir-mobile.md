---
id: ir-mobile
title: Mobile triage starts with the backup and the sysdiagnose
tags: ir, mobile, ios
confidence: low
updated: 2026-11-25
uses: 0
sources: references/mobile-reverse.md
status: active
---
# Mobile triage starts with the backup and the sysdiagnose

## Claim

iOS sysdiagnose and Android bug reports hold logs, databases and app state. A backup exposes app data.

## Test

Collect the sysdiagnose or bug report. Check the backup and shared containers. Correlate with the account.

## Proof

An app event or file with a timestamp.

## Failure modes

A backup may exclude protected files. A rooted device changes the picture.
