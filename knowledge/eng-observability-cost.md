---
id: eng-observability-cost
title: Telemetry is a sampled product
tags: engineering, observability, cost
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Telemetry is a sampled product

## Claim

Cardinality and volume drive cost. Sample traces, aggregate metrics and keep logs structured.

## Test

Measure ingest by label. Drop a high-cardinality label. Compare the bill and the answers.

## Proof

A lower cost with the incident questions still answerable.

## Failure modes

A metric with a user id is a log. A sampled error can disappear.
