---
id: resource-based-delegation-is-a-write-on-the-target
title: Resource based delegation is a write on the target
tags: ad, delegation, rbcd
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ad-acl-path.md
status: active
---
# Resource based delegation is a write on the target

## Claim

Write access to a computer object lets an attacker set the allowed principal and impersonate any user to it.

## Test

Find a computer where you can write `msDS-AllowedToActOnBehalfOfOtherIdentity`. Set it, request S4U, clean up.

## Proof

A service ticket as admin on the target.

## Failure modes

A missing SPN blocks the path. Some hosts have the flag locked by policy.
