---
id: ai-sandbox-escape
title: A code interpreter is a process with a filesystem
tags: ai, sandbox, interpreter
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/llm
status: active
---
# A code interpreter is a process with a filesystem

## Claim

Generated code runs in a sandbox that may expose the host filesystem, network or environment.

## Test

Ask the model to read a file outside the workspace. Check the env and network. Try a subprocess.

## Proof

A host file, env variable or network call from generated code.

## Failure modes

A restricted sandbox with no network is still a risk if it reads secrets. Check the mount.
