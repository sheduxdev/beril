---
id: multi-tenant-needs-the-tenant-in-the-key
title: Multi tenant needs the tenant in the key
tags: design, multi-tenant, cache
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ai-rag-tenant-filter.md, knowledge/web-cache-key-unkeyed-input.md
status: active
---
# Multi tenant needs the tenant in the key

## Claim

A cache, a job, a search index and a queue worker that omit the tenant id can return another tenant's data.

## Test

Run two tenants. Compare the key shapes for the cache, the job payload and the index document. Find one without the tenant.

## Proof

A cross tenant read through the shared component.

## Failure modes

A per tenant instance removes the key question. A global public object can be shared.
