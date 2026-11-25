---
id: a-launchd-job-is-persistence-and-privilege
title: A launchd job is persistence and privilege
tags: macos, launchd, persistence
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mal-persistence.md
status: active
---
# A launchd job is persistence and privilege

## Claim

A plist in a LaunchAgents or LaunchDaemons path runs at login or boot. A writable plist is a code path.

## Test

List the jobs and their paths. Check the write rights. Add a marker command. load or reboot.

## Proof

The marker runs at the trigger.

## Failure modes

A SIP protected path holds. A job can be disabled by a user.
