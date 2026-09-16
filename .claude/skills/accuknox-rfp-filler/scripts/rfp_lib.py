"""Shared helpers for the accuknox-rfp-filler scripts.

Everything more than one stage needs lives here: repo paths, the Pillow guard,
the doc-path to URL map, the answer vocabulary, brand values and image helpers.
"""
import hashlib
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.abspath(os.path.join(SKILL, "..", "..", ".."))
DOCS = os.path.join(REPO, "docs")
MODULES_JSON = os.path.join(SKILL, "assets", "modules.json")
LOGO = os.path.join(DOCS, "assets", "images", "ak-logo.png")

HELP_BASE = "https://help.accuknox.com/"
WEB_HOSTS = ("accuknox.com", "www.accuknox.com")

# Pages that exist in docs/ but are unpublished drafts. Never cite them.
DRAFT_PATTERNS = (
    re.compile(r"getting-started/3\.7-release"),
    re.compile(r"release-notes/v3\.7/"),
)

# Brand, from .claude/skills/accuknox-blog-writer/references/asset-kit.md
NAVY = "11206D"
ACCENT = "4D4DD9"
ALERT = "C80019"
BODY = "0D1B4B"
MUTED = "595959"

FLAG_FILL = {"GREEN": "C6EFCE", "AMBER": "FFEB9C", "RED": "FFC7CE"}
FLAG_FONT = {"GREEN": "006100", "AMBER": "9C5700", "RED": "9C0006"}

# Canonical verdicts. Every customer vocabulary maps onto these.
VERDICTS = ["EXCEEDS", "MEETS", "PARTIAL", "PARTNER", "CUSTOM",
            "ROADMAP_30", "ROADMAP_60", "ROADMAP_90", "ROADMAP_90PLUS",
            "ROADMAP", "INFO", "NEGATIVE"]
ROADMAP_ORDER = ["ROADMAP_30", "ROADMAP_60", "ROADMAP_90", "ROADMAP_90PLUS", "ROADMAP"]

# Order matters. A negative or partial phrase must match before "compliant".
_VOCAB_RULES = [
    ("NEGATIVE", r"\bnot\s+(planned|compliant|supported|available|applicable)\b|^\s*no\s*$"
                 r"|\bnon[- ]?compliant\b|\bunsupported\b|\bdoes not\b"),
    ("PARTIAL", r"\bpartial"),
    ("INFO", r"more info|clarif|need.*info"),
    ("ROADMAP_90PLUS", r"roadmap.*(90\s*\+|>\s*90|beyond)"),
    ("ROADMAP_30", r"roadmap.*\b30\b"),
    ("ROADMAP_60", r"roadmap.*\b60\b"),
    ("ROADMAP_90", r"roadmap.*\b90\b"),
    ("ROADMAP", r"roadmap|planned|future|in development|upcoming"),
    ("PARTNER", r"3rd party|third[- ]party|partner"),
    ("CUSTOM", r"custom|configurat|professional services"),
    ("EXCEEDS", r"exceed"),
    ("MEETS", r"\bmeets?\b|compliant|^\s*yes\s*$|\bsupported\b|\bavailable\b|\bcomply\b"),
]

# Phrases that mean "we do not have this today". A MEETS row must not carry them.
GAP_PHRASES = re.compile(
    r"\b(not (currently )?(available|supported|documented)|is not available|on the roadmap|"
    r"in roadmap|roadmap\b|planned for|coming soon|future release|does not (support|provide))",
    re.I)

BANNED = re.compile(
    r"\b(delve|delves|delving|leverage|leverages|leveraging|ensure|ensures|ensuring|"
    r"comprehensive|robust|seamless|seamlessly|streamlined|furthermore|moreover|additionally|"
    r"game-changer|cutting-edge|state-of-the-art|revolutioni[sz]e)\b|—|it'?s worth noting",
    re.I)


# Product names that contain a banned word. Stripped before the ban check.
PRODUCT_TERMS = re.compile(r"(?<![A-Za-z])Comprehensive(?= (scan|Scan|DAST|policy))")


def banned_hit(text):
    """First banned word or em dash in prose, ignoring product names."""
    m = BANNED.search(PRODUCT_TERMS.sub("", text or ""))
    return m.group(0) if m else None


def classify_option(text):
    """Map one customer dropdown option onto a canonical verdict, or None."""
    t = (text or "").strip().lower()
    for verdict, pat in _VOCAB_RULES:
        if re.search(pat, t):
            return verdict
    return None


