---
id: web-clickjacking
title: Clickjacking is a missing frame policy with a valuable action
tags: web, clickjacking, ui
confidence: high
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# Clickjacking is a missing frame policy with a valuable action

## Claim

The page can be framed and a sensitive action sits at a predictable position. frame-ancestors or X-Frame-Options is missing.

## Test

Load the page in an iframe from another origin. Overlay a decoy. Click the action as a logged-in user.

## Proof

A state change from a click the user thought was for the decoy.

## Failure modes

A page that cannot be framed is safe. A low-value action is low impact.
