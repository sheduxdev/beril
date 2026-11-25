---
id: rce-proof-climbs-a-ladder-it-does-not-jump-to-a-shell
title: RCE proof climbs a ladder, it does not jump to a shell
tags: rce, proof, method
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# RCE proof climbs a ladder, it does not jump to a shell

## Claim

A changed error is a lead, an arithmetic expansion is evaluation, command output or a unique callback is execution. A report needs the second, not the first.

## Test

Send an interpreter specific arithmetic marker, confirm the literal is absent and the value is present, repeat with a second operator, then send a read only command.

## Proof

Command output tied to the request, or a unique callback with a timestamp.

## Failure modes

The app reflects the payload. The page already contains the result value. A sandbox evaluates math and blocks objects.
