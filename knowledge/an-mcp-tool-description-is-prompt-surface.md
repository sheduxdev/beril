---
id: an-mcp-tool-description-is-prompt-surface
title: An MCP tool description is prompt surface
tags: ai, mcp, prompt
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ai-mcp.md, docs/mcp-supply-chain.md
status: active
---
# An MCP tool description is prompt surface

## Claim

The description and the schema are fed to the model. A description can request a file read or a different tool order.

## Test

Read every description. Add an instruction to a local test server. Watch whether the model follows it without a user request.

## Proof

The model performs the described action on its own.

## Failure modes

A short description has less room. A host that truncates the schema hides part.
