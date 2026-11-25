---
id: fhir-is-a-rest-api-with-a-scope
title: FHIR is a REST API with a scope
tags: med, fhir, api
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/api-openapi.md
status: active
---
# FHIR is a REST API with a scope

## Claim

FHIR resources carry patient data. A SMART scope grants the resource and the action. A missing scope check is the bug.

## Test

Read the capability statement and the scopes. Request a Patient by id. Try a resource outside the scope.

## Proof

A resource outside the granted scope.

## Failure modes

A strict scope and a consent check hold. A bulk endpoint can be separate.
