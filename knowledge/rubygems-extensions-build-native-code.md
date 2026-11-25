---
id: rubygems-extensions-build-native-code
title: RubyGems extensions build native code
tags: pkg, rubygems, extension
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# RubyGems extensions build native code

## Claim

A gem with an extension runs `extconf.rb` and a compiler at install. The build is code execution.

## Test

Read the gemspec and the extension files. Install in a container. Watch the compiler and the network.

## Proof

A build time command from the gem.

## Failure modes

A pure Ruby gem skips it. A precompiled gem can still run a post install.
