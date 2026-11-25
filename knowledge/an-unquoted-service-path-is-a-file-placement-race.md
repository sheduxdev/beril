---
id: an-unquoted-service-path-is-a-file-placement-race
title: An unquoted service path is a file placement race
tags: win, service, path
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/win-service-acl.md
status: active
---
# An unquoted service path is a file placement race

## Claim

A service path with a space and no quotes searches each prefix, so a writable directory earlier in the path wins.

## Test

Read the ImagePath. Check write rights on each prefix directory. Place a binary at the first writable prefix. Restart.

## Proof

The placed binary runs as the service account.

## Failure modes

The service binary can be in a protected path. A quoted path closes it.
