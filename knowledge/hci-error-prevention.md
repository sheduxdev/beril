---
id: hci-error-prevention
title: Prevent the error before the confirmation
tags: hci, error-prevention, undo
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Prevent the error before the confirmation

## Claim

A constraint, a default or an undo beats a modal confirmation. A dialog is the last resort.

## Test

Try the destructive action with a near-miss input. Check the guard and the undo.

## Proof

A prevented error or a one-step undo.

## Failure modes

A confirmation every time trains a blind click. An undo that expires is a trap.
