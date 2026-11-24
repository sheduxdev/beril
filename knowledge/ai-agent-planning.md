---
id: ai-agent-planning
title: An agent plan is a permission boundary
tags: ai, agent, planning
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# An agent plan is a permission boundary

## Claim

A planner can spawn subagents or tools with broader rights than the user intended, and a retrieved instruction can change the goal.

## Test

Map the plan and each subagent's tools. Plant a goal in a document. Watch the delegated task and its permissions.

## Proof

A subagent action outside the original goal.

## Failure modes

A plan that repeats the user request is normal. Check delegated scope, not only the final text.
