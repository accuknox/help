"""Jev judgments for the edit, through the TypeSafe System One API.

Two places need meaning that a regex cannot supply:

  narration   Before any line goes to ElevenLabs, ask per line: does it carry a customer
              identifier, and will a voice stumble on a term in it? A regex cannot tell the
              product name "KubeArmor" from a hostname, or "a Kubernetes cluster" from a real
              cluster name. One call answers every line in parallel.
  cues        Survey triage of the caption file. Each cue becomes setup, navigation, content,
              off-track or wrap-up, so dead time and wrong turns show up before frame review.

Policy lives in code (the THRESHOLDS below), so a threshold change needs no new call.
Every function returns None when Jev is off or the call fails, and the caller falls back
to its deterministic path.

Data rule: edit.py sets JEV = "off" | "narration" | "all".
  "narration" sends only the narration lines, which leave the machine for ElevenLabs anyway.
  "all" also sends caption cues, which hold the call itself. Use it only when the brief
  allows another outside service. A customer-confidential brief means "narration" at most,
  or "off" when it names ElevenLabs as the only service allowed.
"""
import os
import re
import sys

ENV_FILE = r"D:\Atharva\NOTES\.env"
# Plain product lines score 0.51 to 0.57 on identifier and real ones score about 0.98, so 0.7
# blocks the real ones with margin. The code patterns still catch IPs, hostnames, IDs and paths.
THRESHOLDS = {"identifier": 0.7, "pronounce": 0.6}
CUE_KINDS = {
    "setup": "Joining, recording, screen-share or audio checks before the demo starts.",
    "navigation": "Telling the presenter where to click, scroll or go next.",
    "content": "Explaining what a screen, finding, policy or result means.",
    "off_track": "A wrong click, an empty or unavailable view, confusion, or a retry.",
    "wrap_up": "Ending the call, stopping the recording, or talk after the demo ends.",
}


def _key():
    k = os.environ.get("TYPESAFE_API_KEY", "").strip()
    if not k and os.path.exists(ENV_FILE):
        for line in open(ENV_FILE, encoding="utf-8", errors="ignore"):
            if line.startswith("TYPESAFE_API_KEY="):
                k = line.split("=", 1)[1].strip().strip('"').strip("'")
    return k or None


def _ask(state, questions):
    """One System One call. Returns the response, or None with a one-line reason on stderr."""
    try:
        from typesafe_sdk import TypeSafeClient
    except ImportError:
        print("jev: pip install typesafe-sdk, falling back to code checks", file=sys.stderr)
        return None
    key = _key()
    if not key:
        print("jev: no TYPESAFE_API_KEY, falling back to code checks", file=sys.stderr)
        return None
    try:
        with TypeSafeClient(api_key=key, timeout=60) as client:
            return client.system_one(state=state, questions=questions)
    except Exception as e:  # service, network or auth failure: the deterministic path takes over
        print(f"jev: {type(e).__name__}, falling back to code checks", file=sys.stderr)
        return None


# Generic words of the products and the stacks they run on. Without them Jev reads a plain
# line such as "copies it into a Kubernetes secret" as naming a resource (p=0.69 in testing).
PRODUCT_TERMS = ["AccuKnox", "KubeArmor", "Kubernetes", "cluster", "namespace", "workload", "pod",
                 "policy", "finding", "alert", "service account", "role binding", "role", "identity",
                 "Secrets Manager", "secret", "External Secret", "secret store", "operator",
                 "WordPress", "MySQL", "database", "AWS", "Azure", "GCP", "Oracle", "Terraform",
                 "CIEM", "CSPM", "CWPP", "DSPM", "AI security", "access graph"]


def narration(lines, terms=()):
    """Per line: {"identifier": p, "pronounce": p} probabilities, or None."""
    from typesafe_sdk import Noul
    state = {
        "purpose": "Voiceover script for a product video of a security platform, voiced over the "
                   "product's own screens. Generic product and technology words are expected.",
        "product_terms": PRODUCT_TERMS + list(terms),
        "lines": lines,
    }
    q = {}
    for i in range(len(lines)):
        q[f"id{i}"] = Noul(instructions=(
            f"Does `lines[{i}]` name a specific person, a customer or company, a hostname, an IP address, "
            "an account or resource ID, a container image or registry path, or a named cluster, pod or "
            "namespace? Generic product words in `product_terms` and plain descriptions do not count."))
        q[f"say{i}"] = Noul(instructions=(
            f"Would a text-to-speech voice likely mispronounce something in `lines[{i}]`, or spell it out "
            "letter by letter where the listener expects a word, such as an unexpanded acronym, a file "
            "path, a version string or a code identifier?"))
    r = _ask(state, q)
    if r is None:
        return None
    return [{"identifier": r.nouls[f"id{i}"].noul, "pronounce": r.nouls[f"say{i}"].noul} for i in range(len(lines))]


def narration_fallback(line):
    """Deterministic floor when Jev is off: patterns that are never safe to voice."""
    hits = []
    if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b", line):
        hits.append("IP address")
    if re.search(r"\b[a-z0-9-]+\.(com|net|io|lab|local|internal|svc)\b", line, re.I):
        hits.append("hostname")
    if re.search(r"\b[0-9a-f]{8,}\b", line, re.I) or re.search(r"\b\d{6,}\b", line):
        hits.append("ID or long number")
    if re.search(r"[/\\][\w.-]+[/\\]", line):
        hits.append("path")
    if re.search(r"\b[A-Z]{3,}\b", line):
        hits.append("acronym")
    return hits


def gate(lines, terms=()):
    """Check every narration line. Returns (blocked, warnings), each a list of (index, reason)."""
    blocked, warns = [], []
    scores = narration(lines, terms)
    for i, line in enumerate(lines):
        hits = narration_fallback(line)
        for h in hits:
            (warns if h == "acronym" else blocked).append((i, f"pattern: {h}"))
        if scores:
            s = scores[i]
            if s["identifier"] >= THRESHOLDS["identifier"]:
                blocked.append((i, f"jev: customer identifier p={s['identifier']:.2f}"))
            if s["pronounce"] >= THRESHOLDS["pronounce"]:
                warns.append((i, f"jev: hard to voice p={s['pronounce']:.2f}"))
    return blocked, warns, scores is not None


def cues(rows):
    """rows = [(mm:ss, text)]. Returns [(kind, confidence)] per cue, or None."""
    from typesafe_sdk import Choice
    out = []
    for s in range(0, len(rows), 60):   # batches keep each request small
        chunk = rows[s:s + 60]
        state = {"call": "A recorded screen-share demo of a security platform to a customer.",
                 "cues": [{"at": t, "text": x} for t, x in chunk]}
        q = {f"c{i}": Choice(instructions=f"What is caption `cues[{i}]` doing in the call?", criteria=CUE_KINDS)
             for i in range(len(chunk))}
        r = _ask(state, q)
        if r is None:
            return None
        out += [(r.choices[f"c{i}"].choice, r.choices[f"c{i}"].confidence) for i in range(len(chunk))]
    return out
