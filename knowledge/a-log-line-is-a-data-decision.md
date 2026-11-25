---
id: a-log-line-is-a-data-decision
title: A log line is a data decision
tags: design, logging, privacy
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/legal.md, knowledge/ir-cloud.md
status: active
---
# A log line is a data decision

## Claim

Every field written to a log is a field someone can read, export and forget. The log needs a field list and a retention.

## Test

Read the log schema. Mark personal and secret fields. Check the retention and the redaction step.

## Proof

A field list with a retention and a redaction rule.

## Failure modes

A debug log can carry the body. A sampled log can miss the incident.
