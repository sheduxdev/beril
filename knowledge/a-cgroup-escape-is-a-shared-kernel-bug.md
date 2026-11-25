---
id: a-cgroup-escape-is-a-shared-kernel-bug
title: A cgroup escape is a shared kernel bug
tags: link, cgroup, container
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/os-cgroups.md
status: active
---
# A cgroup escape is a shared kernel bug

## Claim

The cgroup limits resources, not access. A kernel bug in a controller or a namespace transition escapes the group.

## Test

Read the cgroup version and the controllers. Check the namespace and the mount. Try a release agent or a notify path.

## Proof

A process outside the cgroup or a host file access.

## Failure modes

A user namespace can contain it. A patched kernel closes it.
