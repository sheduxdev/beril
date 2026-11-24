---
id: db-vacuum
title: Vacuum reclaims versions and freezes old transaction ids
tags: database, vacuum, bloat
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Vacuum reclaims versions and freezes old transaction ids

## Claim

Dead tuples are removed after no snapshot needs them. Autovacuum lags under load and bloat grows.

## Test

Measure dead tuples and table bloat. Check autovacuum settings and the oldest xid.

## Proof

A vacuum that lowers dead tuples and freezes before wraparound.

## Failure modes

A long transaction blocks cleanup. A freeze too late risks wraparound.
