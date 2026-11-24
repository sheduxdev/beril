---
id: eng-config
title: Config belongs to the environment, secrets belong to a store
tags: engineering, config, secrets
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Config belongs to the environment, secrets belong to a store

## Claim

A config value changes per environment. A secret is not a config default in source.

## Test

List every config key. Check the default, the validation and the secret source.

## Proof

A deploy that fails fast on a missing or invalid value.

## Failure modes

A secret in a config file in git is a leak.
