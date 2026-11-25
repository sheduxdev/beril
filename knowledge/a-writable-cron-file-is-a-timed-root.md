---
id: a-writable-cron-file-is-a-timed-root
title: A writable cron file is a timed root
tags: linux, cron, privilege
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A writable cron file is a timed root

## Claim

A script or a directory in a root cron job that a user can write runs the user code as root at the next tick.

## Test

Read `/etc/cron*`, user crontabs and systemd timers. Check write rights on every path. Place a marker.

## Proof

The marker runs as root.

## Failure modes

A root owned directory with no write is safe. A timer can be disabled.
