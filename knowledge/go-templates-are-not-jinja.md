---
id: go-templates-are-not-jinja
title: Go templates are not Jinja
tags: lang, go, ssti
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Go templates are not Jinja

## Claim

`text/template` does not auto escape. A user value in the template source reaches methods on the data object.

## Test

Send `{{.}}` and a method call. Check the output and the escape for `html/template`.

## Proof

An evaluated expression or an unescaped output.

## Failure modes

A template parsed once with a fixed source is safer. A sandbox can limit the methods.
