---
id: api-partial-update
title: PATCH needs a rule for absent, null and empty
tags: api-design, patch, merge
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# PATCH needs a rule for absent, null and empty

## Claim

Absent means unchanged, null means clear, empty means set empty. A merge patch cannot express all three.

## Test

Send the three cases. Check the stored value.

## Proof

A documented and tested semantic for each case.

## Failure modes

A merge patch that cannot clear a field. A full replace that wipes an omitted field.
