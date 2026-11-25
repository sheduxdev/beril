---
id: an-okta-admin-role-is-a-tenant-key
title: An Okta admin role is a tenant key
tags: idp, okta, admin
confidence: high
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# An Okta admin role is a tenant key

## Claim

A super admin or an app admin in Okta can add a federation, assign an app or reset a factor across the tenant.

## Test

List the roles and the assignments. Check the admin app. Try one assignment with the role.

## Proof

A new app assignment or a factor reset.

## Failure modes

A scoped admin role limits the reach. A break glass account can bypass the policy.
