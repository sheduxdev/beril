---
id: token-duplication-needs-sedebugprivilege
title: Token duplication needs SeDebugPrivilege
tags: win, token, privilege
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/win-token-privileges.md
status: active
---
# Token duplication needs SeDebugPrivilege

## Claim

A process with SeDebugPrivilege can open a SYSTEM token and run a new process with it.

## Test

Check whoami /priv. Open a SYSTEM process with a token tool. Duplicate and impersonate. Spawn a shell.

## Proof

A new process runs as SYSTEM.

## Failure modes

A protected process blocks the open. The privilege can be removed from the admin token.
