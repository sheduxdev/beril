---
id: db-corruption
title: Corruption is detected by checksums and repaired from a copy
tags: database, corruption, checksum
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Corruption is detected by checksums and repaired from a copy

## Claim

A page checksum failure marks the page. The repair source is a replica, a backup or a WAL replay.

## Test

Corrupt a page file. Read the table. Check the error and the repair.

## Proof

A detected page and a repaired row.

## Failure modes

A full-page write without checksums hides a torn page. A repair from a corrupt replica spreads it.
