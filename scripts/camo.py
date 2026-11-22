"""Small Camoufox session wrapper used by every harvester in this skill.

Camoufox is a Firefox build with fingerprint patches and Playwright's API. This
module adds caching, polite retries and the handful of parsing helpers the
harvesters share. Import it, do not run it.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
import time
import urllib.parse
from dataclasses import dataclass, field
from typing import Iterable

DEFAULT_UA = (
    "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
)


def clean(text: str | None, limit: int | None = None) -> str:
    out = re.sub(r"\s+", " ", text or "").strip()
    return out[:limit] if limit else out


def cache_key(url: str, prefix: str = "") -> str:
    return hashlib.sha1((prefix + url).encode("utf-8")).hexdigest()


def extract_links(html: str, base: str) -> list[tuple[str, str]]:
    """Return (absolute_url, visible_text) pairs."""
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise SystemExit("Install beautifulsoup4: pip install beautifulsoup4 lxml") from exc
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for a in soup.find_all("a", href=True):
        href = urllib.parse.urljoin(base, a["href"])
        out.append((href, clean(a.get_text(" ", strip=True))))
    return out


def absolutize(html: str, base: str) -> str:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    for tag, attr in (("a", "href"), ("img", "src"), ("script", "src"), ("link", "href")):
        for node in soup.find_all(tag):
            if node.get(attr):
                node[attr] = urllib.parse.urljoin(base, node[attr])
    return str(soup)


@dataclass
class CamoSession:
    headless: bool = True
    humanize: bool = True
    locale: str = "en-US"
    os_name: str | None = None
    proxy: str | None = None
    block_images: bool = True
    geoip: bool = True
    cache_dir: str | None = "raw"
    min_delay: float = 1.0
    max_delay: float = 2.2
    page_timeout_ms: int = 60_000
    extra: dict = field(default_factory=dict)
    fresh: bool = False
    persistent_context: bool = False
    user_data_dir: str | None = None

    browser: object | None = None
    page: object | None = None
    _ctx: object | None = None
    _last_request: float = 0.0

    def __enter__(self) -> "CamoSession":
        from camoufox.sync_api import Camoufox

        kwargs = dict(
            headless=self.headless,
            humanize=self.humanize,
            locale=self.locale,
            i_know_what_im_doing=True,
        )
        if self.os_name:
            kwargs["os"] = self.os_name
        if self.proxy:
            kwargs["proxy"] = {"server": self.proxy}
        if self.geoip:
            kwargs["geoip"] = True
        if self.persistent_context:
            kwargs["persistent_context"] = True
            kwargs["user_data_dir"] = self.user_data_dir or "profile"
        kwargs.update(self.extra)
        self._ctx = Camoufox(**kwargs)
        self.browser = self._ctx.__enter__()
        self.page = self.browser.new_page()
        self.page.set_default_timeout(self.page_timeout_ms)
        if self.block_images:
            self.page.route(
                re.compile(r"\.(png|jpe?g|gif|webp|svg|ico|woff2?|ttf|mp4|webm)(\?.*)?$"),
                lambda route: route.abort(),
            )
        if self.cache_dir:
            os.makedirs(self.cache_dir, exist_ok=True)
        return self

    def __exit__(self, *exc) -> None:
        if getattr(self, "_ctx", None):
            self._ctx.__exit__(None, None, None)

    def _polite(self) -> None:
        wait = random.uniform(self.min_delay, self.max_delay)
        elapsed = time.time() - self._last_request
        if elapsed < wait:
            time.sleep(wait - elapsed)

    def get(
        self,
        url: str,
        kind: str = "html",
        retries: int = 3,
        wait_ms: int | None = None,
        selector: str | None = None,
        fresh: bool = False,
    ) -> str | None:
        """Fetch a URL through the browser.

        kind: html (full DOM), text (body text), json (body text parsed later).
        Returns None on a 4xx/5xx after all retries.
        """
        cache_path = None
        if self.cache_dir:
            suffix = {"html": ".html", "text": ".txt", "json": ".json"}.get(kind, ".txt")
            cache_path = os.path.join(self.cache_dir, cache_key(url) + suffix)
            if not (fresh or self.fresh) and os.path.exists(cache_path) and os.path.getsize(cache_path) > 40:
                return open(cache_path, encoding="utf-8", errors="replace").read()

        for attempt in range(1, retries + 1):
            self._polite()
            try:
                resp = self.page.goto(url, wait_until="domcontentloaded", timeout=self.page_timeout_ms)
                self._last_request = time.time()
                if wait_ms:
                    self.page.wait_for_timeout(wait_ms)
                if resp and resp.status >= 400:
                    if resp.status in (403, 429, 503) and attempt < retries:
                        time.sleep(3 + attempt * 4)
                        continue
                    return None
                if selector:
                    self.page.wait_for_selector(selector, timeout=20_000)
                raw = self.page.content() if kind == "html" else self.page.inner_text("body")
                if cache_path and raw:
                    open(cache_path, "w", encoding="utf-8").write(raw)
                return raw
            except Exception as exc:
                if "Download is starting" in str(exc):
                    try:
                        raw = self.page.evaluate("u => fetch(u).then(r => r.text())", url)
                        if cache_path and raw:
                            open(cache_path, "w", encoding="utf-8").write(raw)
                        return raw
                    except Exception:
                        pass
                if attempt == retries:
                    print(f"  ! {url} -> {type(exc).__name__}: {str(exc)[:120]}")
                    return None
                time.sleep(2 + attempt * 2)
        return None

    def json(self, url: str, retries: int = 3) -> dict | list | None:
        raw = self.get(url, "json", retries=retries)
        if not raw:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return None

    def rss(self, url: str) -> list[dict]:
        """Fetch an RSS/Atom feed. Warm the origin first so fetch() is same-origin."""
        origin = "{0.scheme}://{0.netloc}".format(urllib.parse.urlsplit(url))
        try:
            self.page.goto(origin, wait_until="domcontentloaded", timeout=self.page_timeout_ms)
            self._last_request = time.time()
            xml = self.page.evaluate("u => fetch(u).then(r => r.text())", url)
        except Exception:
            xml = self.get(url, "text")
        return parse_feed(xml or "")

    def text_of(self, selector: str) -> str:
        try:
            return clean(self.page.inner_text(selector))
        except Exception:
            return ""

    def headings(self, selector: str = "h2, h3") -> list[str]:
        try:
            values = self.page.eval_on_selector_all(
                selector, "els => els.map(e => e.innerText)"
            )
            return [clean(v) for v in values if 3 < len(clean(v)) < 160]
        except Exception:
            return []

    def snapshot(self, url: str, folder: str = "evidence", label: str | None = None) -> dict:
        """Save DOM, visible text and a full page screenshot as evidence."""
        os.makedirs(folder, exist_ok=True)
        self._polite()
        resp = self.page.goto(url, wait_until="domcontentloaded", timeout=self.page_timeout_ms)
        self.page.wait_for_timeout(1200)
        stem = label or cache_key(url)
        html_path = os.path.join(folder, stem + ".html")
        png_path = os.path.join(folder, stem + ".png")
        txt_path = os.path.join(folder, stem + ".txt")
        open(html_path, "w", encoding="utf-8").write(self.page.content())
        open(txt_path, "w", encoding="utf-8").write(self.page.inner_text("body"))
        try:
            self.page.screenshot(path=png_path, full_page=True)
        except Exception:
            png_path = ""
        return {"url": url, "status": resp.status if resp else None,
                "html": html_path, "text": txt_path, "screenshot": png_path}


def parse_feed(xml: str) -> list[dict]:
    """Minimal RSS/Atom parser that tolerates CDATA and missing fields."""
    items = []
    chunks = re.findall(r"<item\b.*?</item>", xml, re.S) or re.findall(
        r"<entry\b.*?</entry>", xml, re.S
    )
    for block in chunks:
        def value(tag: str) -> str:
            m = re.search(
                rf"<{tag}[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</{tag}>", block, re.S
            )
            if not m:
                return ""
            return clean(re.sub(r"<[^>]+>", "", m.group(1)))

        link = value("link")
        if not link:
            m = re.search(r'<link[^>]+href="([^"]+)"', block)
            link = m.group(1) if m else ""
        items.append({
            "title": value("title"),
            "url": link,
            "author": value("dc:creator") or value("author") or value("name"),
            "date": value("pubDate") or value("updated") or value("published"),
            "summary": value("description") or value("summary") or value("content"),
        })
    return items


def iter_jsonl(path: str) -> Iterable[dict]:
    if not os.path.exists(path):
        return []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def write_jsonl(path: str, rows: Iterable[dict], key_fields=("type", "url", "title")) -> int:
    """Merge, dedupe and write. Returns the number of unique rows."""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    merged = list(iter_jsonl(path)) + list(rows)
    seen, unique = set(), []
    for row in merged:
        ident = (row.get("url") or row.get("repo") or row.get("profile") or row.get("name") or "")
        key = (row.get("type", ""), ident, row.get("title") or row.get("name") or row.get("handle") or "")
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    with open(path, "w", encoding="utf-8") as fh:
        for row in unique:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(unique)
