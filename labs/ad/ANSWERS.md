# AD lab answers

## 1. Roastable

`svc_backup` has `MSSQLSvc/backup.lab:1433`. A service ticket can be requested and cracked offline. A weak service password becomes a credential.

```bash
impacket-GetUserSPNs LAB/alice:pass -dc-ip 10.0.0.10 -request
```

## 2. Alice

`Domain Users` and `Helpdesk`.

## 3. Helpdesk right

`GenericAll` on `svc_sql`. That allows a password reset, a SPN rewrite, or a full object takeover.

```bash
impacket-net rpc password svc_sql -newpass 'NewPass123!' -user alice -password pass -dc-ip 10.0.0.10
```

## 4. Shortest path

`alice -> MemberOf Helpdesk -> GenericAll svc_sql -> AdminTo APP01 -> HasSession DC01`.

1. Reset `svc_sql` with the Helpdesk right.
2. Use `svc_sql` local admin on `APP01`.
3. Dump the session on `APP01` and find the Domain Admin token.
4. Reuse it against `DC01`.

```bash
impacket-secretsdump LAB/svc_sql:NewPass123!@APP01
```

## 5. ESC1

`WebServer` allows `Helpdesk` to enroll with an enrollable SAN and client auth. A requester can put an arbitrary UPN in the SAN and get a certificate for another user.

```bash
certipy req -u alice@lab -p pass -ca LAB-CA -template WebServer -upn administrator@lab -dc-ip 10.0.0.10
```

## 6. Backup Operators

`svc_backup` is in `Backup Operators`. The group can back up and restore files, often including `ntds.dit`, and log on locally on a DC.

## 7. Commands

Step 3: `impacket-net rpc password svc_sql ...` as above.

Step 4: `impacket-secretsdump` against `APP01` with the `svc_sql` local admin, then `impacket-psexec` or WinRM with the recovered DA hash.

## 8. Mitigations

Remove `GenericAll` from Helpdesk and delegate only the needed right. For ESC1, require approval or remove `ENROLLEE_SUPPLIES_SUBJECT` from the template.

## 9. `HasSession`

A session on `DC01` means a Domain Admin token is present. Local admin on `APP01` lets you dump it. The session edge turns a local win into domain control.

## 10. Chain

```text
alice (Helpdesk) --GenericAll--> svc_sql --AdminTo--> APP01 --HasSession--> DC01
```

The chain is confirmed when the DC hash or a DA shell is in hand. Fix the first edge and the whole path breaks.

## Stretch notes

- BloodHound CE import needs the JSON in its collector format, not this simplified file.
- `WriteDACL` on a group is enough to grant yourself `GenericAll`.
- Constrained delegation to a service on a DC is another path. Compare the required rights.
- Fixes: tiered admin, managed service accounts, gMSA, approval on templates, and session hygiene.
