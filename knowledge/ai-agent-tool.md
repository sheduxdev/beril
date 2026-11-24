---
id: ai-agent-tool
title: Agent tool abuse is argument control, not prompt text
tags: ai, agent, tool
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/llm
status: active
---
# Agent tool abuse is argument control, not prompt text

## Claim

The model can be made to call a tool with an attacker-chosen path, recipient or query, beyond the user's intent.

## Test

Map each tool and its arguments. Plant an instruction in a document. Watch the argument values.

## Proof

A tool call with an attacker value and a visible effect.

## Failure modes

A tool call that repeats the user's request is normal. Check the argument, not only the tool name.
