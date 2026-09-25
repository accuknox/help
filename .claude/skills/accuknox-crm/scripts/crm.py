#!/usr/bin/env python3
"""Client and CLI for the AccuKnox CRM REST API (https://crm.accuknox.com/rest).

The CRM is the open-source trycompai/crm app. Every tRPC procedure is served over
REST under /rest, and the live OpenAPI document is at /openapi.json.

The API key is read at run time and never written anywhere:
  1. the CRM_API_KEY environment variable
  2. a CRM_API_KEY= line in ./.env
  3. a CRM_API_KEY= line in the file named by CRM_ENV_FILE

Use it as a CLI:
  python crm.py whoami
  python crm.py spec                       # every endpoint, grouped by tag
  python crm.py spec --path /deals         # request schema for matching paths
  python crm.py search companies --q acme --all --out acme.csv
  python crm.py get deals <id>
  python crm.py fields COMPANY
  python crm.py call PATCH /deals/<id> --data '{"data": {"amountCents": 500000}}'
  python crm.py bulk update contacts edits.csv --dry-run

Or import it:
  from crm import Crm
  crm = Crm()
  for row in crm.search_all("deals", {"stage": ["CLOSED_WON"]}):
      print(row["name"])
"""

import argparse
import csv
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("pip install requests")

BASE = os.environ.get("CRM_BASE_URL", "https://crm.accuknox.com").rstrip("/")
REST = BASE + "/rest"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "..", ".cache")
SPEC_CACHE = os.path.join(CACHE, "openapi.json")
# Nest controllers (operationId "XController_y") are served at the site root.
# Every other path is a tRPC procedure on the REST bridge under /rest.
ROOT_PREFIXES = ("/auth/", "/health", "/internal/", "/api/")
KEY_FILES = [os.path.join(os.getcwd(), ".env")] + (
    [os.environ["CRM_ENV_FILE"]] if os.environ.get("CRM_ENV_FILE") else [])

# Entity name -> REST collection. Accepts singular, plural and field-entity names.
ENTITIES = {
    "company": "companies", "companies": "companies", "COMPANY": "companies",
    "contact": "contacts", "contacts": "contacts", "CONTACT": "contacts",
    "deal": "deals", "deals": "deals", "DEAL": "deals",
}
FIELD_ENTITY = {"companies": "COMPANY", "contacts": "CONTACT", "deals": "DEAL"}

# Calls that delete data, revoke access, or change workspace-wide settings.
# The CLI refuses them without --yes.
DANGEROUS = [
    (r"DELETE", r".*"),
    (r"POST", r".*/(bulk-)?purge.*"),
    (r"POST", r".*/purge-synced-data"),
    (r"POST", r".*/revoke"),
    (r"POST", r"/api-keys"),
    (r"(PATCH|PUT|POST)", r"/(workspace|sso|settings|currency|tracking|slack)(/.*)?"),
    (r"POST", r"/internal/.*"),
]


def load_key():
    key = os.environ.get("CRM_API_KEY", "").strip()
    if key:
        return key
    for path in KEY_FILES:
        try:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    m = re.match(r"\s*CRM_API_KEY\s*=\s*['\"]?([^'\"\s]+)", line)
                    if m:
                        return m.group(1)
        except OSError:
            continue
    sys.exit("No CRM key. Set CRM_API_KEY, or add CRM_API_KEY=crm_... to a .env file.")


def fix_path(path):
    """Undo Git Bash turning /deals/x into C:/Program Files/Git/deals/x."""
    m = re.match(r"^[A-Za-z]:/.*?/Git(/.*)$", path)
    path = m.group(1) if m else path
    return path if path.startswith(("/", "http")) else "/" + path


def is_dangerous(method, path):
    return any(re.fullmatch(m, method.upper()) and re.fullmatch(p, path) for m, p in DANGEROUS)


class CrmError(Exception):
    def __init__(self, status, body):
        super().__init__(f"HTTP {status}: {body[:500]}")
        self.status = status
        self.body = body


