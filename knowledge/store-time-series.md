---
id: store-time-series
title: A time-series store trades resolution for retention
tags: storage, time-series, downsampling
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A time-series store trades resolution for retention

## Claim

Raw points age into rollups. The rollup interval sets the query resolution and the storage cost.

## Test

Write a week of points. Age past the raw window. Query the average.

## Proof

A rollup that answers the query at the promised resolution.

## Failure modes

A rollup without the min/max loses spikes. A retention without a downsampling job deletes history.
