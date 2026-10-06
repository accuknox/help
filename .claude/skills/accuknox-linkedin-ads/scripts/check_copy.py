"""Check ad copy in a campaigns file against the playbook limits.

    python check_copy.py <campaigns.json>

Exit code 1 when any ad breaks a hard rule:
- intro text over 150 characters (LinkedIn hides the rest behind "see more")
- LinkedIn headline over 70 characters
- form headline over 120 characters
- intro text that opens on "We" or "AccuKnox"
- a competitor name anywhere in the campaign
- an em dash, en dash or semicolon in any copy field, form field or pick
- a form headline that is not a question
"""
import json
import re
import sys
from pathlib import Path

COMPETITORS = [
    "wiz", "palo alto", "prisma", "cortex", "crowdstrike", "aqua", "aquasec", "orca", "sysdig",
    "lacework", "snyk", "noma", "horizon3", "palantir", "zscaler", "netskope", "varonis",
    "upwind", "sentinelone", "check point", "fortinet", "tenable", "rapid7", "qualys",
    "protect ai", "hiddenlayer", "lakera", "prompt security", "pillar",
]
COPY_KEYS = ("headline", "body", "tagline", "intro", "li_headline", "cta", "cta_button")


def walk(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)
    elif isinstance(obj, str):
        yield obj


def main():
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = []
    for c in data["campaigns"]:
        blob = " ".join(walk(c)).lower()
        for name in COMPETITORS:
            if re.search(rf"\b{re.escape(name)}\b", blob):
                errors.append(f"{c['id']}: names a competitor ({name})")
        form = c.get("form", {})
        if len(form.get("headline", "")) > 120:
            errors.append(f"{c['id']}: form headline over 120 characters")
        if form and not form.get("headline", "").rstrip().endswith("?"):
            errors.append(f"{c['id']}: form headline is not a question")
        for field in [form.get("headline", ""), *form.get("questions", []), c.get("pick", "")]:
            if re.search(r"[\u2013\u2014;]", field):
                errors.append(f"{c['id']}: dash or semicolon in the form or the pick")
        for ad in c.get("ads", []):
            aid = ad["id"]
            intro = ad.get("intro", "")
            if len(intro) > 150:
                errors.append(f"{aid}: intro is {len(intro)} characters, limit 150")
            if len(ad.get("li_headline", "")) > 70:
                errors.append(f"{aid}: LinkedIn headline over 70 characters")
            if re.match(r"\s*(we|accuknox)\b", intro, re.I):
                errors.append(f"{aid}: intro opens on We or AccuKnox")
            for k in COPY_KEYS:
                if re.search(r"[–—;]", ad.get(k, "")):
                    errors.append(f"{aid}: dash or semicolon in {k}")
    for e in errors:
        print("FAIL", e)
    print(f"{len(errors)} problems" if errors else "copy passes")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
