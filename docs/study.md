# Study and coverage

Two commands keep the knowledge sharp.

## Quiz

Draw recall cards as questions. The default mode shows the title and the test
scenario and hides the claim, proof and failure.

```bash
./beril quiz
./beril quiz --tag web --count 5
./beril quiz --tag auth --mode claim --answers
./beril quiz --json
```

Modes.

| Mode | Question | Answer |
|---|---|---|
| `test` | Title and scenario | Claim, proof, failure |
| `claim` | Claim | Test, proof, failure |
| `title` | Title | Claim, test, proof |

Use one card a day per weak domain. Say the answer out loud before `--answers`.
A card you fail twice goes into your notes as a drill.

## Coverage

```bash
./beril coverage
./beril coverage --json
```

The panel counts active cards, labs and references per domain and marks a domain
thin under ten cards. The target is twenty per domain. Coverage is a rough map,
not a score of quality.

Use it once a month. Take the three thinnest domains and add one card each after
a real lesson. Do not add a card without a test and a failure mode.

## Rules

- A card you cannot test is a note, not knowledge.
- A quiz answer without the proof is half an answer.
- A thin domain needs a lab before more cards.
- A strong domain still needs one old card each month.
