---
id: tcc-is-the-privacy-consent-database
title: TCC is the privacy consent database
tags: macos, tcc, privacy
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# TCC is the privacy consent database

## Claim

Camera, microphone, screen, disk and automation grants live in TCC. A user level grant is a durable capability.

## Test

Read the TCC database with full disk access. List the grants. Trigger one app and watch the prompt.

## Proof

A grant that survives a restart.

## Failure modes

A signed app can inherit a grant. A reset clears it.
