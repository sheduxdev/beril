---
id: a-dictionary-crosses-magic-checks
title: A dictionary crosses magic checks
tags: fuzz, dictionary, magic
confidence: high
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A dictionary crosses magic checks

## Claim

A parser that checks a magic value or a keyword is unreachable by random bytes without a dictionary token.

## Test

Read the magic and the keywords. Add them to the dictionary. Compare the edge count with and without.

## Proof

New edges after the dictionary is added.

## Failure modes

A dictionary can bloat the input. A checksum still blocks the path.
