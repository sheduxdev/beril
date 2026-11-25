# API lab

Four broken API patterns. Standard library only, local only.

```bash
python3 lab_server.py --port 8103
./tests.sh
```

| Endpoint | Bug |
|---|---|
| `GET /api/users/<id>` | BOLA, any token reads any user |
| `PATCH /api/users/<id>` | Role is mass assignable |
| `GET /graphql` | Alias batching has no cost limit |
| `GET /api/export` | SSRF to any URL |

Tokens are `alice-token` and `bob-token`. Users are alice, bob and admin.

## Tasks

1. Read user 3 with the bob token.
2. Change your role with one PATCH.
3. Send ten aliases in one GraphQL query. Compare with ten requests.
4. Point the export at a closed port and at the health endpoint.
5. Write the fix for each bug.
6. Chain BOLA and mass assignment into a tenant admin.
7. Explain why a token check is not an authorization check.

## Constraints

Local host. State resets on restart. Do not read outside the lab.

## Evidence

Keep the request, the response and the token. The BOLA proof needs a user id outside the token owner.

Answers are in `ANSWERS.md`.
