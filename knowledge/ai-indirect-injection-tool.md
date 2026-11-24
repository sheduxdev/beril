---
id: ai-indirect-injection-tool
title: Indirect injection turns a document into an instruction
tags: ai, llm, prompt-injection
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/llm, references/techniques.md
status: active
---
# Indirect injection turns a document into an instruction

## Claim

A retrieved chunk contains instructions that the model follows, especially when a tool can send data out.

## Test

Plant an instruction in a document. Ask a normal question. Watch for a tool call with attacker arguments.

## Proof

A tool call or output that crosses the boundary without a user instruction.

## Failure modes

A prompt that says ignore previous instructions is not impact until the tool acts.
