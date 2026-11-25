---
id: an-agent-tool-call-is-a-confused-deputy
title: An agent tool call is a confused deputy
tags: ai, agent, authorization
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ai-agent-tool.md, labs/llm
status: active
---
# An agent tool call is a confused deputy

## Claim

The agent calls a tool with its own service rights. A user who cannot use the tool directly can reach it through the model.

## Test

Map each tool and the identity it uses. Call the tool through the chat with a low privilege account. Compare with a direct call.

## Proof

The tool acts with rights the user does not hold.

## Failure modes

A per user token passed to the tool closes it. A read only tool has low impact.