def build_vocab(options):
    """options -> {verdict: exact customer string}, first match wins per verdict."""
    vocab = {}
    for o in options:
        v = classify_option(o)
        if v and v not in vocab:
            vocab[v] = o
    return vocab


def resolve_response(verdict, vocab):
    """Pick the customer's exact string for a canonical verdict.

    Returns (string, degraded_reason_or_None). Never returns a negative option.
    """
    if verdict == "NEGATIVE":
        raise ValueError("NEGATIVE verdicts are never written. Use a roadmap tier, PARTNER or PARTIAL.")
    if verdict in vocab:
        return vocab[verdict], None
    if verdict.startswith("ROADMAP"):
        start = ROADMAP_ORDER.index(verdict)
        for v in ROADMAP_ORDER[start:] + ROADMAP_ORDER[:start]:
            if v in vocab:
                return vocab[v], f"{verdict} not offered, used {v}"
        for v in ("PARTIAL", "INFO"):
            if v in vocab:
                return vocab[v], f"no roadmap option, used {v}"
        if "MEETS" in vocab:
            return vocab["MEETS"], ("no roadmap option in this RFP, answered with the positive option "
                                    "plus a roadmap statement. Human sign-off required")
    if verdict == "EXCEEDS" and "MEETS" in vocab:
        return vocab["MEETS"], None
    if verdict in ("PARTNER", "CUSTOM", "PARTIAL"):
        for v in ("PARTNER", "CUSTOM", "PARTIAL", "MEETS"):
            if v in vocab:
                return vocab[v], f"{verdict} not offered, used {v}"
    raise ValueError(f"cannot express {verdict} in this vocabulary: {sorted(vocab)}")


def require_pillow():
    try:
        import PIL  # noqa: F401
    except ImportError:
        sys.exit("FATAL: Pillow is not installed. Without it openpyxl reads 0 images and "
                 "silently deletes every picture on save. Run: pip install pillow openpyxl pyyaml")


def load_workbook(path):
    require_pillow()
    import openpyxl
    return openpyxl.load_workbook(path)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def image_count(wb):
    return {ws.title: len(ws._images) for ws in wb.worksheets}


def anchored_rows(ws):
    return {im.anchor._from.row + 1 for im in ws._images}


def cell_text(v):
    return " ".join(str(v).split()) if v is not None else ""


# ------------------------------------------------------------- doc paths ---

def doc_url(rel):
    """docs-relative .md path -> live help.accuknox.com URL (use_directory_urls)."""
    rel = rel.replace("\\", "/")
    if rel.startswith("docs/"):
        rel = rel[5:]
    rel = re.sub(r"\.md$", "", rel)
    if rel == "index":
        return HELP_BASE
    if rel.endswith("/index"):
        rel = rel[: -len("index")]
    else:
        rel += "/"
    return HELP_BASE + rel


def is_draft(path_or_url):
    s = str(path_or_url).replace("\\", "/")
    return any(p.search(s) for p in DRAFT_PATTERNS)


_NAV = None


def nav_pages():
    global _NAV
    if _NAV is not None:
        return _NAV
    import yaml

    class Loader(yaml.SafeLoader):
        pass

    Loader.add_multi_constructor("tag:yaml.org,2002:python/", lambda loader, suffix, node: None)
    with open(os.path.join(REPO, "mkdocs.yml"), encoding="utf-8") as f:
        cfg = yaml.load(f, Loader=Loader)
    pages = set()

    def walk(node):
        if isinstance(node, str):
            if node.endswith(".md"):
                pages.add(node)
        elif isinstance(node, list):
            for x in node:
                walk(x)
        elif isinstance(node, dict):
            for x in node.values():
                walk(x)

    walk(cfg.get("nav", []))
    _NAV = pages
    return pages


def in_nav(rel):
    rel = rel.replace("\\", "/")
    rel = rel[5:] if rel.startswith("docs/") else rel
    return rel in nav_pages()


def url_status(url, tries=3):
    """HTTP status with retries. Transient network errors are common here."""
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 accuknox-rfp-filler"})
            return urllib.request.urlopen(req, timeout=30).status
        except urllib.error.HTTPError as e:
            return e.code
        except Exception as e:  # noqa: BLE001
            last = type(e).__name__
            time.sleep(2 * (i + 1))
    return last


# ------------------------------------------------------------- images ------

