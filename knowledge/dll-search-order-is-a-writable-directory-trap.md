---
id: dll-search-order-is-a-writable-directory-trap
title: DLL search order is a writable directory trap
tags: win, dll, hijack
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/win-service-acl.md
status: active
---
# DLL search order is a writable directory trap

## Claim

A missing DLL loaded from the application directory, the current directory or PATH takes the attacker copy if that directory is writable.

## Test

Use Process Monitor to find NAME NOT FOUND loads. Check write access on the searched paths. Place a proxy DLL.

## Proof

The DLL loads into the target process.

## Failure modes

Safe DLL search and a full path reduce it. A signed DLL check can block the proxy.
