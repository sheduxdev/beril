# Specialist tracks

Beril has twelve four week specialist tracks. Each has a threat model, drills,
a local or external lab and an exit proof. The program is `references/specialist-program.md`.
The scoring rubric is `references/senior-bar.md`.

## Start

Pick one track from the table in the program. Do not pick the one you already
know. Run the entry drill, then decide whether to stay.

```bash
./beril labs --run web
./beril labs --run rce
./beril labs --run ad
```

Every Friday ends with one page. Every fourth week ends with an exit proof a
peer can rerun.

## Time

Two hours a day, ten hours a week, four weeks. Twelve tracks is a year. Keep
one track warm each month after that.

## Choose by work

| Work | First track |
|---|---|
| SaaS bounty | Web and business logic |
| Internal enterprise | Identity and SSO |
| API product | API and GraphQL |
| Cloud team | Cloud and Kubernetes |
| Windows estate | Active Directory |
| Exploit research | Binary exploitation |
| Mobile product | Mobile and client |
| SOC | Detection and IR |
| Build platform | Supply chain and CI |
| AI product | AI and agent security |
| Hardware | Firmware and IoT |
| Network team | Network and BGP |

## Evidence

Each week has one artifact. A request pair, a crash, a rule with a false
positive table, a trust diff, a timeline. Keep it in a folder named after the
track. Redact client data before publishing.

## Review

Score the artifact on the ten axes. Eighteen or more moves on. Twenty four or
more is senior. Below eighteen means repeat the exit proof with a new target.

Ask a peer one question per axis. Write their answer down. The review is the
lesson.

## Relation to the 25 week curriculum

The six week RCE track and these twelve tracks sit on top of `references/curriculum.md`.
The 25 week plan gives the base. A track gives the depth. Do not run a track
before the base week that it needs.

| Track | Base week |
|---|---|
| Web, identity, API | Week 8 and 9 |
| Cloud, AD | Week 18 and 19 |
| Binary, mobile, firmware | Week 14 and 21 |
| Detection, network | Week 20 |
| AI | Week 23 |
| Supply chain | Week 10 |

## What does not count

A tutorial watched at double speed. A tool install. A list of payloads. A
certificate without an artifact. A track week without a file path.

## Portfolio

One artifact per track, twelve total. A short index page that links each one.
The portfolio is the proof of the senior bar, not the track list.
