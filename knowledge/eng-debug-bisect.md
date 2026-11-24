---
id: eng-debug-bisect
title: Bisect the space, not the code
tags: engineering, debugging, bisect
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Bisect the space, not the code

## Claim

The failing input, commit, config or layer can be narrowed by halving. Change one variable at a time.

## Test

Reproduce. List the variables. Halve the commits or inputs. Keep a log.

## Proof

A minimal failing case and the first bad change.

## Failure modes

A cache can make a bisect lie. Clear state between runs.
