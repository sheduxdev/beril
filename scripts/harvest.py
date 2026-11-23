#!/usr/bin/env python3
"""Harvest cybersecurity forums, experts, tools and method pages.

Examples
--------
python scripts/harvest.py forums --sources 0x00sec,htb --out data/threads.jsonl
python scripts/harvest.py experts --sources hackerone --out data/experts.jsonl
python scripts/harvest.py tools --sources canonical --out data/tools.jsonl
python scripts/harvest.py methods --out data/methods.jsonl
python scripts/harvest.py all --out-dir data
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guard
from camo import CamoSession, clean, extract_links, write_jsonl

NOW = lambda: dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")  # noqa: E731

CURATED_EXPERTS = [
    ("nahamsec", "Ben Sadeghipour", "https://www.nahamsec.com/", "recon, live hacking, bug bounty education"),
    ("Jhaddix", "Jason Haddix", "https://x.com/Jhaddix", "bug hunter methodology, recon, attack surface"),
    ("tomnomnom", "Tom Hudson", "https://tomnomnom.com/", "recon tooling, Go, asset discovery"),
    ("fransrosen", "Frans Rosen", "https://fransrosen.com/", "web exploitation, account takeover chains"),
    ("stokfredrik", "STOK", "https://x.com/stokfredrik", "recon, content discovery, live hacking"),
    ("edoverflow", "EdOverflow", "https://edoverflow.com/", "web security, disclosure, OAuth"),
    ("mazen160", "Mazin Ahmed", "https://mazinahmed.net/", "application security, SSRF, recon"),
    ("samwcurry", "Sam Curry", "https://samcurry.net/", "web exploitation, supply chain"),
    ("orange_8361", "Orange Tsai", "https://blog.orange.tw/", "web exploitation, network appliances"),
    (
        "albinowax",
        "James Kettle",
        "https://portswigger.net/research/james-kettle",
        "request smuggling, cache poisoning, desync",
    ),
    ("garethheyes", "Gareth Heyes", "https://portswigger.net/research/gareth-heyes", "XSS, parser quirks, client-side"),
    ("Rhynorater", "Justin Gardner", "https://x.com/Rhynorater", "web exploitation, bug bounty"),
    ("hakluke", "Luke Stephens", "https://hakluke.com/", "recon, automation"),
    ("zhero___", "Zhero", "https://x.com/zhero___", "web exploitation, APIs"),
    ("ryancblack", "Ryan Black", "https://x.com/ryancblack", "red team, cloud, Active Directory"),
    ("0xsha", "Sha", "https://x.com/0xsha", "exploit development, Windows internals"),
]

CANONICAL_TOOLS = {
    "recon": [
        "projectdiscovery/subfinder",
        "projectdiscovery/httpx",
        "projectdiscovery/katana",
        "projectdiscovery/naabu",
        "projectdiscovery/dnsx",
        "projectdiscovery/tlsx",
        "projectdiscovery/cdncheck",
        "projectdiscovery/asnmap",
        "projectdiscovery/alterx",
        "projectdiscovery/notify",
        "projectdiscovery/interactsh",
        "projectdiscovery/uncover",
        "owasp-amass/amass",
        "tomnomnom/waybackurls",
        "lc/gau",
        "tomnomnom/hakrawler",
        "ffuf/ffuf",
        "epi052/feroxbuster",
        "OJ/gobuster",
        "maurosoria/dirsearch",
        "s0md3v/Arjun",
        "devanshb01/ParamSpider",
        "ProjectDiscovery/chaos",
        "findomain/findomain",
        "tomnomnom/assetfinder",
        "d3mondev/puredns",
        "blechschmidt/massdns",
        "aboul3la/Sublist3r",
        "projectdiscovery/nuclei",
    ],
    "web": [
        "sqlmapproject/sqlmap",
        "hahwul/dalfox",
        "s0md3v/XSStrike",
        "sullo/nikto",
        "wpscanteam/wpscan",
        "PortSwigger/param-miner",
        "PortSwigger/turbo-intruder",
        "ticarpi/jwt_tool",
        "dolevf/graphql-cop",
        "nikitastupin/clairvoyance",
        "swisskyrepo/PayloadsAllTheThings",
        "danielmiessler/SecLists",
        "zan8in/afrog",
        "chaitin/xray",
        "projectdiscovery/nuclei-templates",
    ],
    "cloud_ad": [
        "BloodHoundAD/BloodHound",
        "fortra/impacket",
        "ropnop/kerbrute",
        "GhostPack/Rubeus",
        "ly4k/Certipy",
        "lgandx/Responder",
        "jpillora/chisel",
        "nicocha30/ligolo-ng",
        "BishopFox/sliver",
        "HavocFramework/Havoc",
    ],
    "mobile_binary": [
        "MobSF/Mobile-Security-Framework-MobSF",
        "frida/frida",
        "sensepost/objection",
        "iBotPeaches/Apktool",
        "skylot/jadx",
        "NationalSecurityAgency/ghidra",
        "radareorg/radare2",
        "Gallopsled/pwntools",
        "JonathanSalwan/ROPgadget",
        "isec-tools/one_gadget",
    ],
    "osint_surface": [
        "sherlock-project/sherlock",
        "soxoj/maigret",
        "laramies/theHarvester",
        "sundowndev/phoneinfoga",
        "mxrch/GHunt",
        "smicallef/spiderfoot",
        "lissy93/web-check",
        "yogeshojha/rengine",
        "six2dez/reconftw",
        "kpcyrd/sn0int",
        "GhostTroops/scan4all",
        "Autumn-27/ScopeSentry",
    ],
    "agentic": [
        "KeygraphHQ/shannon",
        "usestrix/strix",
        "GreyDGL/PentestGPT",
        "vxcontrol/pentagi",
        "xalgorix/xalgorix",
        "Armur-Ai/Pentest-Swarm-AI",
        "CyberStrikeus/CyberStrike",
        "elementalsouls/Claude-BugHunter",
    ],
    "audit_defense": [
        "CISOfy/lynis",
        "aquasecurity/trivy",
        "anchore/grype",
        "returntocorp/semgrep",
        "gitleaks/gitleaks",
        "trufflesecurity/trufflehog",
        "fuzzdb-project/fuzzdb",
    ],
}


# ------------------------------------------------------------------ forums


def forums_0x00sec(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    feeds = [
        ("feed", "https://0x00sec.org/rss/"),
        ("redteam", "https://0x00sec.org/tag/redteam/rss/"),
        ("reverse-engineering", "https://0x00sec.org/tag/reverse-engineering/rss/"),
        ("deep-dive", "https://0x00sec.org/deep-dive-series/rss/"),
    ]
    for tag, url in feeds:
        for item in s.rss(url)[:limit]:
            if item["title"] and item["url"]:
                rows.append(
                    {
                        "type": "thread",
                        "source": "0x00sec",
                        "url": item["url"],
                        "title": item["title"],
                        "author": item["author"],
                        "date": item["date"],
                        "tags": [tag],
                        "summary": clean(item["summary"], 700),
                        "collected_at": NOW(),
                    }
                )
    return rows


def forums_htb(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    for endpoint in ("top.json?t=year", "latest.json"):
        data = s.json(f"https://forum.hackthebox.com/{endpoint}")
        if not isinstance(data, dict):
            continue
        for t in data.get("topic_list", {}).get("topics", [])[:limit]:
            rows.append(
                {
                    "type": "thread",
                    "source": "Hack The Box Forum",
                    "url": f"https://forum.hackthebox.com/t/{t.get('slug')}/{t.get('id')}",
                    "title": t.get("title", ""),
                    "author": "",
                    "date": t.get("created_at", ""),
                    "tags": t.get("tags", []),
                    "summary": clean(t.get("excerpt"), 700),
                    "metrics": {"replies": t.get("posts_count"), "views": t.get("views")},
                    "collected_at": NOW(),
                }
            )
    return rows


def forums_reddit(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    subs = ["netsec", "bugbounty", "AskNetsec", "ReverseEngineering", "websecurity", "blueteamsec"]
    for sub in subs:
        base = f"https://sh.reddit.com/r/{sub}"
        s.get(base, "text")
        html = s.get(f"{base}/top/?t=year", "html", wait_ms=3500)
        if not html:
            continue
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        for post in soup.select("shreddit-post")[:limit]:
            title, permalink = post.get("post-title"), post.get("permalink")
            if not title or not permalink:
                continue
            rows.append(
                {
                    "type": "thread",
                    "source": f"r/{sub}",
                    "url": "https://www.reddit.com" + permalink,
                    "title": title,
                    "author": post.get("author", ""),
                    "date": post.get("created-timestamp", ""),
                    "tags": [sub],
                    "summary": "",
                    "metrics": {"score": post.get("score"), "comments": post.get("comment-count")},
                    "collected_at": NOW(),
                }
            )
    return rows


def forums_hackerone(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    for page in range(4):
        url = (
            "https://hackerone.com/hacktivity/overview?queryString=disclosed%3Atrue"
            f"&sortField=latest_disclosable_activity_at&sortDirection=DESC&pageIndex={page}"
        )
        html = s.get(url, wait_ms=6500)
        if not html:
            continue
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.select('[data-testid="hacktivity-item"]')[:limit]:
            rep = item.select_one('a[href*="/reports/"]')
            if not rep:
                continue
            lines = [clean(x) for x in item.get_text("\n", strip=True).splitlines() if clean(x)]
            user = item.select_one('a[href*="type=user"]')
            rows.append(
                {
                    "type": "thread",
                    "source": "HackerOne Hacktivity",
                    "url": urllib.parse.urljoin("https://hackerone.com", rep["href"]),
                    "title": clean(rep.get_text(" ", strip=True)),
                    "author": user.get_text(strip=True) if user else "",
                    "date": "",
                    "tags": ["disclosed", "hackerone"],
                    "summary": max(lines, key=len)[:700] if lines else "",
                    "metrics": {
                        "program": lines[0] if lines else "",
                        "weakness": lines[1] if len(lines) > 1 else "",
                        "severity": lines[2] if len(lines) > 2 else "",
                        "bounty": next((x for x in lines if x.startswith("$")), ""),
                        "status": next((x for x in lines if x in ("Resolved", "Informative", "Duplicate")), ""),
                    },
                    "collected_at": NOW(),
                }
            )
    return rows


def forums_intigriti(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    base = "https://www.intigriti.com/researchers/blog"
    html = s.get(base)
    if not html:
        return rows
    for href, text in extract_links(html, base):
        if "/researchers/blog/" in href and len(text) > 15 and href.count("/") >= 5:
            parts = href.rstrip("/").split("/")
            rows.append(
                {
                    "type": "thread",
                    "source": "Intigriti",
                    "url": href,
                    "title": text,
                    "author": "",
                    "date": "",
                    "tags": [parts[-2]],
                    "summary": "",
                    "collected_at": NOW(),
                }
            )
            if len(rows) >= limit:
                break
    return rows


def solve_cloudflare(s: CamoSession, url: str, max_wait: int = 50) -> str:
    """Open a Cloudflare-protected page and wait for the challenge to clear."""
    s.page.goto(url, wait_until="domcontentloaded", timeout=60_000)
    for _ in range(max_wait // 5):
        s.page.wait_for_timeout(5_000)
        title = s.page.title()
        if "Just a moment" not in title and "Challenge" not in title:
            break
        try:
            frame = s.page.frame_locator("iframe[src*='challenges.cloudflare.com']")
            box = frame.locator("input[type=checkbox]")
            if box.count():
                box.first.click(timeout=3_000)
        except Exception:
            pass
    return s.page.content()


def forums_hackforums(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    ads = ("DARKVPS", "Spoof Call", "WEB PENTEST", "Best Crypter", "LEARN HOW TO MAKE")
    sections = [
        (43, "website-hacking"),
        (4, "beginner-hacking"),
        (10, "hacking-tools"),
        (447, "blackhat-redteam"),
        (45, "exploits"),
        (287, "malware"),
    ]
    per_section = max(2, limit // len(sections))
    seen = set()
    home = solve_cloudflare(s, "https://hackforums.net/")
    for fid, slug in sections:
        url = f"https://hackforums.net/forumdisplay.php?fid={fid}"
        try:
            s.page.goto(url, wait_until="domcontentloaded", timeout=60_000)
            s.page.wait_for_timeout(5_000)
            html = s.page.content()
            if "Just a moment" in s.page.title():
                html = solve_cloudflare(s, url, max_wait=30)
        except Exception:
            continue
        added = 0
        for href, text in extract_links(html or "", url):
            if "showthread.php?tid=" not in href or not text or href in seen:
                continue
            if any(ad.lower() in text.lower() for ad in ads) or len(text) < 12:
                continue
            seen.add(href)
            rows.append(
                {
                    "type": "thread",
                    "source": "HackForums",
                    "url": href,
                    "title": text,
                    "author": "",
                    "date": "",
                    "tags": ["hackforums", slug],
                    "summary": "",
                    "forum": slug,
                    "collected_at": NOW(),
                }
            )
            added += 1
            if added >= per_section:
                break
        s._polite()
    if not rows and home:
        for href, text in extract_links(home, "https://hackforums.net/"):
            if "showthread.php?tid=" in href and text and href not in seen:
                if any(ad.lower() in text.lower() for ad in ads):
                    continue
                seen.add(href)
                rows.append(
                    {
                        "type": "thread",
                        "source": "HackForums",
                        "url": href,
                        "title": text,
                        "author": "",
                        "date": "",
                        "tags": ["hackforums"],
                        "summary": "",
                        "collected_at": NOW(),
                    }
                )
                if len(rows) >= limit:
                    break
    return rows[: limit * 2]


def forums_hn(s: CamoSession, limit: int) -> list[dict]:
    data = s.json("https://hn.algolia.com/api/v1/search_by_date?query=security&tags=story&hitsPerPage=100")
    rows = []
    for h in (data or {}).get("hits", [])[:limit]:
        if not h.get("title"):
            continue
        rows.append(
            {
                "type": "thread",
                "source": "Hacker News",
                "url": h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                "title": h["title"],
                "author": h.get("author", ""),
                "date": h.get("created_at", ""),
                "tags": ["hn", "security"],
                "summary": "",
                "metrics": {"points": h.get("points"), "comments": h.get("num_comments")},
                "collected_at": NOW(),
            }
        )
    return rows


def forums_lobsters(s: CamoSession, limit: int) -> list[dict]:
    data = s.json("https://lobste.rs/t/security.json") or []
    rows = []
    for h in data[:limit]:
        rows.append(
            {
                "type": "thread",
                "source": "Lobsters",
                "url": h.get("url") or h.get("comments_url", ""),
                "title": h.get("title", ""),
                "author": h.get("submitter", ""),
                "date": h.get("created_at", ""),
                "tags": ["lobsters", "security"],
                "summary": "",
                "metrics": {"score": h.get("score"), "comments": h.get("comment_count")},
                "collected_at": NOW(),
            }
        )
    return rows


def forums_fulldisclosure(s: CamoSession, limit: int) -> list[dict]:
    base = "https://seclists.org/fulldisclosure/"
    html = s.get(base)
    rows = []
    for href, text in extract_links(html or "", base):
        if "fulldisclosure/20" in href and len(text) > 5:
            rows.append(
                {
                    "type": "thread",
                    "source": "Full Disclosure",
                    "url": href,
                    "title": text,
                    "author": "",
                    "date": "",
                    "tags": ["fulldisclosure", "advisory"],
                    "summary": "",
                    "collected_at": NOW(),
                }
            )
            if len(rows) >= limit:
                break
    return rows


def forums_rss(s: CamoSession, limit: int, name: str, url: str) -> list[dict]:
    rows = []
    for item in s.rss(url)[:limit]:
        if not item["title"] or not item["url"]:
            continue
        rows.append(
            {
                "type": "thread",
                "source": name,
                "url": item["url"],
                "title": item["title"],
                "author": item["author"],
                "date": item["date"],
                "tags": ["research"],
                "summary": clean(item["summary"], 600),
                "collected_at": NOW(),
            }
        )
    return rows


def forums_projectzero(s: CamoSession, limit: int) -> list[dict]:
    return forums_rss(s, limit, "Project Zero", "https://googleprojectzero.blogspot.com/feeds/posts/default?alt=rss")


def forums_watchtowr(s: CamoSession, limit: int) -> list[dict]:
    return forums_rss(s, limit, "watchTowr Labs", "https://labs.watchtowr.com/rss/")


def forums_horizon3(s: CamoSession, limit: int) -> list[dict]:
    return forums_rss(s, limit, "Horizon3", "https://horizon3.ai/feed/")


def forums_trailofbits(s: CamoSession, limit: int) -> list[dict]:
    return forums_rss(s, limit, "Trail of Bits", "https://blog.trailofbits.com/feed/")


def forums_nccgroup(s: CamoSession, limit: int) -> list[dict]:
    return forums_rss(s, limit, "NCC Group", "https://research.nccgroup.com/feed/")


def forums_bugcrowd(s: CamoSession, limit: int) -> list[dict]:
    return forums_rss(s, limit, "Bugcrowd", "https://www.bugcrowd.com/blog/feed/")


def forums_portswigger_rss(s: CamoSession, limit: int) -> list[dict]:
    return forums_rss(s, limit, "PortSwigger Research", "https://portswigger.net/research/rss")


def forums_mastodon(s: CamoSession, limit: int) -> list[dict]:
    data = s.json("https://infosec.exchange/api/v1/timelines/public?limit=40&local=true") or []
    rows = []
    for item in data[:limit]:
        from bs4 import BeautifulSoup

        text = BeautifulSoup(item.get("content", ""), "html.parser").get_text(" ", strip=True)
        rows.append(
            {
                "type": "thread",
                "source": "infosec.exchange",
                "url": item.get("url", ""),
                "title": clean(text, 140),
                "author": (item.get("account") or {}).get("acct", ""),
                "date": item.get("created_at", ""),
                "tags": ["mastodon"],
                "summary": clean(text, 600),
                "metrics": {"reblogs": item.get("reblogs_count"), "favourites": item.get("favourites_count")},
                "collected_at": NOW(),
            }
        )
    return rows


def forums_seclists(s: CamoSession, limit: int, name: str, path: str) -> list[dict]:
    base = f"https://seclists.org/{path}/"
    html = s.get(base)
    months = [(h, t) for h, t in extract_links(html or "", base) if re.search(rf"/{path}/20\d\d/[A-Z][a-z]{{2}}/$", h)]
    if not months:
        return []
    month, _ = months[0]
    page = s.get(month)
    rows = []
    for href, text in extract_links(page or "", month):
        if re.search(rf"/{path}/20\d\d/[A-Z][a-z]{{2}}/\d+$", href) and len(text) > 5:
            rows.append(
                {
                    "type": "thread",
                    "source": name,
                    "url": href,
                    "title": text,
                    "author": "",
                    "date": "",
                    "tags": [path],
                    "summary": "",
                    "collected_at": NOW(),
                }
            )
            if len(rows) >= limit:
                break
    return rows


def forums_bugtraq(s: CamoSession, limit: int) -> list[dict]:
    return forums_seclists(s, limit, "Bugtraq", "bugtraq")


def forums_webappsec(s: CamoSession, limit: int) -> list[dict]:
    return forums_seclists(s, limit, "WebAppSec", "webappsec")


FORUMS = {
    "0x00sec": forums_0x00sec,
    "htb": forums_htb,
    "reddit": forums_reddit,
    "hackerone": forums_hackerone,
    "intigriti": forums_intigriti,
    "hackforums": forums_hackforums,
    "hn": forums_hn,
    "lobsters": forums_lobsters,
    "fulldisclosure": forums_fulldisclosure,
    "projectzero": forums_projectzero,
    "watchtowr": forums_watchtowr,
    "horizon3": forums_horizon3,
    "trailofbits": forums_trailofbits,
    "nccgroup": forums_nccgroup,
    "bugcrowd": forums_bugcrowd,
    "portswigger_rss": forums_portswigger_rss,
    "mastodon": forums_mastodon,
    "bugtraq": forums_bugtraq,
    "webappsec": forums_webappsec,
}


# ----------------------------------------------------------------- experts


def experts_curated(s: CamoSession, limit: int) -> list[dict]:
    return [
        {
            "type": "expert",
            "source": "curated",
            "name": name,
            "handle": handle,
            "profile": profile,
            "focus": focus,
            "works": [],
            "collected_at": NOW(),
        }
        for handle, name, profile, focus in CURATED_EXPERTS[:limit]
    ]


def experts_portswigger(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    handles = ["james-kettle", "gareth-heyes", "zakhar-fedotkin", "tom-stacey", "alex-craig"]
    skip = {"/research", "/research/articles", "/research/talks", "/research/rss"}
    for handle in handles[:limit]:
        url = f"https://portswigger.net/research/{handle}"
        html = s.get(url)
        if not html:
            continue
        works, seen = [], set()
        for href, text in extract_links(html, url):
            if "/research/" not in href or href in skip or href.rstrip("/").endswith(handle):
                continue
            if len(text) < 15 or href in seen:
                continue
            seen.add(href)
            text = re.sub(r"\s+\d{1,2}\s+[A-Z][a-z]+\s+\d{4}\s+", " ", text).strip()
            works.append({"title": text, "url": href})
        rows.append(
            {
                "type": "expert",
                "source": "PortSwigger Research",
                "name": handle.replace("-", " ").title(),
                "handle": handle,
                "profile": url,
                "focus": "web exploitation and research",
                "works": works[:12],
                "collected_at": NOW(),
            }
        )
    return rows


def experts_hackerone(s: CamoSession, limit: int) -> list[dict]:
    found: dict[str, dict] = {}
    for page in range(4):
        url = (
            "https://hackerone.com/hacktivity/overview?queryString=disclosed%3Atrue"
            f"&sortField=latest_disclosable_activity_at&sortDirection=DESC&pageIndex={page}"
        )
        html = s.get(url, wait_ms=6500)
        if not html:
            continue
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        for item in soup.select('[data-testid="hacktivity-item"]'):
            rep, user = item.select_one('a[href*="/reports/"]'), item.select_one('a[href*="type=user"]')
            if not rep or not user:
                continue
            handle = clean(user.get_text())
            if not handle:
                continue
            lines = [clean(x) for x in item.get_text("\n", strip=True).splitlines()]
            row = found.setdefault(
                handle,
                {
                    "type": "expert",
                    "source": "HackerOne Hacktivity",
                    "name": handle,
                    "handle": handle,
                    "profile": urllib.parse.urljoin("https://hackerone.com", user["href"]),
                    "focus": "disclosed HackerOne reports",
                    "works": [],
                    "collected_at": NOW(),
                },
            )
            if len(row["works"]) < 12:
                row["works"].append(
                    {
                        "title": clean(rep.get_text(" ", strip=True)),
                        "url": urllib.parse.urljoin("https://hackerone.com", rep["href"]),
                        "severity": lines[2] if len(lines) > 2 else "",
                    }
                )
    return list(found.values())[:limit]


def experts_intigriti(s: CamoSession, limit: int) -> list[dict]:
    rows, base = [], "https://www.intigriti.com/researchers/blog"
    html = s.get(base)
    if not html:
        return rows
    for href, text in extract_links(html, base):
        if "hacker-spotlight" in href and len(text) > 20:
            rows.append(
                {
                    "type": "expert",
                    "source": "Intigriti",
                    "name": text,
                    "handle": "",
                    "profile": href,
                    "focus": "hacker spotlight interview",
                    "works": [{"title": text, "url": href}],
                    "collected_at": NOW(),
                }
            )
    return rows[:limit]


EXPERTS = {
    "curated": experts_curated,
    "portswigger": experts_portswigger,
    "hackerone": experts_hackerone,
    "intigriti": experts_intigriti,
}


# ------------------------------------------------------------------- tools


def tools_canonical(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    for category, repos in CANONICAL_TOOLS.items():
        for repo in repos:
            if len(rows) >= limit:
                return rows
            page_url = f"https://github.com/{repo}"
            html = s.get(page_url)
            if not html:
                continue
            readme = ""
            for branch in ("HEAD", "main", "master"):
                readme = s.get(f"https://raw.githubusercontent.com/{repo}/{branch}/README.md", "text")
                if readme:
                    break
            m = re.search(r'"stargazerCount":(\d+)', html)
            desc = re.search(r'<meta name="description" content="([^"]*)"', html)
            description = clean(desc.group(1) if desc else "").split("Contribute to")[0].strip()
            lang = re.search(r'"primaryLanguage":\s*\{\s*"name":\s*"([^"]+)"', html)
            install = []
            for line in readme.splitlines():
                cmd = line.strip().strip("`$ ").strip()
                if re.match(
                    r"^(go install|pip3? install|brew install|cargo install|git clone|docker (run|pull)|apt(-get)? install|npm (i|install))",
                    cmd,
                ):
                    install.append(cmd[:200])
                if len(install) >= 3:
                    break
            flags = sorted(set(re.findall(r"(?<![\w-])(--[a-zA-Z][a-zA-Z0-9-]{1,22})", readme[:12000])))[:18]
            rows.append(
                {
                    "type": "tool",
                    "source": "canonical",
                    "category": category,
                    "repo": page_url,
                    "name": repo,
                    "description": description,
                    "stars": m.group(1) if m else "",
                    "language": lang.group(1) if lang else "",
                    "install": install,
                    "flags": flags,
                    "collected_at": NOW(),
                }
            )
    return rows


def tools_topics(s: CamoSession, limit: int) -> list[dict]:
    rows, topics = (
        [],
        [
            "bug-bounty",
            "recon",
            "penetration-testing",
            "red-team",
            "osint",
            "fuzzing",
            "rce-exploit",
            "exploit",
            "payload",
            "subdomain",
            "web-security",
            "reverse-engineering",
        ],
    )
    for topic in topics:
        for sort in ("stars", "updated"):
            html = s.get(f"https://github.com/topics/{topic}?o=desc&s={sort}")
            if not html:
                continue
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html, "html.parser")
            for art in soup.select("article"):
                link = art.select_one("h3 a:last-child")
                if not link:
                    continue
                repo = urllib.parse.urljoin("https://github.com/", link["href"])
                atext = art.get_text(" ", strip=True).replace("\xa0", " ")
                stars = re.search(r"Star\s+([\d.,]+k?)", atext)
                desc = art.select_one("p")
                lang = art.select_one('[itemprop="programmingLanguage"]')
                rows.append(
                    {
                        "type": "tool",
                        "source": f"github/topics/{topic}",
                        "category": topic,
                        "repo": repo,
                        "name": repo.split("github.com/")[-1],
                        "description": clean(desc.get_text(" ") if desc else ""),
                        "stars": stars.group(1) if stars else "",
                        "language": clean(lang.get_text()) if lang else "",
                        "install": [],
                        "flags": [],
                        "collected_at": NOW(),
                    }
                )
            if len(rows) >= limit:
                return rows
    return rows


TOOLS = {"canonical": tools_canonical, "topics": tools_topics}


# ----------------------------------------------------------------- methods


def methods_listing(s: CamoSession, limit: int) -> list[dict]:
    rows = []
    sources = [
        ("PortSwigger Research", "https://portswigger.net/research", "/research/"),
        ("ProjectDiscovery Blog", "https://projectdiscovery.io/blog", "/blog/"),
        ("Intigriti", "https://www.intigriti.com/researchers/blog", "/researchers/blog/"),
        ("HackerOne Blog", "https://www.hackerone.com/blog", "/blog/"),
        ("0x00sec", "https://0x00sec.org/", "0x00sec.org/"),
    ]
    for source, base, needle in sources:
        html = s.get(base)
        if not html:
            continue
        count = 0
        for href, text in extract_links(html, base):
            if needle not in href or len(text) < 12 or "/topic/" in href:
                continue
            if re.search(r"/research/(james|gareth|zakhar|tom-stacey|alex-craig)", href):
                continue
            text = re.sub(r"\s+\d{1,2}\s+[A-Z][a-z]+\s+\d{4}\s+", " ", text).strip()
            rows.append({"type": "method", "source": source, "url": href, "title": text, "collected_at": NOW()})
            count += 1
            if count >= limit:
                break
    fixed = [
        ("OWASP WSTG", "https://owasp.org/www-project-web-security-testing-guide/latest/"),
        ("OWASP MASTG", "https://mas.owasp.org/MASTG/"),
        ("OWASP ASVS", "https://owasp.org/www-project-application-security-verification-standard/"),
        ("OWASP Cheat Sheets", "https://cheatsheetseries.owasp.org/"),
        ("PTES", "http://www.pentest-standard.org/index.php/Main_Page"),
        ("MITRE ATT&CK", "https://attack.mitre.org/"),
        ("HackTricks", "https://book.hacktricks.wiki/"),
        ("PayloadsAllTheThings", "https://github.com/swisskyrepo/PayloadsAllTheThings"),
        ("Bugcrowd VRT", "https://bugcrowd.com/vulnerability-rating-taxonomy"),
        ("PortSwigger Web Security Academy", "https://portswigger.net/web-security"),
    ]
    for name, url in fixed:
        rows.append({"type": "method", "source": name, "url": url, "title": name + " reference", "collected_at": NOW()})
    return rows


METHODS = {"listing": methods_listing}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["forums", "experts", "tools", "methods", "all"])
    ap.add_argument("--sources", default="", help="comma separated source names")
    ap.add_argument("--out", default="", help="JSONL output for one command")
    ap.add_argument("--out-dir", default="data", help="directory for 'all'")
    ap.add_argument("--limit", type=int, default=40, help="items per source or total for tools")
    ap.add_argument("--delay", type=float, default=1.2, help="minimum seconds between requests")
    ap.add_argument("--headful", action="store_true", help="show the browser window")
    ap.add_argument("--cache", default="raw", help="cache directory, empty string disables")
    ap.add_argument("--fresh", action="store_true", help="ignore the cache")
    ap.add_argument("--profile", default="", help="persistent browser profile directory (for challenge clearance)")
    args = ap.parse_args()

    tables = {"forums": FORUMS, "experts": EXPERTS, "tools": TOOLS, "methods": METHODS}
    jobs = []
    if args.command == "all":
        for cmd, table in tables.items():
            os.makedirs(args.out_dir, exist_ok=True)
            for name in table:
                jobs.append(
                    (
                        cmd,
                        name,
                        table[name],
                        os.path.join(
                            args.out_dir,
                            {
                                "forums": "threads.jsonl",
                                "experts": "experts.jsonl",
                                "tools": "tools.jsonl",
                                "methods": "methods.jsonl",
                            }[cmd],
                        ),
                    )
                )
    else:
        table = tables[args.command]
        chosen = [x for x in args.sources.split(",") if x] or list(table)
        unknown = [x for x in chosen if x not in table]
        if unknown:
            ap.error(f"unknown source(s): {unknown}. Choose from {list(table)}")
        out = args.out or os.path.join(
            args.out_dir,
            {"forums": "threads.jsonl", "experts": "experts.jsonl", "tools": "tools.jsonl", "methods": "methods.jsonl"}[
                args.command
            ],
        )
        jobs = [(args.command, name, table[name], out) for name in chosen]

    total = 0
    with CamoSession(
        headless=not args.headful,
        min_delay=args.delay,
        max_delay=args.delay + 1.2,
        cache_dir=args.cache or None,
        fresh=args.fresh,
        persistent_context=bool(args.profile),
        user_data_dir=args.profile or None,
    ) as session:
        for cmd, name, fn, target in jobs:
            print(f"== {cmd}:{name}")
            try:
                rows = fn(session, args.limit)
            except Exception as exc:
                print(f"  failed: {type(exc).__name__}: {str(exc)[:140]}")
                continue
            for row in rows:
                risk = guard.analyze(row.get("summary") or row.get("title") or "")
                row["prompt_risk"] = risk["level"]
                row["treat_as"] = "data"
            n = write_jsonl(target, rows)
            total += len(rows)
            print(f"  {len(rows)} rows, {n} unique in {target}")
    print(f"done, {total} new rows")


if __name__ == "__main__":
    main()
