---
id: a-content-provider-is-a-sql-surface
title: A content provider is a SQL surface
tags: android, provider, sql
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-deep-link-bridge.md
status: active
---
# A content provider is a SQL surface

## Claim

A provider exposes query, insert and call to other apps. A missing read permission or a projection injection reaches the database.

## Test

Read the manifest and the provider paths. Query with a projection and a selection. Try a path traversal in the uri.

## Proof

A row or a file outside the app.

## Failure modes

A signature permission closes it. A provider can be app internal only.
