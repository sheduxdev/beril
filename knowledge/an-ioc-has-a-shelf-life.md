---
id: an-ioc-has-a-shelf-life
title: An IOC has a shelf life
tags: ti, ioc, lifecycle
confidence: high
updated: 2026-11-26
uses: 0
sources: references/scoring.md
status: active
---
# An IOC has a shelf life

## Claim

A hash is stable and a domain decays. An indicator without a first seen and a last seen date is a guess.

## Test

Read the record. Check the dates, the source and the confidence. Compare with a current sandbox run.

## Proof

A dated indicator with a source and a state.

## Failure modes

A long lived infrastructure can last. A fast flux domain changes hourly.
