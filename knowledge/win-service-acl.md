---
id: win-service-acl
title: A weak service ACL is local privilege escalation
tags: windows, privesc, service
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# A weak service ACL is local privilege escalation

## Claim

A service binary or its directory is writable by a low-privilege user, or the service path is unquoted.

## Test

Check service ACLs and binary paths. Look for unquoted paths with spaces. Replace the binary and restart if allowed.

## Proof

A shell as the service account, usually SYSTEM.

## Failure modes

A writable directory is not enough if the binary is signed and locked. Restart rights matter.
