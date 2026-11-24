---
id: linux-cron-systemd
title: Scheduled jobs inherit a weak PATH or writable unit
tags: linux, privesc, cron, systemd
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Scheduled jobs inherit a weak PATH or writable unit

## Claim

A root cron job runs a script from a writable directory, or a systemd unit points to a writable binary.

## Test

List cron, timers and units. Check file ownership and PATH. Wait for the schedule or trigger the timer.

## Proof

A root command from a file you control.

## Failure modes

A writable script that root never runs is not a finding. Check the schedule.
