---
id: an-agent-loop-needs-a-turn-and-token-budget
title: An agent loop needs a turn and token budget
tags: ai, agent, cost
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ai-cost-control.md, knowledge/ai-agent-planning.md
status: active
---
# An agent loop needs a turn and token budget

## Claim

A planner that can call itself or a tool without a cap loops on one ambiguous goal and burns the key.

## Test

Give an impossible task. Watch the turn count and the token spend. Remove the tool from the loop.

## Proof

The run stops at the cap and reports the spend.

## Failure modes

A small model can still loop inside one turn. A cheap tool call hides the cost.
