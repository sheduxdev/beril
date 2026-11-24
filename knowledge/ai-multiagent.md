---
id: ai-multiagent
title: Multi-agent trust is a delegation graph
tags: ai, multiagent, delegation
confidence: high
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# Multi-agent trust is a delegation graph

## Claim

A planner delegates to a worker with broader tools or memory. A compromised worker can poison the shared state.

## Test

Map agents, tools and shared memory. Plant an instruction in a worker input. Observe the planner's next task.

## Proof

A planner action outside the original goal.

## Failure modes

A worker that only reads is lower risk. Shared memory makes the effect persistent.
