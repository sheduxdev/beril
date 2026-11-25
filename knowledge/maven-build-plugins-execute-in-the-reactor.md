---
id: maven-build-plugins-execute-in-the-reactor
title: Maven build plugins execute in the reactor
tags: pkg, maven, plugin
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Maven build plugins execute in the reactor

## Claim

A plugin bound to a phase runs during the build with the builder rights. A repository or a version range is the trust edge.

## Test

Read the plugin list and the versions. Check the repo and the pin. Run a build with a network monitor.

## Proof

A plugin goal that calls out during the build.

## Failure modes

A pinned version and a mirror narrow it. A plugin can be cached.
