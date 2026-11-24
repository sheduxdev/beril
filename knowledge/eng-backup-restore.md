---
id: eng-backup-restore
title: An untested backup is a hope
tags: engineering, backup, restore
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# An untested backup is a hope

## Claim

The restore path, the encryption key and the recovery time are part of the backup. Test the restore, not the backup job.

## Test

Restore a random backup into an isolated environment. Measure the time. Check the key.

## Proof

A restored dataset with a measured RTO.

## Failure modes

A successful backup job says nothing about the restore. A key lost with the host is data loss.
