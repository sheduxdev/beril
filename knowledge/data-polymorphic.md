---
id: data-polymorphic
title: A polymorphic reference trades integrity for flexibility
tags: data-modeling, polymorphic, constraints
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A polymorphic reference trades integrity for flexibility

## Claim

A type column plus an id cannot be a foreign key. An exclusive arc or a join table restores it.

## Test

Insert a reference with a wrong type. Check whether the database rejects it.

## Proof

A constraint that rejects an orphan reference.

## Failure modes

A type column without a check drifts. An exclusive arc adds nullable columns.
