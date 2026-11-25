---
id: red-team-opsec-is-a-mistake-ledger
title: Red team OPSEC is a mistake ledger
tags: red, opsec, mistake
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/attacking.md
status: active
---
# Red team OPSEC is a mistake ledger

## Claim

Every tool leaves a log, a file, a process or a network artifact. The operation needs a list of the artifacts per action.

## Test

Before an action, write the artifact it will leave and who sees it. After, check the artifact.

## Proof

An artifact list with the blue team view.

## Failure modes

A native tool avoids the file drop but leaves the log. A noisy host hides the artifact.
