#!/usr/bin/env python3
"""Validate a press release, case study or comparison against its live format.

`grade.py` scores a blog post on SEO. This scores the other three channels on
structure, because a press release with no dateline and a case study with no
quantified outcome both fail for reasons a search-oriented grader never checks.

Every rule below came from reading the published pages on accuknox.com in
August 2026. The per-channel specs sit in `CHANNELS` and are meant to be edited
when the live format moves.

Usage:
    python check_asset.py draft.md --channel press-release
    python check_asset.py draft.md --channel case-study
    python check_asset.py draft.md --channel comparison
    python check_asset.py draft.md --channel comparison --json

Exit codes: 0 no CRITICAL findings, 1 at least one CRITICAL, 2 bad arguments.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- channel spec

CHANNELS: dict[str, dict] = {
    "press-release": {
        "front_matter": [
            "title", "slug", "url", "release_type", "dateline_city",
            "dateline_date", "excerpt", "contact_name", "contact_email",
        ],
        "url_prefix": "https://accuknox.com/press-release/",
        "words": (350, 950),
        "required_sections": [],
        "min_quotes": 2,
        "max_quotes": 5,
        "needs_about": True,
        "needs_media_contacts": True,
        "min_h2": 2,
        "count_tables": False,
    },
    "case-study": {
        "front_matter": [
            "title", "subtitle", "slug", "url", "customer", "sector",
            "region", "anonymized", "excerpt", "environment", "deployment",
        ],
        "url_prefix": "https://accuknox.com/case-studies/",
        "words": (300, 900),
        "required_sections": ["challenges", "solutions", "outcomes"],
        "min_quotes": 1,
        "max_quotes": 2,
        "needs_about": False,
        "needs_media_contacts": False,
        "min_h2": 3,
        "count_tables": False,
    },
    "comparison": {
        "front_matter": [
            "title", "subtitle", "slug", "url", "archetype", "category",
            "competitors", "excerpt",
        ],
        "url_prefix": "https://accuknox.com/comparisons/",
        "words": (700, 2600),
        "required_sections": [],
        "min_quotes": 0,
        "max_quotes": 3,
        "needs_about": False,
        "needs_media_contacts": False,
        # A matrix comparison keeps its substance in the table, so the cells
        # count toward the length budget.
        "min_h2": 2,
        "count_tables": True,
    },
}

ARCHETYPES = {"head-to-head", "three-way", "alternatives", "stack-ranking"}
CATEGORIES = {"cnapp", "appsec", "kubernetes", "ai-security", "cloud-posture",
              "siem", "mixed"}

RELEASE_TYPES = {"partnership", "customer-win", "product-launch", "award",
                 "executive-hire", "funding", "certification"}

# Language that turns a comparison into an attack. writing-rules section 10.
ATTACK_WORDS = re.compile(
    r"\b(terrible|useless|garbage|worthless|hopeless|pathetic|laughable|"
    r"woefully|abysmal|dismal|crippl\w+|fails? miserably|joke|scam|"
    r"rip[- ]?off|nightmare|disaster)\b", re.I)

# Shapes writing-rules and house-style ban outright.
PARALLEL = [
    (re.compile(r"\bnot only\b[^.]{0,80}\bbut also\b", re.I),
     "\"not only X but also Y\""),
    (re.compile(r"\bit'?s not just\b[^.]{0,60},\s*it'?s\b", re.I),
     "\"it's not just X, it's Y\""),
    (re.compile(r"\bit isn'?t\b[^.]{0,60},\s*it'?s\b", re.I),
     "\"it isn't X, it's Y\""),
    (re.compile(r"\bnot\b[^.]{0,60},\s*but rather\b", re.I),
     "\"not X, but rather Y\""),
]

ANNOUNCEMENT = re.compile(
    r"^\s*(that is where .{0,40} comes? in|here is the (honest|practical) "
    r"\w+|this is the part that matters|let us look at why|watch this|"
    r"the (table|section|list|chart) below shows|this section covers|"
    r"as mentioned (earlier|above))\b", re.I)

WEAK_HEADING = re.compile(
    r"^(understanding|introduction|overview|background|getting started|"
    r"key takeaways|benefits|features)\b", re.I)

QUOTE_LINE = re.compile(r'^\s*[>*_]*\s*[“"].{40,}', re.M)
# `**— Srimal Silva, AGM - IT, FairFirst Insurance**`, and the same line with a
# `[name]` bracket still standing in for an unconfirmed speaker.
ATTRIB_LINE = re.compile(
    r"^\s*\**\s*(?:—|--|-)\s*[\w\[].*,.*$", re.M)

# A figure with a unit. `300+ unique findings` and `7-day deployment` both
# count, so the pattern allows a plus sign and up to two words before the unit.
MEASURED = re.compile(
    r"(\$\s?\d[\d,.]*"
    r"|\b\d[\d,.]*\s*\+?[-\s]*(?:[a-z]+[-\s]+){0,2}"
    r"(?:%|percent|x\b|days?|weeks?|hours?|minutes?|seconds?|ms\b|"
    r"projects?|subscriptions?|clusters?|environments?|regions?|"
    r"integrations?|findings?|frameworks?|benchmarks?|images?|"
    r"vulnerabilit\w+|CVEs?|controls?|models?|agents?|accounts?|users?|"
    r"nodes?|pipelines?|repos(?:itories)?|datasets?|policies|"
    r"[MBK]?B\b))", re.I)


class Report:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []

    def add(self, level: str, area: str, msg: str) -> None:
        self.rows.append((level, area, msg))

    def count(self, level: str) -> int:
        return sum(1 for lv, _, _ in self.rows if lv == level)


# ------------------------------------------------------------------- utilities

def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    raw, body = text[3:end], text[end + 4:].lstrip("\n")
    fm: dict[str, str] = {}
    key = None
    for line in raw.splitlines():
        m = re.match(r"^([a-z_][a-z0-9_]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            fm[key] = m.group(2).strip()
        elif key and line.strip():
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm, body


def unquote(v: str) -> str:
    """Strip YAML quoting, block markers and a trailing `# comment`."""
    v = v.strip()
    # A quoted value ends at its closing quote. Anything after it is a comment.
    m = re.match(r"^(['\"])(.*?)\1", v)
    if m:
        return m.group(2)
    v = re.sub(r"\s+#\s.*$", "", v)
    return v.lstrip(">|").strip()


def headings(body: str) -> list[tuple[int, str, int]]:
    out = []
    for i, line in enumerate(body.splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out.append((len(m.group(1)),
                        re.sub(r"\*\*|__|`", "", m.group(2)).strip(), i))
    return out


def prose_only(body: str) -> str:
    """Body with code fences, tables and HTML comments removed.

    A comment holds the template's own instructions to the writer. Scanning it
    reports findings against text that never ships.
    """
    t = re.sub(r"<!--.*?-->", " ", body, flags=re.S)
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"^\s*\|.*\|\s*$", " ", t, flags=re.M)
    return t


# Lines that are legitimately verbless. A caption, a label, a standalone link,
# a quote attribution, a contact block line.
VERBLESS_OK = re.compile(
    r"^\s*(?:"
    r"\[[^\]]*\]\([^)]*\)"                 # a line that is only a link
    r"|\**[A-Z][\w &/'-]{1,40}:\**\s*.*"   # **Label:** value
    r"|\**[—-]{1,2}\s*\w.*"                # an attribution line
    r"|\*[^*]+\*"                          # an italic caption
    r"|#{1,6}\s.*"                         # a heading
    r"|\[.*\]"                             # a bracketed gap left for a human
    r")\s*$")


def near_quote(paragraphs: list[str], i: int) -> bool:
    """True when this paragraph is one of the two after a quote.

    A case study attribution runs `Security Leadership` then the organisation,
    both on their own, both verbless on purpose.
    """
    return any(QUOTE_LINE.match(paragraphs[j].strip())
               for j in range(max(0, i - 2), i))


def prose_words(body: str, count_tables: bool = False) -> int:
    if count_tables:
        t = re.sub(r"<!--.*?-->", " ", body, flags=re.S)
        t = re.sub(r"```.*?```", " ", t, flags=re.S)
        t = re.sub(r"^\s*\|[\s:|-]+\|\s*$", " ", t, flags=re.M)
        t = t.replace("|", " ")
    else:
        t = prose_only(body)
    t = re.sub(r"^#{1,6}.*$", " ", t, flags=re.M)
    return len(t.split())


# --------------------------------------------------------------- shared checks

def check_shared(body: str, hs: list[tuple[int, str, int]], r: Report) -> None:
    """Rules every AccuKnox page obeys, from house-style.md."""
    h1 = [h for h in hs if h[0] == 1]
    if len(h1) != 1:
        r.add("CRITICAL", "structure", f"{len(h1)} H1 headings, need exactly 1")

    prev = 0
    for level, title, line in hs:
        if prev and level > prev + 1:
            r.add("HIGH", "structure",
                  f"line {line}: H{level} follows H{prev}, no skipped levels")
        prev = level
        if ":" in title and level > 1 and not title.endswith("?"):
            r.add("MEDIUM", "structure",
                  f"line {line}: no colon in a heading: \"{title}\"")
        if level == 2 and WEAK_HEADING.match(title):
            r.add("MEDIUM", "structure",
                  f"line {line}: heading states a topic, not a conclusion: "
                  f"\"{title}\"")

    prose = prose_only(body)
    for pattern, label in PARALLEL:
        if pattern.search(prose):
            r.add("HIGH", "watermark", f"banned sentence shape: {label}")

    for i, line in enumerate(prose.splitlines(), 1):
        if ANNOUNCEMENT.match(line.strip()):
            r.add("HIGH", "watermark",
                  f"line {i}: announcement sentence, delete it: "
                  f"\"{line.strip()[:60]}\"")

    # Verbless fragments outside headings, tables, captions and attributions.
    paragraphs = re.split(r"\n\s*\n", prose)
    for i, para in enumerate(paragraphs):
        s = para.strip()
        if (not s or s.startswith(("#", "|", ">", "```", "*", "-"))
                or ATTRIB_LINE.match(s) or VERBLESS_OK.match(s)
                or QUOTE_LINE.match(s) or near_quote(paragraphs, i)):
            continue
        for sent in re.split(r"(?<=[.!?])\s+", s):
            words = sent.split()
            if len(words) > 5 or not words:
                continue
            # A finite verb is either a known auxiliary or a word carrying a
            # verb inflection. The inflection test over-accepts, which is the
            # right way round: a missed fragment costs less than a false alarm
            # on a real sentence.
            if re.search(r"\b(is|are|was|were|be|been|am|has|have|had|do|"
                         r"does|did|can|could|will|would|shall|should|may|"
                         r"might|must)\b", sent, re.I):
                continue
            if any(re.fullmatch(r"[a-z]{3,}(s|ed|es)", w.strip(".,;:!?\"'`*)"),
                                re.I) for w in words):
                continue
            r.add("HIGH", "watermark",
                  f"verbless fragment, rewrite as a sentence: "
                  f"\"{sent.strip()}\"")

    bare = re.findall(r"(?<![(\[<])\bhttps?://[^\s)>\]]+", prose)
    if bare:
        r.add("HIGH", "links",
              f"{len(bare)} bare URL(s) in prose, wrap each in link text")
    for anchor, url in re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)\)", prose):
        if anchor.strip().lower() in ("click here", "here", "read more",
                                      "this", "link", ""):
            r.add("HIGH", "links", f"weak anchor text \"{anchor}\" -> {url}")

    # Tables need a header row and no empty cells.
    for block in re.findall(r"((?:^\s*\|.*\|\s*$\n?)+)", body, re.M):
        rows = [ln for ln in block.strip().splitlines() if ln.strip()]
        if len(rows) < 2 or not re.match(r"^\s*\|[\s:|-]+\|\s*$", rows[1]):
            r.add("HIGH", "tables",
                  f"table starting \"{rows[0].strip()[:50]}\" has no header row")
            continue
        for ln in rows[2:]:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if any(c == "" for c in cells):
                r.add("MEDIUM", "tables",
                      f"empty cell in row \"{ln.strip()[:50]}\". "
                      "Write `-` or the real value")

    callouts = re.findall(r"^\s*>\s*\*\*(Note|Prerequisite|Warning|Limitation)",
                          body, re.M)
    if len(callouts) > 3:
        r.add("MEDIUM", "callouts",
              f"{len(callouts)} callouts. Cap at 3, or the warning stops "
              "reading as a warning")


# ------------------------------------------------------------ channel checks

def check_press_release(fm: dict, body: str, hs: list, r: Report) -> None:
    rtype = unquote(fm.get("release_type", "")).lower()
    if rtype and rtype not in RELEASE_TYPES:
        r.add("HIGH", "front-matter",
              f"release_type `{rtype}` is not one of "
              f"{', '.join(sorted(RELEASE_TYPES))}")

    city = unquote(fm.get("dateline_city", ""))
    if city and city.split(",")[0].strip() not in body:
        r.add("CRITICAL", "dateline",
              f"the body never opens with the dateline city `{city}`")

    first = next((p for p in re.split(r"\n\s*\n", body)
                  if p.strip() and not p.lstrip().startswith("#")), "")
    if city and not re.match(r"^\s*\**" + re.escape(city.split(",")[0]), first):
        r.add("HIGH", "dateline",
              "the first paragraph does not start with the dateline. "
              "Open with **City, Country**, DD MON YYYY.")

    quotes = QUOTE_LINE.findall(body)
    attribs = ATTRIB_LINE.findall(body)
    if len(quotes) < 2:
        r.add("CRITICAL", "quotes",
              f"{len(quotes)} quote(s). A release carries 2 to 5, one per "
              "organisation named in the headline")
    if len(quotes) > 5:
        r.add("MEDIUM", "quotes", f"{len(quotes)} quotes. Five is the ceiling")
    if len(attribs) < len(quotes):
        r.add("CRITICAL", "quotes",
              f"{len(quotes)} quotes but {len(attribs)} attribution lines. "
              "Every quote needs `**— Name, Title, Company**`")

    labels = [t.lower() for _, t, _ in hs]
    abouts = [t for t in labels if t.startswith("about ")]
    if not abouts:
        r.add("CRITICAL", "boilerplate",
              "no `About <organisation>` section. Every named org gets one")
    if not any("about accuknox" in t for t in abouts):
        r.add("HIGH", "boilerplate", "no `About AccuKnox` section")
    if not any("media contact" in t for t in labels):
        r.add("HIGH", "boilerplate", "no `Media Contacts` section")

    if not unquote(fm.get("contact_email", "")):
        r.add("HIGH", "boilerplate", "no contact_email in the front matter")


def check_case_study(fm: dict, body: str, hs: list, r: Report) -> None:
    labels = [t.lower().strip() for _, t, _ in hs]
    sections = {}
    for want in ("challenges", "solutions", "outcomes"):
        idx = next((i for i, t in enumerate(labels) if t == want), None)
        if idx is None:
            r.add("CRITICAL", "structure", f"no `{want.title()}` section")
        sections[want] = idx

    lines = body.splitlines()
    starts = {t: ln for lv, t, ln in [(a, b.lower().strip(), c)
                                      for a, b, c in hs]}
    order = sorted((ln, t) for t, ln in starts.items())
    for want in ("challenges", "solutions", "outcomes"):
        if want not in starts:
            continue
        begin = starts[want]
        after = [ln for ln, _ in order if ln > begin]
        end = after[0] if after else len(lines) + 1
        chunk = "\n".join(lines[begin:end - 1])
        bullets = re.findall(r"^\s*[-*]\s+(.+)$", chunk, re.M)
        if not 3 <= len(bullets) <= 6:
            r.add("HIGH", "structure",
                  f"`{want.title()}` has {len(bullets)} bullets, write 3 to 6")
        for b in bullets:
            if len(b.split()) < 6:
                r.add("MEDIUM", "structure",
                      f"`{want.title()}` bullet is a fragment: \"{b[:50]}\"")
        if want == "outcomes":
            measured = sum(1 for b in bullets if MEASURED.search(b))
            if measured < 3:
                r.add("CRITICAL", "outcomes",
                      f"only {measured} of {len(bullets)} outcomes carry a "
                      "number with a unit. A case study without figures is a "
                      "testimonial")

    quotes = QUOTE_LINE.findall(body)
    if not quotes:
        r.add("CRITICAL", "quotes",
              "no customer quote. Use `Security Leadership` where the name "
              "cannot be published")

    # `customer` holds the descriptor cleared for publication, so it belongs in
    # the body. `internal_customer_name` holds the real name and must never
    # reach the page.
    anon = unquote(fm.get("anonymized", "")).lower() in ("true", "yes")
    real = unquote(fm.get("internal_customer_name", ""))
    if anon and not real:
        r.add("HIGH", "privacy",
              "anonymized is true but internal_customer_name is empty. Record "
              "the real name there so the leak check can run")
    if anon and real and re.search(re.escape(real), body, re.I):
        r.add("CRITICAL", "privacy",
              f"anonymized is true but the body names `{real}`")

    if not re.search(r"^##\s+\S", body, re.M):
        r.add("HIGH", "structure", "no H2 subtitle under the H1")


def check_comparison(fm: dict, body: str, hs: list, r: Report) -> None:
    arch = unquote(fm.get("archetype", "")).lower()
    if arch and arch not in ARCHETYPES:
        r.add("CRITICAL", "front-matter",
              f"archetype `{arch}` is not one of {', '.join(sorted(ARCHETYPES))}")
    cat = unquote(fm.get("category", "")).lower()
    if cat and cat not in CATEGORIES:
        r.add("HIGH", "front-matter",
              f"category `{cat}` is not one of {', '.join(sorted(CATEGORIES))}")

    competitors = [c.strip(' "\'')
                   for c in unquote(fm.get("competitors", "")).strip("[]").split(",")
                   if c.strip(' "\'')]
    if not competitors:
        r.add("CRITICAL", "front-matter", "competitors list is empty")
    if arch == "head-to-head" and len(competitors) != 1:
        r.add("HIGH", "front-matter",
              f"archetype head-to-head names {len(competitors)} competitors, "
              "expected 1")
    if arch == "three-way" and len(competitors) != 2:
        r.add("HIGH", "front-matter",
              f"archetype three-way names {len(competitors)} competitors, "
              "expected 2")

    hit = ATTACK_WORDS.search(prose_only(body))
    if hit:
        r.add("CRITICAL", "tone",
              f"attack language \"{hit.group(0)}\". Compare on a named sourced "
              "capability or drop the line (writing-rules section 10)")

    rows = re.findall(r"^\s*\|.*\|\s*$", body, re.M)
    params = [t for lv, t, _ in hs if lv == 3]

    if arch in ("head-to-head", "three-way", "stack-ranking"):
        if len(params) < 6 and len(rows) < 8:
            r.add("CRITICAL", "structure",
                  f"{len(params)} parameter rows. A matrix comparison carries "
                  "at least 6")
        labels = [t.lower() for _, t, _ in hs]
        if not any("why customers choose accuknox" in t for t in labels):
            r.add("HIGH", "structure",
                  "no `Why customers choose AccuKnox over <competitor>` section")
        else:
            for want in ("better", "faster", "cheaper"):
                if not any(t.lower().strip() == want for _, t, _ in hs):
                    r.add("MEDIUM", "structure",
                          f"the closing section is missing the `{want.title()}` "
                          "heading")

    if arch == "alternatives":
        numbered = [t for lv, t, _ in hs if lv == 2 and re.match(r"^\d+\.", t)]
        if len(numbered) < 3:
            r.add("HIGH", "structure",
                  f"{len(numbered)} numbered vendor sections. An alternatives "
                  "page lists at least 3")

    # Every competitor claim needs a source the competitor published.
    for name in competitors:
        mentions = len(re.findall(re.escape(name), body, re.I))
        sourced = len(re.findall(
            r"\[[^\]]*\]\(https?://[^)]*" + re.escape(name.split()[0].lower()),
            body, re.I))
        if mentions >= 3 and sourced == 0:
            r.add("HIGH", "sourcing",
                  f"`{name}` appears {mentions} times with no link to their "
                  "own documentation. Every competitor claim carries its source")

    helpdocs = len(re.findall(r"https://help\.accuknox\.com/", body))
    if helpdocs < 2:
        r.add("HIGH", "sourcing",
              f"{helpdocs} help.accuknox.com link(s). Each AccuKnox capability "
              "claim reaches the doc that proves it")


CHECKERS = {
    "press-release": check_press_release,
    "case-study": check_case_study,
    "comparison": check_comparison,
}


# ------------------------------------------------------------------ front end

def run(path: Path, channel: str) -> Report:
    spec = CHANNELS[channel]
    text = path.read_text("utf-8")
    fm, body = split_front_matter(text)
    hs = headings(body)
    r = Report()

    for key in spec["front_matter"]:
        if key not in fm or not unquote(fm[key]):
            r.add("CRITICAL", "front-matter", f"missing `{key}`")

    slug = unquote(fm.get("slug", ""))
    if slug and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        r.add("HIGH", "front-matter",
              f"slug `{slug}` must be lowercase words joined by hyphens")
    url = unquote(fm.get("url", ""))
    if slug and url and url != spec["url_prefix"] + slug:
        r.add("HIGH", "front-matter",
              f"url should be {spec['url_prefix']}{slug}")

    words = prose_words(body, spec.get("count_tables", False))
    lo, hi = spec["words"]
    if words < lo:
        r.add("HIGH", "length",
              f"{words} prose words, live pages of this type run {lo} to {hi}")
    elif words > hi:
        r.add("MEDIUM", "length",
              f"{words} prose words, live pages of this type run {lo} to {hi}")

    if sum(1 for lv, _, _ in hs if lv == 2) < spec["min_h2"]:
        r.add("HIGH", "structure",
              f"fewer than {spec['min_h2']} H2 sections")

    check_shared(body, hs, r)
    CHECKERS[channel](fm, body, hs, r)
    return r


def render(path: Path, channel: str, r: Report) -> str:
    out = [f"{channel} check  {path.name}", ""]
    if not r.rows:
        out.append("  no findings")
        return "\n".join(out)
    for level in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
        rows = [x for x in r.rows if x[0] == level]
        if not rows:
            continue
        out.append(f"{level} ({len(rows)})")
        for _, area, msg in rows:
            out.append(f"  [{area}] {msg}")
        out.append("")
    out.append(f"{r.count('CRITICAL')} critical, {r.count('HIGH')} high, "
               f"{r.count('MEDIUM')} medium")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", type=Path)
    ap.add_argument("--channel", required=True, choices=sorted(CHANNELS))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not args.draft.exists():
        print(f"no such file: {args.draft}", file=sys.stderr)
        return 2
    r = run(args.draft, args.channel)
    if args.json:
        print(json.dumps({"file": str(args.draft), "channel": args.channel,
                          "findings": [{"level": a, "area": b, "message": c}
                                       for a, b, c in r.rows]}, indent=2))
    else:
        print(render(args.draft, args.channel, r))
    return 1 if r.count("CRITICAL") else 0


if __name__ == "__main__":
    raise SystemExit(main())
