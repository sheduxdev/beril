---
id: composer-scripts-run-after-install
title: Composer scripts run after install
tags: pkg, composer, script
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Composer scripts run after install

## Claim

A `post-install-cmd` or a plugin in composer.json runs with the project user.

## Test

Read the scripts and the plugin allow list. Install in a clean container. Watch the process and the network.

## Proof

A script execution during install.

## Failure modes

`--no-scripts` blocks it. A global plugin allow list can disable it.
