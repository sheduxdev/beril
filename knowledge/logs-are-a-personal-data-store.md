---
id: logs-are-a-personal-data-store
title: Logs are a personal data store
tags: privacy, logs, pii
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/legal.md, knowledge/ir-cloud.md
status: active
---
# Logs are a personal data store

## Claim

Access logs, request bodies and error traces carry emails, tokens and IPs. A log pipeline without a retention rule grows a shadow database.

## Test

Sample the logs. Mark every personal field. Check the retention and the access list.

## Proof

A retention rule and a redaction step for the marked fields.

## Failure modes

A short retention lowers the risk. A debug log can be forgotten for years.
