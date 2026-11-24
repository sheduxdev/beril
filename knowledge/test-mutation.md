---
id: test-mutation
title: Mutation testing measures whether a test would notice a change
tags: testing, mutation, coverage
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Mutation testing measures whether a test would notice a change

## Claim

The tool flips an operator and checks a test failure. A surviving mutant is a gap in assertion strength.

## Test

Run mutations on a module. Read the surviving mutants.

## Proof

A mutation score with the survivors explained.

## Failure modes

Line coverage stays high while mutants survive. An equivalent mutant is a false alarm.
