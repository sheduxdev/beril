---
id: dependency-confusion-needs-an-internal-name-on-a-public-regi
title: Dependency confusion needs an internal name on a public registry
tags: supply, dependency-confusion, registry
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Dependency confusion needs an internal name on a public registry

## Claim

A package manager that prefers the public registry for an internal name installs the attacker package when versions are higher.

## Test

Read the scope and registry config. Look for unscoped internal names. Check whether a public package with that name exists.

## Proof

The public package installs in place of the internal one.

## Failure modes

A scope or a registry pin closes it. A higher internal version can win.
