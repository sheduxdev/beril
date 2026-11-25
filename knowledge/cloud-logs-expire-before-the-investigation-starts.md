---
id: cloud-logs-expire-before-the-investigation-starts
title: Cloud logs expire before the investigation starts
tags: ir, cloud, retention
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-cloud.md
status: active
---
# Cloud logs expire before the investigation starts

## Claim

Default retention can be 7 to 90 days, so the window may close while the host is still being contained.

## Test

Read the retention per log source. Export the relevant window first. Check the audit log for the actor actions.

## Proof

An export with a hash and a time range.

## Failure modes

An org can have long retention. A missing source cannot be exported.