def image_bytes(src, target_w=270, max_h=210):
    """Resize any image file to evidence size. Returns (PNG buffer, w, h)."""
    from PIL import Image
    im = Image.open(src)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA")
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    w, h = im.size
    nw, nh = target_w, max(1, int(h * target_w / w))
    if nh > max_h:
        nw, nh = max(1, int(w * max_h / h)), max_h
    im = im.resize((nw, nh), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG")
    buf.seek(0)
    return buf, nw, nh


def add_image(ws, row, col, src, target_w=270, max_h=210):
    """Anchor an image at (row, col) with a one-cell anchor, and grow the row to fit."""
    from openpyxl.drawing.image import Image as XLImage
    from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, OneCellAnchor
    from openpyxl.drawing.xdr import XDRPositiveSize2D
    from openpyxl.utils.units import pixels_to_EMU

    buf, w, h = image_bytes(src, target_w, max_h)
    img = XLImage(buf)
    img.width, img.height = w, h
    img.anchor = OneCellAnchor(
        _from=AnchorMarker(col=col - 1, colOff=pixels_to_EMU(4), row=row - 1, rowOff=pixels_to_EMU(4)),
        ext=XDRPositiveSize2D(pixels_to_EMU(w), pixels_to_EMU(h)),
    )
    ws.add_image(img)
    need = h * 0.75 + 12
    if (ws.row_dimensions[row].height or 15) < need:
        ws.row_dimensions[row].height = need
    return w, h


def resolve_image(ref, workdir):
    """Turn an answer's image reference into a local file path.

    docs/<path>   a help docs image (preferred)
    gen:<file>    a diagram rendered by diagram.py into <workdir>/gen/
    web:<url>     an accuknox.com image, cached into <workdir>/web/
    """
    if not ref:
        return None
    if ref.startswith("gen:"):
        p = os.path.join(workdir, "gen", ref[4:])
    elif ref.startswith("web:"):
        p = fetch_web_image(ref[4:], os.path.join(workdir, "web"))
    else:
        rel = ref[5:] if ref.startswith("docs/") else ref
        p = os.path.join(DOCS, rel.replace("/", os.sep))
    if is_draft(p):
        raise ValueError(f"image is from an unpublished draft: {ref}")
    if not os.path.isfile(p):
        raise FileNotFoundError(f"image not found: {ref} -> {p}")
    return p


def fetch_web_image(url, cache_dir):
    from urllib.parse import urlparse
    host = urlparse(url).hostname or ""
    if host not in WEB_HOSTS:
        raise ValueError(f"web images are limited to accuknox.com, got {host}")
    os.makedirs(cache_dir, exist_ok=True)
    name = hashlib.sha1(url.encode()).hexdigest()[:12] + os.path.splitext(urlparse(url).path)[1][:5]
    p = os.path.join(cache_dir, name)
    if not os.path.isfile(p):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 accuknox-rfp-filler"})
        with urllib.request.urlopen(req, timeout=30) as r, open(p, "wb") as f:
            f.write(r.read())
    return p


# ------------------------------------------------------------- io ----------

def read_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def write_json(p, data):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False, default=str)


def inside_repo(path):
    return os.path.abspath(path).lower().startswith(REPO.lower() + os.sep.lower())


def workdir_for(rfp_path, allow_repo=False):
    """Working folder beside the customer file. Never inside the public repo."""
    base = os.path.splitext(os.path.abspath(rfp_path))[0] + ".rfp-work"
    if inside_repo(base) and not allow_repo:
        sys.exit("Refusing to write customer RFP work inside the help-docs repo, which is public on "
                 "GitHub. Copy the RFP outside the repo, for example to Downloads, and run again.")
    os.makedirs(base, exist_ok=True)
    return base


# ------------------------------------------------------------- routing -----

_MODS = None


def modules():
    global _MODS
    if _MODS is None:
        _MODS = read_json(MODULES_JSON)
    return _MODS


def _kw_hit(kw, text):
    return re.search(r"(?<![a-z0-9])" + re.escape(kw) + r"(?:s|es)?(?![a-z0-9])", text) is not None


def route(text, context="", top=2):
    """Score a requirement against the 12 modules. Returns [(module_id, score)].

    `context` is the sheet name and section heading. It counts at half weight,
    so a sheet called DAST pulls an ambiguous row toward ASPM without
    overriding a row that clearly names another module.
    """
    t = (text or "").lower()
    c = (context or "").lower()
    scores = []
    for m in modules()["modules"]:
        s = 0.0
        for kw in m["keywords"]:
            w = 2 if (" " in kw or "-" in kw) else 1
            if _kw_hit(kw, t):
                s += w
            elif c and _kw_hit(kw, c):
                s += w * 0.5
        if s:
            scores.append((m["id"], s))
    if not scores:
        scores = search_route(text)
    scores.sort(key=lambda x: -x[1])
    return scores[:top]


