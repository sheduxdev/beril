---
id: an-app-container-is-a-data-boundary
title: An app container is a data boundary
tags: ios, container, data
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# An app container is a data boundary

## Claim

The container holds the app data and the keychain items are separate. A backup and a shared group cross the container.

## Test

List the container and the group. Read the file protection. Check the backup state.

## Proof

A file readable outside the app process.

## Failure modes

A protected file needs the device unlocked. A group container is intentional sharing.
