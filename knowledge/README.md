# Knowledge cards

Durable, testable lessons. Read `INDEX.md` first, then `./beril recall "<query>"`.

Each card has a claim, a test, a proof and failure modes. A card is editable Markdown; the index is generated.

```bash
./beril remember add --title ... --claim ... --test ... --proof ... --failure ... --tags ...
./beril remember update --id ... --claim ...
./beril remember use --id ...
./beril remember prune --days 180
./beril remember index
```

Rules:

- One mechanism per card.
- A source for every claim.
- A date and a confidence.
- No secrets.
- Split when the card needs two tests.
