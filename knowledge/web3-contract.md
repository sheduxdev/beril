---
id: web3-contract
title: Smart contracts fail on external calls and access control
tags: web3, solidity, contract
confidence: high
updated: 2026-11-25
uses: 0
sources: references/techniques.md
status: active
---
# Smart contracts fail on external calls and access control

## Claim

Reentrancy, missing modifiers, unsafe delegatecall, oracle trust or integer issues move funds.

## Test

Read the contract and the call graph. Test a reentrancy path in a fork. Check owner functions and price feeds.

## Proof

A state change or fund movement an attacker can repeat.

## Failure modes

A testnet-only issue may not matter. Check the deployed bytecode and proxy.
