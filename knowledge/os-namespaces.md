---
id: os-namespaces
title: A namespace makes a resource set invisible
tags: os, namespaces, isolation
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A namespace makes a resource set invisible

## Claim

Mount, PID, network and user namespaces split the view. A shared namespace is a shared failure domain.

## Test

Inspect the namespace ids. Enter a new mount namespace. Check the visibility.

## Proof

A process that cannot see the host resource.

## Failure modes

A user namespace alone is not a container. A shared network namespace shares ports.
