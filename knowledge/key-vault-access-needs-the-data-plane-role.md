---
id: key-vault-access-needs-the-data-plane-role
title: Key Vault access needs the data plane role
tags: azure, keyvault, secret
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-secrets.md
status: active
---
# Key Vault access needs the data plane role

## Claim

Management plane rights do not read secrets. A data plane role such as Key Vault Secrets User does.

## Test

Check the access model and the role. Try a secret list and a get with the current token.

## Proof

A secret value.

## Failure modes

A firewall on the vault blocks the request. An RBAC model can be off.
