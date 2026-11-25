---
id: app-consent-phishing-is-a-scope-grant
title: App consent phishing is a scope grant
tags: idp, consent-phishing, oauth
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/web-oauth-redirect-binding.md
status: active
---
# App consent phishing is a scope grant

## Claim

A malicious app asks for a scope and the user grants it. The app reads mail or files without a password.

## Test

Read the consent screen and the scopes. Grant with a test user. Call the resource with the token.

## Proof

A resource read from the granted token.

## Failure modes

An admin consent policy blocks the user. A verified publisher can raise trust.
