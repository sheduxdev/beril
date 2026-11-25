---
id: a-process-environment-is-a-secret-store
title: A process environment is a secret store
tags: linux, proc, secret
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/os-namespaces.md
status: active
---
# A process environment is a secret store

## Claim

`/proc/<pid>/environ` holds the environment of a running process, including tokens and keys passed at start.

## Test

List processes. Read environ for the app, the agent and the cron job. Grep for key names.

## Proof

A live token from the environment.

## Failure modes

A process can scrub the environment. A container can hide the host proc.
