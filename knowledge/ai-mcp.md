---
id: ai-mcp
title: MCP config is a trust boundary with filesystem and network rights
tags: ai, mcp, config
confidence: high
updated: 2026-11-24
uses: 0
sources: references/claude-bughunter.md
status: active
---
# MCP config is a trust boundary with filesystem and network rights

## Claim

An MCP server runs with the user's rights and exposes tools. A malicious config or prompt can read files or call APIs.

## Test

Read the config. List tools. Check the working directory and env. Test one read outside the project.

## Proof

A file or API read from an MCP tool that the project did not need.

## Failure modes

A read-only server is lower risk. A server that shells out is high.
