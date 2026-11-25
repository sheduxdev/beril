---
id: a-state-machine-can-be-jumped-not-only-raced
title: A state machine can be jumped, not only raced
tags: web, logic, state-machine
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md, knowledge/web-race-single-packet.md
status: active
---
# A state machine can be jumped, not only raced

## Claim

If the server trusts the submitted status, an order moves from created to shipped or refunded without the middle step.

## Test

Send the final status directly after create. Then send a backward transition and a second refund.

## Proof

The skipped or repeated transition is accepted.

## Failure modes

A guarded transition table rejects it. A worker can overwrite the status later.
