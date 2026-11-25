---
id: a-writable-systemd-unit-is-a-service-takeover
title: A writable systemd unit is a service takeover
tags: linux, systemd, privilege
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A writable systemd unit is a service takeover

## Claim

Write access to a unit file, a drop in or the unit directory lets an attacker change ExecStart and restart the service.

## Test

List units and their paths. Check write rights. Add a drop in with a command. daemon-reload and restart.

## Proof

The command runs as the service user.

## Failure modes

A read only unit in a protected path holds. A masked unit can block the restart.
