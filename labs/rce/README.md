# RCE lab

A deliberately vulnerable app for the six week track. Standard library only,
local only. Linux or WSL, the command endpoint uses `getent`. Five classes, one chain.

```bash
python3 lab_server.py --port 8100
./tests.sh
```

Open `http://127.0.0.1:8100/`. Every endpoint is broken on purpose.

| Endpoint | Bug | Class |
|---|---|---|
| `/cmd?host=` | shell string with no quote | Command injection, visible |
| `/blind?host=` | same, output swallowed | Blind command injection |
| `/calc?expr=` | `eval` on the input | Code injection |
| `/deser?data=` | `pickle.loads` on base64 | Deserialization |
| `/read?file=` | path join with no realpath | Path traversal |
| `/upload` plus `/plugin` | executes the stored file | Upload to execution |

`notes.txt` and `secret.env` are the read targets. `access.log` is written next
to the server.

## Tasks

Keep the request, the response and one sentence of impact for each.

1. `/cmd`, send `127.0.0.1;id`. Which shell ran, and as which user?
2. `/cmd`, prove a second command with an arithmetic marker. Why must the
   literal payload be absent for a real proof?
3. `/blind`, prove execution with time. Then prove it with a file write into
   `labs/rce/evidence`.
4. `/calc`, run `6*7`. Then reach `os.popen("id").read()`. What does the
   `__builtins__` context allow?
5. `/deser`, build a pickle by hand with `__reduce__` and call
   `subprocess.check_output(["id"])`. Why is base64 not a format check?
6. `/read`, read `secret.env` through traversal. Then read `../web/notes.txt`.
7. `/upload?name=owned.py` with a Python file, then `/plugin?name=owned.py`.
   Which check is missing between storage and execution?
8. Chain two bugs into one proof. Upload plus plugin is one. Find a second
   chain from read to execution. The access log and the plugin runner are
   available.
9. Write the fix for `/cmd`, `/calc`, `/deser` and `/plugin`.
10. Write the report for the command injection. Use the rung 3 proof.

## Constraints

Local host only. The lab executes commands and files. Do not put secrets in the
lab directory. Snapshot if you run it on a shared host.

## Evidence

`labs/rce/evidence/` is for your files. The smoke test writes `blind.txt` and
`owned.py` there. Keep your request pairs in a notes file.

## Stretch

- Make `/cmd` quote the host but keep `$()` working. Which fix still fails?
- Build a payload that survives a space filter.
- Turn the upload into a reverse shell.
- Add a signature check on the pickle and break it.
- Run the whole chain through a proxy and save the session.

## Map to the track

The lab covers weeks 1 to 6 at rung 2 and 3. PortSwigger covers the engines and
the Java gadget cases the lab cannot. Answers are in `ANSWERS.md`.