# ------------------------------------------------------------- doc search --

_STOP = set("""a an the and or of to in for on with by as at is are be shall should must may can will
solution system tool product vendor support supports provide provides capability capable ability able allow
allows including include such other any all each using use used which that this these those from into its it
their they than then also etc via per where ever wherever applicable required requirement proposed offer
offers have has not""".split())


def tokens(text):
    return [w for w in re.findall(r"[a-z][a-z0-9+#.-]{1,}", (text or "").lower()) if w not in _STOP]


_INDEX = None


def doc_index():
    """BM25 index over published docs pages, cached in the temp folder."""
    global _INDEX
    if _INDEX is not None:
        return _INDEX
    import math
    import tempfile
    files = []
    for root, _, names in os.walk(DOCS):
        for n in names:
            if n.endswith(".md") and n != "README.md":
                rel = os.path.relpath(os.path.join(root, n), DOCS).replace(os.sep, "/")
                if not is_draft(rel):
                    files.append(rel)
    stamp = max(os.path.getmtime(os.path.join(DOCS, f)) for f in files)
    cache = os.path.join(tempfile.gettempdir(), "accuknox-rfp-filler-index.json")
    if os.path.isfile(cache):
        data = read_json(cache)
        if data.get("stamp") == stamp and data.get("n") == len(files):
            _INDEX = data
            return data
    docs = {}
    df = {}
    for rel in files:
        with open(os.path.join(DOCS, rel), encoding="utf-8", errors="ignore") as f:
            raw = f.read()
        body = re.sub(r"<style.*?</style>|<script.*?</script>", " ", raw, flags=re.S)
        title = re.search(r"^title:\s*(.+)$", raw, re.M)
        heads = " ".join(re.findall(r"^#+\s*(.+)$", body, re.M))
        toks = tokens(body) + tokens(heads) * 3 + tokens(title.group(1) if title else "") * 3
        tf = {}
        for t in toks:
            tf[t] = tf.get(t, 0) + 1
        docs[rel] = {"len": len(toks), "tf": tf, "title": title.group(1).strip().strip('"') if title else rel}
        for t in tf:
            df[t] = df.get(t, 0) + 1
    n = len(docs)
    idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}
    avg = sum(d["len"] for d in docs.values()) / max(1, n)
    _INDEX = {"stamp": stamp, "n": n, "docs": docs, "idf": idf, "avg": avg}
    write_json(cache, _INDEX)
    return _INDEX


def search_docs(query, top=5, prefer=()):
    """Rank published docs pages for a query. `prefer` boosts a module's own pages."""
    idx = doc_index()
    q = set(tokens(query))
    k1, b = 1.4, 0.75
    out = []
    for rel, d in idx["docs"].items():
        s = 0.0
        for t in q:
            f = d["tf"].get(t)
            if f:
                s += idx["idf"].get(t, 0) * f * (k1 + 1) / (f + k1 * (1 - b + b * d["len"] / idx["avg"]))
        if s:
            if rel in prefer:
                s *= 1.35
            if not in_nav(rel):
                s *= 0.6
            if "release" in rel:
                s *= 0.7
            out.append((rel, round(s, 2), d["title"]))
    out.sort(key=lambda x: -x[1])
    return out[:top]


def page_modules():
    m = {}
    for mod in modules()["modules"]:
        for k in ("pages", "matrices", "faqs"):
            for p in mod[k]:
                m.setdefault(p, mod["id"])
    return m


def search_route(text, min_score=6.0):
    """Fallback routing through doc search when no keyword hits."""
    pm = page_modules()
    scores = {}
    for rel, s, _ in search_docs(text, top=8):
        mid = pm.get(rel)
        if mid and s >= min_score:
            scores[mid] = scores.get(mid, 0) + round(s / 10, 2)
    return list(scores.items())


def fit_risks(text):
    t = (text or "").lower()
    return [r["topic"] for r in modules()["fit_risks"] if re.search(r["pattern"], t)]


def module_by_id(mid):
    for m in modules()["modules"]:
        if m["id"] == mid:
            return m
    raise KeyError(mid)