class Crm:
    """Thin REST client. Retries 429 and 5xx with backoff, raises CrmError otherwise."""

    def __init__(self, key=None):
        self.key = key or load_key()
        self._local = threading.local()

    def _session(self):
        if not hasattr(self._local, "s"):
            s = requests.Session()
            s.headers.update({"x-api-key": self.key, "content-type": "application/json"})
            self._local.s = s
        return self._local.s

    def call(self, method, path, body=None, query=None, retries=6):
        path = fix_path(path)
        if path.startswith("http"):
            url = path
        else:
            url = (BASE if path.startswith(ROOT_PREFIXES) else REST) + path
        last = ""
        for attempt in range(retries):
            try:
                r = self._session().request(method.upper(), url, json=body, params=query, timeout=90)
            except requests.RequestException as exc:
                last = str(exc)
            else:
                if r.status_code < 400:
                    return r.json() if r.content else None
                if r.status_code not in (429, 500, 502, 503, 504):
                    raise CrmError(r.status_code, r.text)
                last = f"{r.status_code} {r.text[:200]}"
            time.sleep(min(30, 2 ** attempt))
        raise CrmError(0, f"gave up after {retries} tries: {last}")

    # ---- convenience wrappers

    def get(self, path, **query):
        return self.call("GET", path, query=query or None)

    def post(self, path, body=None):
        return self.call("POST", path, body or {})

    def patch(self, path, data):
        """PATCH /companies|contacts|deals/{id} take {"data": {...}}. Pass the inner dict."""
        return self.call("PATCH", path, {"data": data})

    def search(self, entity, filters=None, page=1, page_size=100):
        coll = ENTITIES[entity]
        body = {"page": page, "pageSize": page_size, **(filters or {})}
        return self.post(f"/{coll}/search", body)

    def search_all(self, entity, filters=None, limit=None):
        """Yield every row that matches, 100 per page."""
        page, seen = 1, 0
        while True:
            res = self.search(entity, filters, page=page)
            for row in res["rows"]:
                yield row
                seen += 1
                if limit and seen >= limit:
                    return
            if page * 100 >= res["total"] or not res["rows"]:
                return
            page += 1

    def record(self, entity, record_id):
        return self.get(f"/{ENTITIES[entity]}/{record_id}")

    def fields(self, entity, include_archived=False):
        fe = FIELD_ENTITY.get(ENTITIES.get(entity, ""), entity.upper())
        return self.get("/fields", entity=fe, includeArchived=str(include_archived).lower())

    def users(self):
        return self.get("/users")

    def spec(self, refresh=False):
        if not refresh and os.path.exists(SPEC_CACHE) and time.time() - os.path.getmtime(SPEC_CACHE) < 86400:
            with open(SPEC_CACHE, encoding="utf-8") as f:
                return json.load(f)
        r = requests.get(BASE + "/openapi.json", timeout=60)
        r.raise_for_status()
        os.makedirs(CACHE, exist_ok=True)
        with open(SPEC_CACHE, "w", encoding="utf-8") as f:
            f.write(r.text)
        return r.json()


# ---------------------------------------------------------------- output

def flatten(row, prefix=""):
    """Nested dicts become dotted columns. Custom field lists become fields.<key>."""
    out = {}
    for k, v in row.items():
        key = f"{prefix}{k}"
        if k == "fields" and isinstance(v, list):
            for f in v:
                out[f"fields.{f.get('key')}"] = f.get("value")
        elif k == "fields" and isinstance(v, dict):
            for fk, fv in v.items():
                out[f"fields.{fk}"] = fv
        elif isinstance(v, dict):
            out.update(flatten(v, key + "."))
        elif isinstance(v, list):
            out[key] = json.dumps(v, ensure_ascii=False)
        else:
            out[key] = v
    return out


def write_rows(rows, out):
    rows = list(rows)
    if not out:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return
    if out.endswith(".json"):
        with open(out, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2, ensure_ascii=False)
    else:
        flat = [flatten(r) for r in rows]
        cols = list(dict.fromkeys(k for r in flat for k in r))
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(flat)
    print(f"wrote {len(rows)} rows to {out}", file=sys.stderr)


def parse_data(value):
    if value is None:
        return None
    if value.startswith("@"):
        with open(value[1:], encoding="utf-8") as f:
            return json.load(f)
    return json.loads(value)


# ---------------------------------------------------------------- bulk

