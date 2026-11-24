---
id: process-duplicate-search
title: Search duplicates before writing a report
tags: process, triage, duplicate
confidence: high
updated: 2026-11-24
uses: 0
sources: references/claude-bughunter.md
status: active
---
# Search duplicates before writing a report

## Claim

A valid bug can be a duplicate. The search needs the endpoint, the parameter and the class, not the title only.

## Test

Search the program, disclosed reports, changelog and issue tracker. Check the fix and the date.

## Proof

A duplicate check with sources and a decision to proceed or drop.

## Failure modes

A closed report can still be a new variant. A different endpoint can be the same root cause.
