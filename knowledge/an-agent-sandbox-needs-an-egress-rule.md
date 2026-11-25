---
id: an-agent-sandbox-needs-an-egress-rule
title: An agent sandbox needs an egress rule
tags: ai, sandbox, egress
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ai-sandbox-escape.md, references/specialist-program.md
status: active
---
# An agent sandbox needs an egress rule

## Claim

A code interpreter with open egress can reach metadata, internal APIs and the model key. The sandbox is only as strong as the network.

## Test

From the sandbox, request the metadata address, a public callback and an internal service. Check DNS and proxy variables.

## Proof

A request leaves the sandbox to a host it should not reach.

## Failure modes

A proxy allowlist and a metadata hop limit close it. A network namespace without routes is strong.
