# The senior bar

A senior is judged by the decisions around the bug, not only by the bug. This
file scores those decisions. Use it after every specialist track artifact and
in peer review.

## Levels

| Level | Signal |
|---|---|
| Operator | Can run the tool and reproduce a known class with help |
| Senior | Can model an unfamiliar target, choose the class, prove it and land the fix |
| Principal | Changes how a team works, predicts failure, and the org trusts the call |

A certificate can open a door. This bar decides whether you keep the room.

## The ten axes

Score each axis 0 to 3.

### 1. Scope and threat model

| Score | Anchor |
|---|---|
| 0 | Tests whatever looks interesting |
| 1 | Reads the scope and the app entry points |
| 2 | Names actors, assets and trust boundaries before a payload |
| 3 | Predicts which boundary matters and writes the one page model |

### 2. Evidence

| Score | Anchor |
|---|---|
| 0 | A screenshot and a claim |
| 1 | A request or a crash |
| 2 | Minimal request pair, response and hash |
| 3 | Reproducible from a clean machine with a timestamp and a baseline |

### 3. Root cause

| Score | Anchor |
|---|---|
| 0 | Names the symptom |
| 1 | Names the function |
| 2 | Names the missing check and the transform |
| 3 | Shows the shortest source to sink path and the fix in code |

### 4. Impact and business context

| Score | Anchor |
|---|---|
| 0 | Copies a CVSS vector |
| 1 | Names data or an action |
| 2 | Shows who is harmed and what it costs |
| 3 | Ranks the impact against the business and the threat actor that matters |

### 5. Chain building

| Score | Anchor |
|---|---|
| 0 | One step, assumed |
| 1 | Two steps, one unproven |
| 2 | Every link has a request or a proof |
| 3 | The weakest link is tested first and the chain stops when the impact is clear |

### 6. Tool judgment

| Score | Anchor |
|---|---|
| 0 | Runs every tool and dumps the output |
| 1 | Runs the standard tool for the class |
| 2 | Picks the tool after the hypothesis and knows its noise |
| 3 | Drops the tool when the manual request is faster and says why |

### 7. Communication

| Score | Anchor |
|---|---|
| 0 | Payload dump |
| 1 | Steps in order |
| 2 | A triager can rerun it and a developer can fix it |
| 3 | The right profile for the reader, no oversell, the fix is verifiable |

### 8. Judgment under uncertainty

| Score | Anchor |
|---|---|
| 0 | Guesses and hides it |
| 1 | Labels confirmed and inferred |
| 2 | Names the assumption and the test that would settle it |
| 3 | Stops when the risk of a wrong call is higher than the value of one more probe |

### 9. Teaching and review

| Score | Anchor |
|---|---|
| 0 | No notes |
| 1 | Shares the command |
| 2 | Reviews a peer and names the weak link |
| 3 | Predicts the three mistakes a learner will make and builds the drill |

### 10. Ethics and law

| Score | Anchor |
|---|---|
| 0 | Scans first, asks later |
| 1 | Checks ownership and avoids writes |
| 2 | Keeps the gate, the scope and the production window |
| 3 | Documents the legal basis, the data handled and the rollback |

## Bands

| Total | Meaning |
|---:|---|
| 0 to 9 | Operator |
| 10 to 17 | Strong operator, not senior |
| 18 to 23 | Senior track, needs one more artifact |
| 24 to 29 | Senior |
| 30 | Principal evidence |

## Artifact floor

No score above 1 on axes 2, 3 and 4 without the matching evidence. A perfect
communication score cannot carry a thin proof.

## Review questions

1. What did the tester assume, and is it written down?
2. Which link in the chain is weakest, and was it tested first?
3. Could a different explanation produce the same response?
4. Is the impact real for this business, not for a lab?
5. Does the fix close the class, or only the string?
6. What did the tester not test, and does it matter?
7. Would a second run from a clean machine reproduce it?

## Anti patterns

| Pattern | What it hides |
|---|---|
| CVSS as the first sentence | No business thought |
| Tool output as the report | No root cause |
| Every class on every endpoint | No depth |
| A screenshot with no request | No reproduction |
| "Critical" in the title, info in the impact | Oversell |
| A fix that blocks one payload | No class level fix |
| A chain with an assumed hop | Theater |
| No untested section | Dishonesty |

## Use

- Score your own artifact before sending.
- Score a peer artifact every month.
- Keep the two lowest axes as next month's drill.
- Re score one old artifact after six months. The delta is your progress.

## Honest limits

The bar is a judgment tool. Two reviewers can differ by three points on one
axis. Calibrate on the evidence, not on style.
