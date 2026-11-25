---
id: persistence-needs-a-trigger-the-blue-team-does-not-watch
title: Persistence needs a trigger the blue team does not watch
tags: red, persistence, trigger
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mal-persistence.md
status: active
---
# Persistence needs a trigger the blue team does not watch

## Claim

A run key is watched. A WMI subscription, a COM hijack or a scheduled task with a long delay is not always.

## Test

List the monitored autoruns. Pick a trigger outside the list. Create it and wait for the trigger.

## Proof

A run from the chosen trigger.

## Failure modes

A full autoruns baseline catches it. A trigger can be removed by a cleanup script.
