---
id: web-ldap-xpath
title: LDAP and XPath injection are filter syntax bugs
tags: web, ldap, xpath, injection
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# LDAP and XPath injection are filter syntax bugs

## Claim

User input is concatenated into an LDAP filter or XPath expression, so a wildcard or boolean changes the match set.

## Test

Try *)(uid=*, admin*, and boolean pairs. For XPath, try ' or 1=1 or '1'='1 and count nodes.

## Proof

A login bypass or extra node in the result.

## Failure modes

An LDAP bind that parses the filter safely is not vulnerable. Escaping differs by library.
