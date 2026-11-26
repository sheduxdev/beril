---
id: a-github-dork-is-a-query-with-a-field
title: A GitHub dork is a query with a field
tags: osint, github, dork
confidence: high
updated: 2026-11-26
uses: 0
sources: references/osint-toolkit.md
status: active
---
# A GitHub dork is a query with a field

## Claim

`org:`, `filename:` and `path:` narrow the code search to the target. A bare string returns every fork and tutorial.

## Test

Add one field at a time to the query. Compare the hit count and the first page. Open a hit and confirm the org.

## Proof

A hit inside the target org with the file path.

## Failure modes

A fork carries the same file. A private repo can be invisible.
