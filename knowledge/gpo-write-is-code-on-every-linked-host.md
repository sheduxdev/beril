---
id: gpo-write-is-code-on-every-linked-host
title: GPO write is code on every linked host
tags: ad, gpo, code
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# GPO write is code on every linked host

## Claim

Control of a GPO linked to an OU gives a logon or startup script on every computer in that OU.

## Test

Find a GPO where you can edit the settings or the link. Add a run once script. Wait for a refresh or force it on a lab host.

## Proof

The script runs as SYSTEM on a linked host.

## Failure modes

Security filtering can narrow the scope. A disabled link does nothing.
