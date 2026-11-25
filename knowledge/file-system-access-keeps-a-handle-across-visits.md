---
id: file-system-access-keeps-a-handle-across-visits
title: File System Access keeps a handle across visits
tags: browser, file-system, api
confidence: low
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# File System Access keeps a handle across visits

## Claim

A stored directory handle can read and write files the user granted, and the grant can persist.

## Test

Request a directory handle. Reload and query permission. Read a file after the reload.

## Proof

A file read after a new page load.

## Failure modes

A permission reset clears it. A read only grant blocks writes.
