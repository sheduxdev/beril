---
id: coop-and-coep-isolate-the-browsing-context
title: COOP and COEP isolate the browsing context
tags: browser, coop, coep
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# COOP and COEP isolate the browsing context

## Claim

Cross origin opener and embedder policies decide whether a popup keeps an opener and whether a page can embed cross origin resources.

## Test

Read the two headers. Open the page in a popup and check `window.opener`. Embed a cross origin image without CORP.

## Proof

An opener survives or an embed is blocked as the policy predicts.

## Failure modes

A report only mode changes nothing. Same origin resources bypass the embed check.
