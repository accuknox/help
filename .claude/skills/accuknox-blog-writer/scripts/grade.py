#!/usr/bin/env python3
"""Score an AccuKnox blog draft on the mechanics a human should not have to count.

This is the deterministic half of the SEO audit. It measures what a regex can
measure: front matter completeness, title and description lengths, heading
hierarchy, keyword placement, link counts, word count, reading time, TL;DR and
FAQ presence, image captions and passive voice. It says nothing about whether
the argument is any good. That judgement stays with the writer and with
`references/seo-audit.md`.

A page fetched from accuknox.com carries `markdown_url` in its front matter.
The script detects that and reports the SEO fields as not provided, because on
a published post they live in WordPress. Force either mode with `--draft` or
`--published`.

Usage:
    python grade.py draft.md
    python grade.py draft.md --json
    python grade.py draft.md --min-words 1200
    python grade.py fetched.md --published

Exit codes: 0 no CRITICAL findings, 1 at least one CRITICAL finding.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WPM = 200  # accuknox.com reading times match 200 words per minute

REQUIRED_FM = [
    "title", "seo_title", "meta_description", "slug", "url",
    "primary_keyword", "secondary_keywords", "excerpt", "category",
    "reading_time", "cover_image_prompt_claude", "cover_image_prompt_midjourney",
]

FAQ_HEADINGS = ("faq", "faqs", "frequently asked questions")

PASSIVE = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?\w+(ed|en|own|ung)\b", re.I)

WEAK_HEADING = re.compile(
    r"^(understanding|introduction|overview|what is|background|conclusion|"
    r"getting started|key takeaways|benefits|features|challenges)\b", re.I)


class Report:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []
        self.scores: dict[str, int] = {}

    def add(self, level: str, area: str, msg: str) -> None:
        self.rows.append((level, area, msg))

    def count(self, level: str) -> int:
        return sum(1 for lv, _, _ in self.rows if lv == level)


def split_front_matter(text: str) -> tuple[dict[str, str], str, int]:
    """Return (front matter as raw strings, body, body start line)."""
    if not text.startswith("---"):
        return {}, text, 1
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text, 1
    raw = text[3:end]
    body = text[end + 4:].lstrip("\n")
    fm: dict[str, str] = {}
    key = None
    for line in raw.splitlines():
        m = re.match(r"^([a-z_][a-z0-9_]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            fm[key] = m.group(2).strip()
        elif key and line.strip():
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm, body, raw.count("\n") + 3


def unquote(v: str) -> str:
    v = v.strip()
    if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v.lstrip(">|").strip()


def headings(body: str) -> list[tuple[int, str, int]]:
    out = []
    for i, line in enumerate(body.splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out.append((len(m.group(1)),
                        re.sub(r"\*\*|__|`", "", m.group(2)).strip(), i))
    return out


def prose_words(body: str) -> int:
    t = re.sub(r"```.*?```", " ", body, flags=re.S)
    t = re.sub(r"^\s*\|.*\|\s*$", " ", t, flags=re.M)
    t = re.sub(r"^#{1,6}.*$", " ", t, flags=re.M)
    return len(t.split())


def grade(path: Path, min_words: int, published: bool | None = None) -> Report:
    text = path.read_text("utf-8")
    fm, body, _ = split_front_matter(text)
    r = Report()
    hs = headings(body)
    words = prose_words(body)
    kw = unquote(fm.get("primary_keyword", "")).lower()

    # A page fetched from accuknox.com carries `markdown_url` in its front
    # matter. Its SEO fields live in WordPress, not in the markdown, so report
    # them as not provided rather than as authoring failures.
    if published is None:
        published = "markdown_url" in fm
    missing_level = "INFO" if published else "CRITICAL"

    # --- Front matter -----------------------------------------------------
    fm_score = 100
    for key in REQUIRED_FM:
        if key not in fm or not unquote(fm[key]):
            r.add(missing_level, "front-matter",
                  f"`{key}` not provided" if published else f"missing `{key}`")
            if not published:
                fm_score -= 100 // len(REQUIRED_FM)
    if published:
        r.add("INFO", "front-matter",
              "published page. SEO fields live in WordPress, so the front "
              "matter score is not scored")
        fm_score = 100

    seo_title = unquote(fm.get("seo_title", ""))
    if seo_title:
        n = len(seo_title)
        if not 45 <= n <= 60:
            r.add("HIGH", "front-matter",
                  f"seo_title is {n} chars, target 45 to 60")
            fm_score -= 8
        if kw and kw not in seo_title.lower():
            r.add("HIGH", "front-matter",
                  f"seo_title omits the primary keyword `{kw}`")
            fm_score -= 8

    desc = unquote(fm.get("meta_description", ""))
    if desc:
        n = len(desc)
        if not 150 <= n <= 160:
            r.add("HIGH", "front-matter",
                  f"meta_description is {n} chars, target 150 to 160")
            fm_score -= 8
        if kw and kw not in desc.lower():
            r.add("HIGH", "front-matter",
                  f"meta_description omits the primary keyword `{kw}`")
            fm_score -= 8

    slug = unquote(fm.get("slug", ""))
    if slug:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
            r.add("HIGH", "front-matter",
                  f"slug `{slug}` must be lowercase words joined by hyphens")
            fm_score -= 8
        if len(slug) > 65:
            r.add("MEDIUM", "front-matter",
                  f"slug is {len(slug)} chars, keep it under 65")
        url = unquote(fm.get("url", ""))
        if url and not url.endswith(f"/blog/{slug}"):
            r.add("HIGH", "front-matter",
                  f"url does not end in /blog/{slug}")
            fm_score -= 8

    rt = unquote(fm.get("reading_time", ""))
    expected = max(1, round(words / WPM))
    m = re.search(r"\d+", rt)
    if m and abs(int(m.group()) - expected) > 1:
        r.add("MEDIUM", "front-matter",
              f"reading_time says {m.group()} min, {words} words is "
              f"~{expected} min at {WPM} wpm")
    r.scores["Front matter"] = max(0, min(100, fm_score))

    # --- Structure --------------------------------------------------------
    st = 100
    h1 = [h for h in hs if h[0] == 1]
    if len(h1) != 1:
        r.add("CRITICAL", "structure", f"{len(h1)} H1 headings, need exactly 1")
        st -= 30
    elif kw and kw not in h1[0][1].lower():
        r.add("MEDIUM", "structure",
              f"H1 omits the primary keyword `{kw}`")
        st -= 5

    prev = 0
    for level, title, line in hs:
        if prev and level > prev + 1:
            r.add("HIGH", "structure",
                  f"line {line}: H{level} follows H{prev}, no skipped levels")
            st -= 6
        prev = level
        if level == 2 and WEAK_HEADING.match(title):
            r.add("MEDIUM", "structure",
                  f"line {line}: heading states a topic, not a conclusion: "
                  f"\"{title}\"")
            st -= 3
        # A question mark or a `Q:` prefix is FAQ convention, not a label colon.
        if (":" in title and level > 1 and not title.endswith("?")
                and not re.match(r"^Q\s*:", title)):
            r.add("MEDIUM", "structure",
                  f"line {line}: no colon in a heading: \"{title}\"")
            st -= 2

    labels = [t.lower().strip("* ") for _, t, _ in hs]
    if not any(l.startswith("tl;dr") for l in labels):
        r.add("CRITICAL", "structure", "no TL;DR section")
        st -= 20
    if not any(l.startswith(FAQ_HEADINGS) for l in labels):
        r.add("HIGH", "structure", "no FAQ section")
        st -= 15
    else:
        idx = next(i for i, l in enumerate(labels) if l.startswith(FAQ_HEADINGS))
        qs = sum(1 for lv, _, _ in hs[idx + 1:] if lv == 3)
        if qs < 3:
            r.add("HIGH", "structure",
                  f"FAQ has {qs} questions, write 3 to 5")
            st -= 8

    h2s = sum(1 for lv, _, _ in hs if lv == 2)
    if h2s < 4:
        r.add("HIGH", "structure", f"{h2s} H2 sections, write at least 4")
        st -= 10
    r.scores["Structure"] = max(0, min(100, st))

    # --- Content ----------------------------------------------------------
    ct = 100
    if words < min_words:
        r.add("HIGH", "content",
              f"{words} prose words, floor for this channel is {min_words}")
        ct -= 15
    if words > 2600:
        r.add("MEDIUM", "content",
              f"{words} prose words, recent AccuKnox posts run 1200 to 2000")

    paras = [p for p in re.split(r"\n\s*\n", body)
             if p.strip() and not p.lstrip().startswith(("#", "|", "-", "*",
                                                         ">", "```", "1."))]
    two_liners = sum(1 for p in paras
                     if 1 <= len(re.findall(r"[.!?](?:\s|$)", p)) <= 2)
    if paras and two_liners / len(paras) > 0.5:
        r.add("MEDIUM", "content",
              f"{two_liners} of {len(paras)} paragraphs run one or two "
              "sentences. Three to four builds an argument "
              "(writing-rules section 5)")
        ct -= 8

    sents = [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\n+", " ", body))
             if len(s.split()) > 3]
    passive_hits = sum(1 for s in sents if PASSIVE.search(s))
    if sents and passive_hits / len(sents) > 0.15:
        r.add("MEDIUM", "content",
              f"{passive_hits} of {len(sents)} sentences look passive, "
              "target under 15%")
        ct -= 6

    if kw:
        hits = len(re.findall(re.escape(kw), body, re.I))
        density = 100 * hits * len(kw.split()) / max(words, 1)
        if hits == 0:
            r.add("CRITICAL", "content",
                  f"primary keyword `{kw}` never appears in the body")
            ct -= 25
        elif density > 3:
            r.add("HIGH", "content",
                  f"primary keyword density {density:.1f}%, keep it under 3%")
            ct -= 10
        elif density < 0.4:
            r.add("MEDIUM", "content",
                  f"primary keyword density {density:.1f}%, aim for 0.5 to 2%")
            ct -= 4

        first150 = " ".join(body.split()[:150]).lower()
        if kw not in first150:
            r.add("HIGH", "content",
                  f"primary keyword `{kw}` is absent from the first 150 "
                  "words (writing-rules section 11)")
            ct -= 10

    numbers = len(re.findall(r"\b\d[\d,.]*\s*(%|percent|ms|s\b|GB|MB|CVE|"
                             r"minutes|hours|days)", body, re.I))
    if numbers < 3:
        r.add("MEDIUM", "content",
              f"only {numbers} concrete figures with units. Specifics are "
              "what an answer engine quotes")
        ct -= 5
    r.scores["Content"] = max(0, min(100, ct))

    # --- Links ------------------------------------------------------------
    # A URL inside a fence is an argument to a command, not a link in the prose.
    prose = re.sub(r"```.*?```", "", body, flags=re.S)
    prose = re.sub(r"`[^`\n]+`", "", prose)
    lk = 100
    links = re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)\)", prose)
    internal = [u for _, u in links if "accuknox.com" in u]
    external = [u for _, u in links if "accuknox.com" not in u]
    helpdocs = [u for u in internal if "help.accuknox.com" in u]
    if len(internal) < 3:
        r.add("HIGH", "links",
              f"{len(internal)} accuknox.com links, add at least 3 inline")
        lk -= 20
    if not helpdocs:
        r.add("MEDIUM", "links",
              "no help.accuknox.com link. A product claim should reach the doc "
              "that proves it")
        lk -= 10
    if not external:
        r.add("HIGH", "links",
              "no external citation. Every standard, CVE and third-party claim "
              "needs its source (writing-rules section 9)")
        lk -= 20
    for anchor, url in links:
        if anchor.strip().lower() in ("click here", "here", "read more",
                                      "this", "link", ""):
            r.add("HIGH", "links", f"weak anchor text \"{anchor}\" -> {url}")
            lk -= 5
    bare = re.findall(r"(?<![(\[<])\bhttps?://[^\s)>\]]+", prose)
    if bare:
        r.add("HIGH", "links",
              f"{len(bare)} bare URL(s) in prose, wrap each in link text")
        lk -= 8
    r.scores["Links"] = max(0, min(100, lk))

    # --- Images -----------------------------------------------------------
    im = 100
    imgs = re.findall(r"!\[([^\]]*)\]\(([^)\s]+)", body)
    placeholders = re.findall(r"^\s*>\s*\*\*Image prompt", body, re.M)
    if not imgs and not placeholders:
        r.add("HIGH", "images",
              "no image and no image prompt. Recent posts carry 2 to 4")
        im -= 40
    for alt, src in imgs:
        if not alt.strip():
            r.add("CRITICAL", "images", f"empty alt text on {src}")
            im -= 20
        elif re.match(r"^(a )?(screenshot|image|picture|diagram) of ", alt, re.I):
            r.add("MEDIUM", "images",
                  f"alt text describes the file, not the point: \"{alt}\"")
            im -= 8
    captions = re.findall(r"^\s*\*[^*\n]{15,}\*\s*$", body, re.M)
    if imgs and len(captions) < len(imgs):
        r.add("MEDIUM", "images",
              f"{len(imgs)} images, {len(captions)} italic captions. "
              "Every image gets one")
        im -= 10
    r.scores["Images"] = max(0, min(100, im))

    # --- AI citation readiness -------------------------------------------
    ai = 100
    tldr = re.search(r"^#{2,3}\s+\**TL;DR\**\s*$(.*?)(?=^#{2,3}\s)",
                     body, re.S | re.M | re.I)
    if tldr:
        bullets = re.findall(r"^\s*[-*]\s+\S", tldr.group(1), re.M)
        if not 3 <= len(bullets) <= 6:
            r.add("MEDIUM", "ai-citation",
                  f"TL;DR has {len(bullets)} bullets, write 3 to 6")
            ai -= 10
        if not re.search(r"\d", tldr.group(1)):
            r.add("HIGH", "ai-citation",
                  "TL;DR carries no number. An answer engine lifts the figure")
            ai -= 15
    else:
        ai -= 25
    if not any(l.startswith(FAQ_HEADINGS) for l in labels):
        ai -= 20
    if len(re.findall(r"^\s*\|.*\|\s*$", body, re.M)) < 3:
        r.add("MEDIUM", "ai-citation",
              "no comparison table. A table is the easiest block to extract")
        ai -= 10
    r.scores["AI citation"] = max(0, min(100, ai))

    r.scores["Overall"] = round(sum(v for k, v in r.scores.items()) /
                                len(r.scores))
    return r


ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}


def render(path: Path, r: Report) -> str:
    out = [f"SEO grade  {path.name}", ""]
    for name in ("Overall", "Front matter", "Structure", "Content", "Links",
                 "Images", "AI citation"):
        v = r.scores.get(name, 0)
        bar = "#" * (v // 10) + "." * (10 - v // 10)
        out.append(f"  {name:14s} {v:3d}/100  {bar}")
    out.append("")
    if not r.rows:
        out.append("  no findings")
        return "\n".join(out)
    for level in ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"):
        rows = [x for x in r.rows if x[0] == level]
        if not rows:
            continue
        out.append(f"{level} ({len(rows)})")
        for _, area, msg in rows:
            out.append(f"  [{area}] {msg}")
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", type=Path)
    ap.add_argument("--min-words", type=int, default=1200)
    ap.add_argument("--json", action="store_true")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--published", action="store_true",
                      help="treat missing SEO front matter as not provided")
    # dest must not collide with the `draft` positional above.
    mode.add_argument("--draft", dest="force_draft", action="store_true",
                      help="require the full SEO front matter")
    args = ap.parse_args()

    if not args.draft.exists():
        print(f"no such file: {args.draft}", file=sys.stderr)
        return 2
    published = True if args.published else (False if args.force_draft else None)
    r = grade(args.draft, args.min_words, published)
    if args.json:
        print(json.dumps({"file": str(args.draft), "scores": r.scores,
                          "findings": [{"level": a, "area": b, "message": c}
                                       for a, b, c in r.rows]}, indent=2))
    else:
        print(render(args.draft, r))
    return 1 if r.count("CRITICAL") else 0


if __name__ == "__main__":
    raise SystemExit(main())
