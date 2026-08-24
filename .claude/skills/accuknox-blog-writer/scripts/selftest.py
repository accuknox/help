#!/usr/bin/env python3
"""Prove the blog harness still works after a change to it.

Offline checks run always. Network checks run unless you pass `--offline`, and
they hit accuknox.com, so keep them out of a tight loop.

Usage:
    python selftest.py
    python selftest.py --offline

Exit codes: 0 every check passed, 1 at least one failed.
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

PASS, FAIL = [], []


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def check(label: str, ok: bool, detail: str = "") -> None:
    (PASS if ok else FAIL).append(label)
    mark = "ok  " if ok else "FAIL"
    print(f"{mark}  {label}" + (f"  ({detail})" if detail else ""))


# A draft that is deliberately wrong in seven named ways.
BAD = '''---
title: "A post"
slug: "Bad_Slug"
url: "https://accuknox.com/blog/other"
primary_keyword: "widget security"
---

# Overview

## Introduction

Some text with a bare URL https://example.com/x in it.

## Understanding things

More text.
'''


def offline_checks() -> None:
    grade = load("grade")
    gdoc = load("to_gdoc_html")
    slop = load("slop")

    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "bad.md"
        bad.write_text(BAD, encoding="utf-8", newline="\n")
        r = grade.grade(bad, 1200, published=False)
        msgs = " | ".join(m for _, _, m in r.rows)
        check("grade flags missing front matter",
              "missing `seo_title`" in msgs)
        check("grade flags a non-kebab slug", "Bad_Slug" in msgs)
        check("grade flags a url that does not match the slug",
              "url does not end in" in msgs)
        check("grade flags a missing TL;DR", "no TL;DR section" in msgs)
        check("grade flags a missing FAQ", "no FAQ section" in msgs)
        check("grade flags a topic heading",
              "states a topic, not a conclusion" in msgs)
        check("grade flags a bare URL", "bare URL" in msgs)
        check("grade flags a keyword that never appears",
              "never appears in the body" in msgs)

        # The template must pass its own front-matter check.
        tmpl = ROOT / "assets" / "blog-template.md"
        rt = grade.grade(tmpl, 400, published=False)
        missing = [m for lv, ar, m in rt.rows
                   if ar == "front-matter" and m.startswith("missing")]
        check("template carries every required front-matter key",
              not missing, ", ".join(missing))

        # A URL inside a fence is not a link in the prose.
        fenced = Path(td) / "fenced.md"
        fenced.write_text(
            "# T\n\n```bash\ncurl https://example.com/inside\n```\n",
            encoding="utf-8", newline="\n")
        rf = grade.grade(fenced, 10, published=False)
        check("grade ignores a URL inside a code fence",
              not any("bare URL" in m for _, _, m in rf.rows))

        # Published pages are scored without the WordPress-only fields.
        pub = Path(td) / "pub.md"
        pub.write_text(
            '---\ntitle: "T"\nmarkdown_url: "https://accuknox.com/blog/t.md"\n'
            '---\n\n# T\n\n## TL;DR\n\n- One fact, 5 of them.\n',
            encoding="utf-8", newline="\n")
        rp = grade.grade(pub, 10)
        check("grade auto-detects a fetched page",
              not any(lv == "CRITICAL" and ar == "front-matter"
                      for lv, ar, _ in rp.rows))

    # The Google Docs converter.
    md = ('---\ntitle: "Doc title"\n---\n\n# Doc title\n\n'
          'Text with a [link](https://example.com).\n\n'
          '```bash\nline one\n  indented two\n```\n\n'
          '| A | B |\n| --- | --- |\n| 1 | 2 |\n')
    title, page = gdoc.convert(md, "fallback")
    check("gdoc uses the front-matter title", title == "Doc title", title)
    check("gdoc emits no <pre>", "<pre" not in page)
    check("gdoc wraps a fence in a code table",
          'table class="code"' in page)
    check("gdoc keeps the fence line break", "line one<br/>" in page)
    check("gdoc preserves leading indentation", "&nbsp;&nbsp;indented" in page)
    check("gdoc keeps the markdown table", "<td>1</td>" in page)
    check("gdoc keeps the hyperlink", 'href="https://example.com"' in page)
    check("gdoc adds no line-break tags to prose",
          page.count("<br/>") == 1)
    check("gdoc renders the front matter as a table",
          'class="meta"' in page)

    # The slop wrapper's suppression rule.
    lines = ["## TL;DR", "", "Body text; with a real semicolon."]
    check("slop suppresses the TL;DR heading",
          slop.is_tldr_semicolon(lines, 1, "semicolon"))
    check("slop keeps a real semicolon",
          not slop.is_tldr_semicolon(lines, 3, "semicolon"))
    check("slop suppresses nothing but semicolons",
          not slop.is_tldr_semicolon(lines, 1, "em-dash"))

    # The PRODUCT UI media index.
    man = ROOT / "media" / "MANIFEST.json"
    idx = ROOT / "media" / "INDEX.md"
    check("media/MANIFEST.json exists", man.exists())
    check("media/INDEX.md exists", idx.exists())
    if man.exists():
        import json as _json
        data = _json.loads(man.read_text("utf-8"))
        check("manifest lists files", data.get("file_count", 0) > 0,
              f"{data.get('file_count')} files")
        check("manifest records its Drive source",
              "drive.google.com" in data.get("source", ""))

    # The cached inventory.
    for name in ("platform", "solutions", "comparisons", "blog",
                 "press-release", "case-study"):
        f = ROOT / "sources" / f"{name}.md"
        rows = f.read_text("utf-8").count("| `") if f.exists() else 0
        check(f"sources/{name}.md exists and lists URLs", rows > 0,
              f"{rows} rows")

    # Every script parses and answers --help.
    for s in ("refresh_sources", "fetch_md", "grade", "verify_links",
              "to_gdoc_html", "slop"):
        p = subprocess.run([sys.executable, str(HERE / f"{s}.py"), "--help"],
                           capture_output=True, text=True)
        check(f"{s}.py runs", p.returncode == 0, p.stderr.strip()[:60])


TWIN = """---
title: "T"
markdown_url: "https://accuknox.com/blog/t.md"
---

