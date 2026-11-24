---
id: proto-framing
title: A frame needs a length the parser can trust
tags: protocol, framing, length
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A frame needs a length the parser can trust

## Claim

A length prefix or a delimiter defines the frame. Ambiguity between parsers is a desync.

## Test

Send an oversized, a truncated and a nested frame. Compare the parser boundary.

## Proof

A rejected or correctly bounded frame.

## Failure modes

A delimiter inside the payload splits a frame. A length without a cap allocates too much.
