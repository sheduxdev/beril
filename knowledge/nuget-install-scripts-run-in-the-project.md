---
id: nuget-install-scripts-run-in-the-project
title: NuGet install scripts run in the project
tags: pkg, nuget, script
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# NuGet install scripts run in the project

## Claim

An `install.ps1` or a build target in a package runs during restore or build. The script is not in the package list view.

## Test

Read the package contents and the nuspec. Restore with a monitor. Check the target imports.

## Proof

A script or a target action during restore.

## Failure modes

Package reference style can skip the install script. A lockfile pins the version.
