---
id: command-injection-depends-on-the-quote-context
title: Command injection depends on the quote context
tags: rce, cmdi, shell
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md, labs/rce
status: active
---
# Command injection depends on the quote context

## Claim

The separator, the quote and the shell decide the payload. A value inside double quotes needs a different escape than an unquoted value. An argv list can still be unsafe when the wrapped tool parses the string.

## Test

Try separator, newline, backtick and dollar paren one at a time. Try both quote styles. Check whether the first command exits non zero before using and-and.

## Proof

An expanded marker, then id output or a callback.

## Failure modes

The app reflects the syntax. A proxy expands it. A wrapper tool parses the argument again.
