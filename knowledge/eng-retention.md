---
id: eng-retention
title: Retention is a deletion clock with an owner
tags: engineering, retention, data
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Retention is a deletion clock with an owner

## Claim

Each dataset has a legal and product lifetime. Archival is not deletion.

## Test

List datasets and retention. Check the archive and the delete job.

## Proof

A deletion after the window with evidence.

## Failure modes

An archive nobody can read is not retention. A backup keeps deleted data alive.
