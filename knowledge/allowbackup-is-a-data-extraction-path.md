---
id: allowbackup-is-a-data-extraction-path
title: AllowBackup is a data extraction path
tags: mobile, android, backup
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/scan-artifacts.md, labs/mobile
status: active
---
# AllowBackup is a data extraction path

## Claim

`android:allowBackup=true` lets adb or a cloud backup copy the app data, including tokens and databases.

## Test

Read the manifest. Run `adb backup` or the modern backup command. Extract the archive and list the files.

## Proof

A token or a database leaves the device.

## Failure modes

A backup rules file can exclude the sensitive path. A debug only build may behave differently.
