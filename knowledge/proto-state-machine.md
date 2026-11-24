---
id: proto-state-machine
title: A protocol is a set of legal transitions
tags: protocol, state-machine, transitions
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A protocol is a set of legal transitions

## Claim

Each message moves the connection between states. An illegal transition is a bug or a bypass.

## Test

List the states and transitions. Send a message out of order. Check the response.

## Proof

A rejected transition with the expected state.

## Failure modes

A permissive server accepts everything, so the state machine hides in the client.
