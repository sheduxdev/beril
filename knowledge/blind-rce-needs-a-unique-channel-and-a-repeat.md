---
id: blind-rce-needs-a-unique-channel-and-a-repeat
title: Blind RCE needs a unique channel and a repeat
tags: rce, blind, oob
confidence: high
updated: 2026-11-26
uses: 0
sources: references/rce-mastery.md
status: active
---
# Blind RCE needs a unique channel and a repeat

## Claim

When output is swallowed, a DNS or HTTP callback with a per request token is the proof. Time alone needs a baseline and a repeat.

## Test

Send one token per request from the target. Record the resolver or web log with time and source. Repeat once to rule out jitter.

## Proof

A callback log entry that matches the token and time.

## Failure modes

A proxy makes the callback. The cache replays it. Sleep comes from network delay.
