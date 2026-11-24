---
id: eng-frontend-state
title: Client state and server state are different caches
tags: engineering, frontend, state
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Client state and server state are different caches

## Claim

Server data has a source of truth and a staleness policy. UI state is local and ephemeral.

## Test

Name each state. Put server data in a query cache with invalidation. Keep UI state local.

## Proof

A refetch after mutation and a local toggle.

## Failure modes

Copying server data into a global store creates two truths.
