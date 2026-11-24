---
id: eng-multi-tenancy
title: Multi-tenancy is isolation plus noisy-neighbor control
tags: engineering, multi-tenant, isolation
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Multi-tenancy is isolation plus noisy-neighbor control

## Claim

Tenant id must be enforced at the data boundary, and a single tenant must not starve the rest.

## Test

Query as tenant A with a tenant B id. Load one tenant and measure another.

## Proof

A cross-tenant read fails and a noisy tenant is rate-limited.

## Failure modes

A tenant filter in the UI is not a data boundary.
