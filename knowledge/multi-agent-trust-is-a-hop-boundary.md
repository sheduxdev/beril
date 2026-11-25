---
id: multi-agent-trust-is-a-hop-boundary
title: Multi agent trust is a hop boundary
tags: ai, multiagent, trust
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/ai-multiagent.md
status: active
---
# Multi agent trust is a hop boundary

## Claim

A worker that trusts a planner message inherits the planner's injection. The worker needs its own tool allowlist.

## Test

Poison the planner input. Watch what the worker calls. Try a tool the worker has but the planner does not.

## Proof

The worker calls a tool outside the intended chain.

## Failure modes

A shared schema narrows the messages. A human gate before the worker stops it.