def bulk(crm, action, entity, path, dry_run, workers, yes):
    """Create or update records from a CSV.

    create: columns are create-body fields (e.g. name, domain for companies).
            A column named fields.<key> sets that custom field after the create.
    update: needs an id column. Every other column goes into PATCH data.
            fields.<key> columns go into data.fields.
    Empty cells are skipped, so a blank never wipes a value.
    Progress is kept in <csv>.state.json so a rerun resumes.
    """
    coll = ENTITIES[entity]
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    state_path = path + ".state.json"
    state = json.load(open(state_path, encoding="utf-8")) if os.path.exists(state_path) else {}
    lock = threading.Lock()
    errors = []

    def split(row):
        top, fields = {}, {}
        for k, v in row.items():
            if v is None or str(v).strip() == "" or k == "id":
                continue
            v = str(v).strip()
            if k.startswith("fields."):
                fields[k[7:]] = v
            elif k == "amountCents":
                top[k] = int(float(v))
            else:
                top[k] = v
        return top, fields

    def one(i, row):
        key = row.get("id") or f"row{i}"
        if state.get(key):
            return "skip"
        top, fields = split(row)
        if dry_run:
            return f"{action} {key}: {json.dumps({**top, 'fields': fields} if fields else top)[:200]}"
        if action == "create":
            rec = crm.post(f"/{coll}", top)
            if fields:
                crm.patch(f"/{coll}/{rec['id']}", {"fields": fields})
            result = rec["id"]
        else:
            if not row.get("id"):
                raise ValueError("update rows need an id column")
            data = dict(top)
            if fields:
                data["fields"] = fields
            crm.patch(f"/{coll}/{row['id']}", data)
            result = row["id"]
        with lock:
            state[key] = result
        return "ok"

    if not dry_run and len(rows) > 50 and not yes:
        sys.exit(f"{len(rows)} rows. Rerun with --yes to write them, or --dry-run to preview.")

    done = 0
    with ThreadPoolExecutor(max_workers=1 if dry_run else workers) as pool:
        futs = {pool.submit(one, i, r): i for i, r in enumerate(rows)}
        for fut in as_completed(futs):
            i = futs[fut]
            try:
                res = fut.result()
                if dry_run and done < 20:
                    print(res)
            except Exception as e:  # noqa: BLE001
                errors.append((i, str(e)[:300]))
            done += 1
            if not dry_run and done % 100 == 0:
                print(f"  {done}/{len(rows)}  errors {len(errors)}", file=sys.stderr)
                with lock:
                    json.dump(state, open(state_path, "w", encoding="utf-8"))
    if not dry_run:
        json.dump(state, open(state_path, "w", encoding="utf-8"))
    print(f"{action}: {done} rows, {len(errors)} errors" + (" (dry run)" if dry_run else ""))
    for i, e in errors[:20]:
        print(f"  row {i + 2}: {e}")


# ---------------------------------------------------------------- CLI

def cmd_spec(crm, args):
    spec = crm.spec(refresh=args.refresh)
    if args.path:
        for p, ops in spec["paths"].items():
            if args.path.lower() not in p.lower():
                continue
            for m, op in ops.items():
                print(f"\n{m.upper()} {p}   [{', '.join(op.get('tags', []))}]")
                for prm in op.get("parameters", []):
                    print(f"  {prm['in']}: {prm['name']}{' (required)' if prm.get('required') else ''} "
                          f"{json.dumps(prm.get('schema', {}))[:160]}")
                body = op.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
                if body:
                    print("  body:", json.dumps(body, indent=1)[: args.max])
        return
    by_tag = {}
    for p, ops in spec["paths"].items():
        for m, op in ops.items():
            tag = (op.get("tags") or ["Other"])[0]
            if args.tag and args.tag.lower() not in tag.lower():
                continue
            by_tag.setdefault(tag, []).append(f"{m.upper():6} {p}")
    for tag in sorted(by_tag):
        print(f"\n## {tag}")
        for line in sorted(by_tag[tag], key=lambda s: s.split()[1]):
            flag = "  !" if is_dangerous(line.split()[0], line.split()[1]) else ""
            print(f"  {line}{flag}")
    print("\n! = deletes data or changes workspace settings. The CLI asks for --yes.")


