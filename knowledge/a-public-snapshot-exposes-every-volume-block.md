---
id: a-public-snapshot-exposes-every-volume-block
title: A public snapshot exposes every volume block
tags: cloud, snapshot, storage
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-iam-wildcard.md
status: active
---
# A public snapshot exposes every volume block

## Claim

A snapshot shared publicly can be restored in another account and mounted, including deleted files and secrets.

## Test

Check the snapshot permissions. Restore it in a lab account. Mount and list the filesystem.

## Proof

A file from the source volume is readable.

## Failure modes

An encrypted snapshot needs the KMS key, which can also be shared. A public AMI is a different object.
