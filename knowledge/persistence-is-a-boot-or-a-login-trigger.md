---
id: persistence-is-a-boot-or-a-login-trigger
title: Persistence is a boot or a login trigger
tags: malware, persistence, boot
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-lolbins.md
status: active
---
# Persistence is a boot or a login trigger

## Claim

Run keys, services, scheduled tasks, WMI subscriptions and startup folders are triggers. The location names the privilege and the detection.

## Test

Diff the autoruns before and after the run. Read the created artifact. Check the trigger and the owner.

## Proof

A new autorun entry with the payload path.

## Failure modes

A fileless persistence lives in the registry only. A signed task can look clean.