def main():
    ap = argparse.ArgumentParser(description="AccuKnox CRM API client")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("whoami", help="check the key and show the workspace")

    s = sub.add_parser("spec", help="list endpoints or show request schemas")
    s.add_argument("--tag")
    s.add_argument("--path", help="substring of the path, e.g. /deals")
    s.add_argument("--refresh", action="store_true")
    s.add_argument("--max", type=int, default=4000, help="max chars of body schema")

    s = sub.add_parser("search", help="list records with filters, paged")
    s.add_argument("entity", choices=["companies", "contacts", "deals"])
    s.add_argument("--q", default="")
    s.add_argument("--filter", help='JSON merged into the search body, e.g. {"stage":["CLOSED_WON"]}')
    s.add_argument("--archived", action="store_true")
    s.add_argument("--all", action="store_true", help="every page, not just the first 100")
    s.add_argument("--limit", type=int)
    s.add_argument("--out", help="write .csv or .json instead of printing")

    s = sub.add_parser("get", help="one record by id")
    s.add_argument("entity", choices=["companies", "contacts", "deals"])
    s.add_argument("id")

    s = sub.add_parser("fields", help="custom field definitions")
    s.add_argument("entity", choices=["COMPANY", "CONTACT", "DEAL"])

    sub.add_parser("users", help="workspace users (valid ownerId values)")
    sub.add_parser("queue", help="agent task queue size")
    sub.add_parser("counts", help="record totals")

    s = sub.add_parser("call", help="any endpoint")
    s.add_argument("method")
    s.add_argument("path", help="path under /rest, e.g. /deals/search")
    s.add_argument("--data", help="JSON body, or @file.json")
    s.add_argument("--query", nargs="*", default=[], help="k=v query params")
    s.add_argument("--yes", action="store_true", help="allow a dangerous call")

    s = sub.add_parser("bulk", help="create or update records from a CSV")
    s.add_argument("action", choices=["create", "update"])
    s.add_argument("entity", choices=["companies", "contacts", "deals"])
    s.add_argument("csv")
    s.add_argument("--dry-run", action="store_true")
    s.add_argument("--workers", type=int, default=6)
    s.add_argument("--yes", action="store_true")

    args = ap.parse_args()
    crm = Crm()

    if args.cmd == "whoami":
        ws = crm.get("/workspace")
        me = crm.get("/auth/me")
        print(json.dumps({"workspace": ws, "me": me}, indent=2))
    elif args.cmd == "spec":
        cmd_spec(crm, args)
    elif args.cmd == "search":
        filters = {"q": args.q, "archived": args.archived, **(json.loads(args.filter) if args.filter else {})}
        if args.all or args.limit:
            rows = crm.search_all(args.entity, filters, limit=args.limit)
        else:
            res = crm.search(args.entity, filters)
            print(f"total {res['total']}", file=sys.stderr)
            rows = res["rows"]
        write_rows(rows, args.out)
    elif args.cmd == "get":
        print(json.dumps(crm.record(args.entity, args.id), indent=2, ensure_ascii=False))
    elif args.cmd == "fields":
        for f in crm.fields(args.entity, include_archived=True):
            opts = ", ".join(o["label"] for o in f.get("options", []))
            print(f"{f['key']:28} {f['type']:10} {f['label']}"
                  f"{'  [agent]' if f.get('agentFilled') else ''}"
                  f"{'  [archived]' if f.get('archivedAt') else ''}"
                  f"{'  options: ' + opts if opts else ''}")
    elif args.cmd == "users":
        for u in crm.users():
            print(f"{u['id']}  {u['name']}  <{u['email']}>")
    elif args.cmd == "queue":
        q = crm.get("/enrichment/queue")
        print(f"due {q['total']}, scheduled {q['scheduledTotal']}")
    elif args.cmd == "counts":
        for e in ("companies", "contacts", "deals"):
            print(f"{e}: {crm.search(e, page_size=1)['total']}")
    elif args.cmd == "call":
        path = fix_path(args.path)
        if is_dangerous(args.method, path) and not args.yes:
            sys.exit(f"{args.method.upper()} {path} deletes data or changes settings. Rerun with --yes.")
        query = dict(kv.split("=", 1) for kv in args.query)
        res = crm.call(args.method, path, parse_data(args.data), query or None)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.cmd == "bulk":
        bulk(crm, args.action, args.entity, args.csv, args.dry_run, args.workers, args.yes)


if __name__ == "__main__":
    try:
        main()
    except CrmError as e:
        sys.exit(str(e))
