# Auth lab

Four broken auth patterns. Standard library only, local only.

```bash
python3 lab_server.py --port 8101
./tests.sh
```

| Endpoint | Bug |
|---|---|
| `/login` | Session id does not rotate at login |
| `/mfa` | MFA is a client flag the API ignores |
| `/reset` | Token is a counter and it is reusable |
| `/admin` | JWT accepts `alg none` |

Users are alice and admin. Passwords are in the server source, which is fair for a lab.

## Tasks

1. Set a session id yourself, log in and prove the id survives.
2. Log in with the password, skip the OTP and call `/api/profile`.
3. Request a reset token twice. Predict the next one. Reuse one token.
4. Take the alice token, change the payload role to admin, keep `alg none` and call `/admin`.
5. Read `/session` and name every value the server returns that a real app would hide.
6. Write the fix for each bug in one line of code terms.
7. Chain fixation and MFA skip into one account takeover.

## Constraints

Local host. The lab keeps state in memory and resets on restart.

## Evidence

For each task keep the cookie, the request and the response. A task without a request pair is a note.

## Stretch

- Add a state parameter and bind it to the session. Break it again.
- Sign the JWT with HMAC and try an algorithm confusion.
- Add a one time reset token and a session rotation, then rerun `tests.sh`.

Answers are in `ANSWERS.md`.
