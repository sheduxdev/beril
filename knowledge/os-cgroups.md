---
id: os-cgroups
title: A cgroup is a resource boundary with pressure signals
tags: os, cgroups, limits
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# A cgroup is a resource boundary with pressure signals

## Claim

CPU, memory and IO limits apply to the group. The OOM killer acts on the group, not only the process.

## Test

Set a memory limit. Exceed it. Check the OOM scope and the pressure file.

## Proof

A bounded group with a clear OOM event.

## Failure modes

A limit on the parent is shared by children. A swap setting changes the failure.
