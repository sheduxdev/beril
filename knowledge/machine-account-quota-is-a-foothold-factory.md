---
id: machine-account-quota-is-a-foothold-factory
title: Machine account quota is a foothold factory
tags: ad, machine-account, quota
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Machine account quota is a foothold factory

## Claim

The default `ms-DS-MachineAccountQuota` lets any user join ten computers, which provides SPNs and computer object control.

## Test

Read the quota. Create a machine account with impacket or PowerMad. Check the created object and its SPN.

## Proof

A computer object you own exists in the domain.

## Failure modes

A quota of zero blocks it. Some hardening removes the default.
