---
id: runtime-stack-unwind
title: Unwinding runs cleanups between throw and catch
tags: runtime, unwind, exceptions
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Unwinding runs cleanups between throw and catch

## Claim

The unwinder uses tables to find landing pads and destructors. A missing table skips cleanup.

## Test

Throw across a frame with a destructor. Check the cleanup and the catch.

## Proof

The destructor runs once before the handler.

## Failure modes

A foreign exception through C can skip cleanup. A catch-all hides the wrong type.
