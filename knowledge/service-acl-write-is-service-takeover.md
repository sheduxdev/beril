---
id: service-acl-write-is-service-takeover
title: Service ACL write is service takeover
tags: win, service, acl
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/win-service-acl.md
status: active
---
# Service ACL write is service takeover

## Claim

SERVICE_CHANGE_CONFIG or WRITE_DAC on a service lets an attacker change the binary or the account and restart it.

## Test

Read the service DACL. Change the binary path to a payload. Restart and check the context.

## Proof

A payload runs as the service account.

## Failure modes

A protected service or a missing restart right blocks it. A service can be disabled.
