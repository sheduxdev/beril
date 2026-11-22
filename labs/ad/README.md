# AD lab

A static Active Directory snapshot. No Windows host needed.

```bash
./tests.sh
```

Files: `users.json`, `acls.csv`, `adcs.csv`.

## Tasks

1. Which account has a Kerberoastable SPN, and why does that matter?
2. Which group does alice belong to?
3. What right does `Helpdesk` have over `svc_sql`?
4. What is the shortest path from alice to a session on `DC01`?
5. Which ADCS template is ESC1, and which principal can enroll?
6. Which account is in `Backup Operators`, and what does that group allow?
7. Write the exact commands for steps 3 and 4.
8. Name two mitigations for the ESC1 template.
9. Which edge is a `HasSession` and why is it useful after local admin?
10. Write the chain as a triager would read it.

## Evidence

Give the edge, the command, and the resulting access. Use `impacket`, `certipy`, and BloodHound syntax even though the lab is fake.

## Stretch

- Import the files into a real BloodHound CE instance.
- Add a `WriteDACL` edge and a second path.
- Add a constrained delegation edge and compare.
- Write the fixes for each ACL edge.

Answers are in `ANSWERS.md`.
