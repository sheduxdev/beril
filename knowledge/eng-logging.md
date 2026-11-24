---
id: eng-logging
title: Log the decision, not the whole world
tags: engineering, logging, observability
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Log the decision, not the whole world

## Claim

A log line should answer what happened and what to do. Request ids, actor, resource and outcome make it useful.

## Test

Read a log from a failed request. Can you reconstruct the decision?

## Proof

A log that reconstructs the request without the source.

## Failure modes

PII in logs is a liability. Unstructured logs are hard to query.
