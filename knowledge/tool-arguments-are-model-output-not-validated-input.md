---
id: tool-arguments-are-model-output-not-validated-input
title: Tool arguments are model output, not validated input
tags: ai, tool, injection
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ai-tool-output.md
status: active
---
# Tool arguments are model output, not validated input

## Claim

A tool that trusts the model argument inherits the model's injection surface. The argument needs the same validation as a user field.

## Test

Plant an instruction in content the model reads. Ask it to call a tool with a traversal path, a URL or a shell flag.

## Proof

The tool receives the crafted argument and acts on it.

## Failure modes

A schema and an allowlist in the tool close it. A model that quotes correctly still needs the check.
