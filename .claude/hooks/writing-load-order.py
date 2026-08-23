#!/usr/bin/env python
"""UserPromptSubmit gate that prints the writing load order for this repo.

Reads the hook payload on stdin. When the prompt asks for prose work, prints the
file chain for the detected channel and the gates that run after it. Plain
stdout from a UserPromptSubmit hook is injected into the model context.

The chain is derived from .claude/core/runtime-contract.md. Change the contract
and change this file in the same commit, or the two will disagree.

Silent on every other prompt. Never blocks. Exits 0 on malformed input.
"""
import json
import re
import sys

WRITING = re.compile(
    r"\b(write|writing|draft|drafting|rewrite|rewriting|redo|revise|compose|"
    r"edit|editing|document|documenting|page|doc|docs|blog|post|guide|"
    r"how-?to|faq|release note|changelog|alt text|caption|readme|"
    r"press release|case study|announce|comparison|battlecard|"
    r"tighten|proofread|de-?slop|slop|humani[sz]e|clean up)\b",
    re.I,
)

AUDIT = re.compile(
    r"\b(which|list|inventory|status|how many|show me|find me|count|"
    r"where is|search|grep)\b", re.I,
)
AUTHORING = re.compile(
    r"\b(write|writing|draft|drafting|rewrite|rewriting|redo|revise|compose|"
    r"edit|editing|document|tighten|de-?slop|humani[sz]e|clean up)\b", re.I,
)

# Ordered. The first match wins, so the narrow channels come first.
CHANNELS = [
    ("Blog post", r"\bblog\b|\bpost\b|\barticle\b|\bseries\b",
     "section 11, plus the accuknox-blog-writer skill, which owns this channel "
     "end to end. Front-load the answer in the first 150 words, then earn the length",
     "references/blog-drafts/ or references/<series>/"),
    ("FAQ answer", r"\bfaq\b|\bfrequently asked\b",
     "section 6. The question is the heading, the answer is the first sentence",
     "docs/faqs/"),
    ("How-to or procedure", r"\bhow-?to\b|\bprocedure\b|\bsteps?\b|\bwalkthrough\b|\bonboard\b",
     "sections 7 and 12. One action per step, commands complete and copy-pasteable",
     "docs/how-to/"),
    ("Getting started", r"\bgetting started\b|\bquick ?start\b|\bfirst\b.*\bsetup\b",
     "sections 7 and 12, with prerequisites first", "docs/getting-started/"),
    ("Integration guide", r"\bintegration\b|\bintegrate\b|\bconnector\b|\bwebhook\b",
     "sections 8 and 9. Every version and field comes from an opened source",
     "docs/integrations/"),
    ("Use case", r"\buse ?case\b|\bscenario\b|\bhardening\b|\bzero ?trust\b|\bforensics\b",
     "sections 1 and 5, with a named scenario", "docs/use-cases/"),
    ("Release note or update", r"\brelease note\b|\bchangelog\b|\bwhat'?s new\b|\bupdate\b|\bv\d+\.\d+\b",
     "section 9. No version, flag or fix claim without a source", "docs/ and updates"),
    ("Press release", r"\bpress release\b|\bannounce\w*\b|\bnewswire\b",
     "the accuknox-press-release-writer skill, which owns this channel. Every "
     "name, title and claim comes from what the user supplied",
     "references/press-release-drafts/"),
    ("Case study", r"\bcase stud\w+\b|\bcustomer story\b|\bsuccess story\b|"
     r"\bcustomer win\b",
     "the accuknox-case-study-writer skill, which owns this channel. Three "
     "quantified outcomes minimum, plus the anonymisation check",
     "references/case-study-drafts/"),
    ("Comparison page", r"\bcompar|\bversus\b|\bvs\b|\balternative\b|"
     r"\bstack ranking\b|\bbattlecard\b",
     "the accuknox-comparison-writer skill, on top of section 10. Compare on a "
     "named sourced capability, never attack",
     "references/comparison-drafts/"),
    ("Doc page", r"\bdocs?\b|\bpage\b|\bdocument\b",
     "the whole of writing-rules.md", "docs/"),
]

TEMPLATE = """\
WRITING LOAD ORDER (hook, not optional)

Detected channel: {channel}

Load in this order, before you draft a line.

1. .claude/core/runtime-contract.md      always
2. .claude/core/writing-rules.md         always
3. .claude/core/restraint-rules.md       always
4. focus for this channel: {focus}

The ten banned words are already in context from CLAUDE.md and AGENTS.md. Never
restate one of them inside another file.

Target path: {path}

Gates, in this order:
  mkdocs build --strict
  python "D:\\Atharva\\NOTES\\SCRIPTS\\slop\\score.py" "<file>"      CRIT must reach 0
  then section 5 of .claude/core/restraint-rules.md

Two rules are hard and outrank every file above. No version, CVE, CVSS score,
compliance control, CLI flag, API field, default or supported platform without
an opened source behind it, and a bracket where the fact is missing. And no
working exploit, live payload or unredacted customer data, in text or in a
screenshot.

Print this block above the draft, filled in with what actually loaded.

    Loaded   runtime-contract -> writing-rules -> restraint-rules
    Channel  {channel}
    Sourced  <the files, docs or advisories opened, by name>
    Gates    mkdocs --strict: pass/fail | slop CRIT <n> | restraint pass: done

No block means the chain was skipped.\
"""


def pick(prompt: str):
    for name, pattern, focus, path in CHANNELS:
        if re.search(pattern, prompt, re.I):
            return name, focus, path
    return ("prose, channel unstated", "the whole of writing-rules.md",
            "<pick from the runtime contract>")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    prompt = str(payload.get("prompt") or "")
    if not WRITING.search(prompt):
        return 0
    if AUDIT.search(prompt) and not AUTHORING.search(prompt):
        return 0
    channel, focus, path = pick(prompt)
    sys.stdout.write(TEMPLATE.format(channel=channel, focus=focus, path=path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
