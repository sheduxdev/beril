---
id: a-login-wall-changes-the-osint-terms
title: A login wall changes the OSINT terms
tags: osint, terms, legal
confidence: high
updated: 2026-11-26
uses: 0
sources: references/osint-toolkit.md, docs/legal.md
status: active
---
# A login wall changes the OSINT terms

## Claim

A public page is one terms state. A logged in page or an API key is another. The collection note must say which.

## Test

Record the login state and the terms URL per source. Check whether the scraper identifies itself.

## Proof

A source note with the login state and the terms link.

## Failure modes

A public page can still forbid scraping. A key can have a query quota.
