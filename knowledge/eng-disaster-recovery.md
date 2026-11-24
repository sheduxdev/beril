---
id: eng-disaster-recovery
title: DR is RTO, RPO and a rehearsal
tags: engineering, disaster, recovery
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# DR is RTO, RPO and a rehearsal

## Claim

The recovery time and the acceptable data loss are business decisions. A runbook without a rehearsal is a guess.

## Test

Define RTO and RPO. Run a game day. Record the gaps.

## Proof

A rehearsal that meets both targets.

## Failure modes

 A full failover without a rollback is risky. A warm standby can be cold in practice.