# T

## Table of Contents

### TL;DR

- One fact.

## A real section

Body.

## Ready For A Personalized Security Assessment

Testimonial text.

## Continue Reading

### [Some other post](https://accuknox.com/blog/other)

[Read More](https://accuknox.com/blog/other)
"""


SKILLS = ROOT.parent  # .claude/skills/

CHANNEL_TEMPLATES = {
    "case-study": SKILLS / "accuknox-case-study-writer/assets/case-study-template.md",
    "press-release": SKILLS / "accuknox-press-release-writer/assets/press-release-template.md",
    "comparison": SKILLS / "accuknox-comparison-writer/assets/comparison-template.md",
}

# A draft that is wrong in eight named ways, one per channel rule.
BAD_CASE_STUDY = '''---
title: "T"
subtitle: "S"
slug: "bad_slug"
url: "https://accuknox.com/case-studies/other"
customer: "Acme Bank"
anonymized: true
internal_customer_name: "Acme Bank"
sector: "banking"
region: "UAE"
environment: "Azure"
deployment: "SaaS"
excerpt: "E"
---

# Title

## Subtitle

Acme Bank runs its core banking platform on Azure, which is the leak this
fixture exists to catch.

## Challenges

- One bullet only, which is too few for this section to say anything.

## Solutions

- One bullet only, which is also too few.

## Outcomes

- Things got better for the customer in several ways.
- The team was happier with the tooling than before.
- Security posture improved across the estate.
'''


def channel_checks() -> None:
    """The three non-blog validators, on shapes that broke them before."""
    check_asset = load("check_asset")

    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "bad.md"
        bad.write_text(BAD_CASE_STUDY, encoding="utf-8", newline="\n")
        msgs = " | ".join(m for _, _, m in
                          check_asset.run(bad, "case-study").rows)
        check("case-study flags a leaked customer name",
              "the body names `Acme Bank`" in msgs)
        check("case-study flags thin Challenges",
              "`Challenges` has 1 bullets" in msgs)
        check("case-study flags outcomes with no figures",
              "outcomes carry a number with a unit" in msgs)
        check("case-study flags a non-kebab slug", "bad_slug" in msgs)
        check("case-study flags a url that does not match the slug",
              "url should be" in msgs)

    # The regression that motivated each fix.
    lines = ["**300+ unique findings** surfaced across 6 subscriptions.",
             "**7-day deployment** completed in the environment.",
             "**$1B+ in secured operations** on AWS.",
             "Things got better for the customer."]
    hits = [bool(check_asset.MEASURED.search(l)) for l in lines]
    check("MEASURED reads `300+ unique findings`", hits[0])
    check("MEASURED reads `7-day deployment`", hits[1])
    check("MEASURED reads a dollar figure", hits[2])
    check("MEASURED rejects a sentence with no figure", not hits[3])

    check("attribution regex reads a bracketed speaker",
          bool(check_asset.ATTRIB_LINE.match(
              "**— [name], [exact job title], AccuKnox**")))
    check("attribution regex reads a named speaker",
          bool(check_asset.ATTRIB_LINE.match(
              "**— Srimal Silva, AGM - IT, FairFirst Insurance**")))

    check("unquote strips a trailing YAML comment",
          check_asset.unquote('"customer-win"   # a | b | c') == "customer-win")

    # The verbless-fragment heuristic must not fire on a real short sentence.
    r = check_asset.Report()
    body = "\n\nThe cost lands later.\n\nA typo pulls the image.\n"
    check_asset.check_shared(body, [], r)
    frags = [m for lv, ar, m in r.rows if ar == "watermark"]
    check("fragment check accepts a short sentence with a verb", not frags,
          "; ".join(frags)[:80])

    # A comparison counts its table toward the length budget.
    with tempfile.TemporaryDirectory() as td:
        tbl = Path(td) / "t.md"
        row = "| p | " + ("word " * 30) + " | " + ("word " * 30) + " |\n"
        tbl.write_text("---\ntitle: \"T\"\n---\n\n# T\n\n| a | b | c |\n"
                       "| --- | --- | --- |\n" + row * 12,
                       encoding="utf-8", newline="\n")
        plain = check_asset.prose_words(tbl.read_text("utf-8"), False)
        withtbl = check_asset.prose_words(tbl.read_text("utf-8"), True)
        check("comparison length counts table cells", withtbl > plain + 500,
              f"{plain} vs {withtbl}")

    for channel, path in CHANNEL_TEMPLATES.items():
        check(f"{channel} template exists", path.exists(), str(path))
        if path.exists():
            check(f"{channel} template carries its front matter",
                  not [m for lv, ar, m in check_asset.run(path, channel).rows
                       if ar == "front-matter" and m.startswith("missing")])

    slop = load("slop")
    attrib = ["**— Nat Natraj, CEO, AccuKnox**", "A prose line with an em dash."]
    check("slop suppresses the attribution em dash",
          slop.is_attribution_dash(attrib, 1, "em-dash"))
    check("slop keeps an em dash in prose",
          not slop.is_attribution_dash(attrib, 2, "em-dash"))


def strip_checks() -> None:
    """The boilerplate stripper, on the shapes that broke it before."""
    fetch = load("fetch_md")
    out = fetch.strip_boilerplate(TWIN)
    check("stripper keeps an H3 TL;DR under the Table of Contents",
          "### TL;DR" in out)
    check("stripper drops the Table of Contents heading",
          "Table of Contents" not in out)
    check("stripper drops the CTA block and its testimonial",
          "Testimonial text" not in out)
    check("stripper drops Continue Reading and its child headings",
          "Continue Reading" not in out and "Some other post" not in out)
    check("stripper keeps the authored section", "A real section" in out)
    check("stripper keeps the front matter", out.startswith("---"))


def network_checks() -> None:
    fetch = load("fetch_md")
    check("markdown twin URL is built correctly",
          fetch.to_md_url("platform/cspm") ==
          "https://accuknox.com/platform/cspm.md")
    try:
        md = fetch.strip_boilerplate(
            fetch.fetch(fetch.to_md_url("blog/ai-spm-tools")))
    except Exception as exc:  # noqa: BLE001
        check("accuknox.com serves a markdown twin", False, str(exc)[:60])
        return
    check("accuknox.com serves a markdown twin", md.startswith("---"))
    check("the twin carries front matter", "markdown_url:" in md)
    check("boilerplate is stripped",
          "Continue Reading" not in md and
          "Ready For A Personalized" not in md)
    check("the body survives stripping", fetch.body_word_count(md) > 400,
          f"{fetch.body_word_count(md)} words")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true",
                    help="skip the checks that hit accuknox.com")
    args = ap.parse_args()

    print("offline checks")
    offline_checks()
    strip_checks()
    channel_checks()
    if not args.offline:
        print("\nnetwork checks")
        network_checks()

    print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
    for f in FAIL:
        print(f"  failed: {f}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
