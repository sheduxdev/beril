---
id: the-object-manager-is-a-namespace-with-a-dacl
title: The object manager is a namespace with a DACL
tags: wink, object-manager, acl
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/win-token-privileges.md
status: active
---
# The object manager is a namespace with a DACL

## Claim

A named object has a path and a security descriptor. A weak DACL lets another user open or duplicate a handle.

## Test

List the object directory. Read the security descriptor. Open with a low privilege token.

## Proof

A handle from the weaker token.

## Failure modes

A private namespace hides the object. A protected process blocks the open.
