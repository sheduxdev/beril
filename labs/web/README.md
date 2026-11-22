# Web lab

A small deliberately vulnerable app. Standard library only, local only.

```bash
python3 lab_server.py --port 8099
./tests.sh
```

Open `http://127.0.0.1:8099/`. Users are alice (1), bob (2), admin (3).

## Tasks

1. Browse the app with DevTools open. List every request parameter.
2. Log in as alice and read bob's profile. What object identifier is missing a check?
3. Put `<script>alert(document.domain)</script>` in search. Which context is unescaped?
4. Use `id=1 OR 1=1` on `/item`. Then read the admin user through a UNION.
5. Read `../../README.md` through `/download`. How far up can you go?
6. Fetch `http://127.0.0.1:8099/health` through `/fetch`. Try a port that is closed and compare the error.
7. Set only the `role=admin` cookie and open `/admin`. Why does it work?
8. Read `/api/users/2` without a login.
9. Compare the HTML profile and the JSON API. Which one leaks more?
10. Write a report for the IDOR with two accounts and the exact requests.

## Constraints

Use only these users and the local host. Do not scan outside.

## Evidence

For each task keep the request, the response, and one sentence of impact. Use `curl -i` or a proxy.

## Stretch

- Reproduce the SQLi through a UNION and return a `users` row in the item template.
- Find a second path traversal encoding that still works.
- Turn the XSS into a cookie theft against `/admin` with a tiny listener.
- Fix two bugs and rerun `tests.sh`.

Answers are in `ANSWERS.md`. Read them only after a real attempt.
