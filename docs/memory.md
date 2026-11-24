# Memory

Beril should not research the same thing twice. Durable knowledge lives in `knowledge/` as small cards, versioned in Git. The raw catalogs stay large; the cards are the distilled layer an agent reads before a search.

## The loop

1. Before a web search, run `./beril recall "<target and class>" --decide`.
2. `USE` means the card is fresh and strong. Answer from it, then test.
3. `REFRESH` means the card is relevant but old or thin. Verify one claim and update it.
4. `RESEARCH` means no card. Collect, then `./beril remember add`.
5. After a lab or finding, add the transferable lesson, not the story.

```bash
./beril recall "saml signature wrapping" --decide
./beril remember add --title "SAML trusts the assertion, not the signature" \
  --claim "The SP reads an assertion the signature does not cover." \
  --test "Move or duplicate the signed assertion, then change identity fields." \
  --proof "A session as the target user from a response signed for another." \
  --failure "A decoded assertion is not a bypass." \
  --tags web,saml,identity --sources references/techniques.md --confidence high
```

## Card shape

```text
---
id: web-idor-owner-check
title: IDOR is a missing owner check, not a hidden id
tags: web, idor, access-control
confidence: high
updated: 2026-11-24
uses: 4
sources: references/techniques.md, docs/break-my-app.md
status: active
---
## Claim
The mechanism.
## Test
The smallest check.
## Proof
What closes it.
## Failure modes
What looks like the bug but is not.
```

A card is a compressed method, not an article summary. If it cannot be tested in 30 minutes, split it.

## Confidence

| Level | Meaning |
|---|---|
| high | Reproduced locally or backed by a primary source, mechanism stable |
| medium | Credible source or one reproduction, some conditions unclear |
| low | Lead, old, or inferred |

High cards can be used without a refresh for 180 days. Medium cards for 90. Low cards are prompts for research.

## Freshness

`./beril remember prune --days 180` marks stale cards. A stale card stays readable; it stops closing a decision until refreshed.

`./beril remember use --id <id>` records a use and bumps the date when you verify it.

## Index

`knowledge/INDEX.md` is generated. Agents read it first, then `recall` for the specific query. The full JSON index is `knowledge/index.json`.

## Git as memory

Every card is a Markdown file with a date and a source. Commit messages become the audit trail. A bad card can be reverted. A good card travels with the repo.

Do not store secrets, customer data, or private report text in a card. Link the source.

## Gaps

`knowledge/GAPS.md` is the honest counterpart to the cards. It lists what Beril does not know yet, ranked. 217 gaps exist and all are covered. The recall regression set is now 69 cases. The recall regression set is `scripts/recall_test.py`. Do not pretend a gap is covered.

```bash
./beril gaps --next
./beril gaps --priority high
./beril gaps --cover web-ldap-xpath --card web-ldap-xpath
```

Close a gap by teaching the card, then cover it.

## What belongs here

- A mechanism that repeats across targets.
- A test that closes a class.
- A parser or protocol quirk.
- A tool invariant, such as GhidRust versus Ghidrust.
- A process rule that prevents waste.

What does not:

- A single CVE with no transferable lesson.
- A target-specific scope note.
- A news item.
- A tool install command.

## Teach the agent

The entry files in the repo root tell Claude, Codex, Cursor and Gemini to recall first. The router has the same rule. The dashboard shows jobs and costs so research waste is visible.

## Recall test

```bash
make recall-test
```

Twenty queries, expected top hit. Run it after a batch of edits.

## Current seed

284 cards across web, mobile, firmware, cloud, AD, RE, exploit, AI and process. The first pass is broad. Grow it from labs and real findings, one card at a time.
