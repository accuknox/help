"""Self-test for accuknox-rfp-filler. Run it after any edit to the skill.

    python selftest.py            offline checks plus a full synthetic run
    python selftest.py --samples  also profile the client RFPs under references/rfp-generation

Everything is written to a temp folder. Nothing lands in the repo.
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rfp_lib as L  # noqa: E402

FAILS = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    if not ok:
        FAILS.append(name)


def run(*args):
    p = subprocess.run([sys.executable, *args], capture_output=True, text=True, cwd=HERE)
    return p.returncode, p.stdout + p.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", action="store_true")
    a = ap.parse_args()
    L.require_pillow()

    # module map
    missing = []
    for m in L.modules()["modules"]:
        for k in ("pages", "matrices", "faqs"):
            missing += [p for p in m[k] if not os.path.isfile(os.path.join(L.DOCS, p))]
        missing += [d for d in m["image_dirs"] if not os.path.isdir(os.path.join(L.DOCS, d))]
        missing += [x["source"] for x in m["limits"] if not os.path.isfile(os.path.join(L.DOCS, x["source"]))]
    check("modules.json has 12 modules", len(L.modules()["modules"]) == 12)
    check("every module path exists", not missing, missing[:5])

    # vocabulary mapping
    cases = {
        "1 - Meets": "MEETS", "2 - Exceeds": "EXCEEDS", "3 -  Roadmap - 30 days": "ROADMAP_30",
        "6 - Roadmap - 90+ days": "ROADMAP_90PLUS", "7 - Achieved via 3rd party integration": "PARTNER",
        "8 - Not Planned": "NEGATIVE", "Fully Compliant": "MEETS", "Partially Compliant": "PARTIAL",
        "Not Compliant": "NEGATIVE", "Yes": "MEETS", "No": "NEGATIVE", "Compliant": "MEETS",
        "Roadmap": "ROADMAP", "Partial Compliant": "PARTIAL", "Need More Info": "INFO",
    }
    bad = {k: L.classify_option(k) for k, v in cases.items() if L.classify_option(k) != v}
    check("dropdown vocabularies classify", not bad, bad)

    yesno = L.build_vocab(["Yes", "No"])
    resp, why = L.resolve_response("ROADMAP_60", yesno)
    check("roadmap on a Yes/No sheet needs sign-off", resp == "Yes" and "sign-off" in why, why)
    try:
        L.resolve_response("NEGATIVE", yesno)
        check("NEGATIVE is refused", False)
    except ValueError:
        check("NEGATIVE is refused", True)
    tdm = L.build_vocab(["1 - Meets", "2 - Exceeds", "3 -  Roadmap - 30 days", "5 - Roadmap - 90 days", "8 - Not Planned"])
    check("missing tier falls to the next tier", L.resolve_response("ROADMAP_60", tdm)[0] == "5 - Roadmap - 90 days")

    # urls and drafts
    check("doc_url maps pages", L.doc_url("docs/how-to/sca.md") == "https://help.accuknox.com/how-to/sca/"
          and L.doc_url("secrets-manager/index.md") == "https://help.accuknox.com/secrets-manager/")
    check("v3.7 drafts are blocked", L.is_draft("docs/getting-started/3.7-release.md")
          and L.is_draft("images/release-notes/v3.7/x.png") and not L.is_draft("release-notes/v3.6/x.png"))
    check("nav parser reads mkdocs.yml", L.in_nav("how-to/sca.md") and len(L.nav_pages()) > 300)

    # ban list
    check("ban list catches prose, spares product names",
          L.banned_hit("a comprehensive platform") and L.banned_hit("fast — slow")
          and not L.banned_hit("The Comprehensive scan runs") and not L.banned_hit("plain text"))

    # routing and search
    check("router: mobile SAST -> aspm", L.route("mobile application code analysis for Android and iOS")[0][0] == "aspm")
    check("router: Jira defects -> integrations", L.route("integrate with Jira to track defects")[0][0] == "integrations")
    check("router: KnoxGuard admission -> kspm", L.route("admission controller to block vulnerable images")[0][0] == "kspm")
    check("fit risk: CIEM flagged", "CIEM or cloud entitlement analytics" in L.fit_risks("Provide CIEM analytics"))
    hits = L.search_docs("prompt injection firewall", top=3)
    check("docs search finds AI pages", any("prompt" in h[0] for h in hits), [h[0] for h in hits])

    tmp = tempfile.mkdtemp(prefix="rfp-selftest-")
    try:
        # synthetic RFP through the full pipeline
        req = {"customer": "Selftest Bank", "title": "Selftest RFP", "sections": [
            {"name": "Application security", "rows": [
                {"id": "A-1", "requirement": "The solution shall support SAST for Java and Kotlin.", "priority": "Mandatory"},
                {"id": "A-2", "requirement": "The solution shall generate an SBOM in CycloneDX format.", "priority": "Desirable"}]},
            {"name": "Endpoint", "rows": [
                {"id": "E-1", "requirement": "The solution shall provide EDR for employee laptops.", "priority": "Mandatory"}]}]}
        rj = os.path.join(tmp, "req.json")
        json.dump(req, open(rj, "w"))
        xlsx = os.path.join(tmp, "synthetic.xlsx")
        code, out = run("template.py", rj, xlsx)
        check("template.py builds a workbook", code == 0 and os.path.isfile(xlsx), out.strip()[-120:])
        code, out = run("intake.py", xlsx)
        check("intake.py reads the template", code == 0 and "requirements 3" in out, out.strip()[-300:])
        wd = xlsx[:-5] + ".rfp-work"
        prof = L.read_json(os.path.join(wd, "profile.json"))
        cols = prof["sheets"][0]["columns"]
        check("intake finds the template columns", cols["requirement"] == 3 and cols["response"] == 5
              and cols["comment"] == 6 and cols["evidence"] == 7, cols)
        e1 = [x for x in prof["sheets"][0]["rows"] if x["id"] == "E-1"][0]
        check("EDR row carries a fit risk", "Endpoint EDR or XDR" in e1["fit_risks"], e1["fit_risks"])

        code, out = run("ground.py", wd, "--all")
        check("ground.py builds evidence", code == 0 and "evidence packs 3" in out, out.strip()[-160:])
        code, out = run("diagram.py", "--demo", os.path.join(wd, "gen"))
        check("diagram.py renders PNG and SVG", code == 0 and os.path.isfile(os.path.join(wd, "gen", "demo-bars.svg")))

        rows = [x["row"] for x in prof["sheets"][0]["rows"] if x["kind"] == "requirement"]
        ans = {"customer": "Selftest Bank", "rows": [
            {"sheet": "Requirements", "row": rows[0], "verdict": "MEETS", "module": "aspm",
             "bullets": ["SAST rule counts cover Java and Kotlin."],
             "urls": ["https://help.accuknox.com/support-matrix/sast-support-matrix/"],
             "image": "gen:demo-bars.png", "flag": "GREEN", "note": "matrix"},
            {"sheet": "Requirements", "row": rows[1], "verdict": "MEETS", "module": "aspm",
             "bullets": ["xBOM generates SBOM output."],
             "urls": ["https://help.accuknox.com/getting-started/xbom-setup/"],
             "image": None, "flag": "AMBER", "note": "no screenshot chosen"},
            {"sheet": "Requirements", "row": rows[2], "verdict": "ROADMAP_90PLUS", "module": "vmsec",
             "bullets": ["Laptop EDR is outside the documented scope. Host malware scanning covers servers today, and endpoint coverage is on the roadmap."],
             "urls": ["https://help.accuknox.com/use-cases/vm-malware-scan/"],
             "image": None, "flag": "RED", "note": "not a fit, confirm with sales"}]}
        aj = os.path.join(tmp, "answers.json")
        json.dump(ans, open(aj, "w"))
        code, out = run("fill.py", wd, aj)
        check("fill.py writes both copies", code == 0 and "Response" in out and "Review" in out, out.strip()[-200:])
        code, out = run("validate.py", wd, "--offline")
        check("validate.py passes the synthetic run", code == 0, out.strip()[-400:])

        bad_ans = dict(ans, rows=[dict(ans["rows"][0], bullets=["A comprehensive answer."])])
        json.dump(bad_ans, open(aj, "w"))
        code, out = run("fill.py", wd, aj)
        check("fill.py stops on a banned word", code != 0 and "banned" in out, out.strip()[-120:])
        neg = dict(ans, rows=[dict(ans["rows"][0], verdict="NEGATIVE")])
        json.dump(neg, open(aj, "w"))
        code, out = run("fill.py", wd, aj)
        check("fill.py stops on a NEGATIVE verdict", code != 0 and "NEGATIVE" in out)

        code, out = run("intake.py", os.path.join(L.DOCS, "..", "mkdocs.yml"))
        check("intake refuses non-RFP files", code != 0)

        if a.samples:
            for f in glob.glob(os.path.join(L.REPO, "references", "rfp-generation", "responses", "client-rfps", "*.xlsx")):
                dst = os.path.join(tmp, os.path.basename(f))
                shutil.copy2(f, dst)
                code, out = run("intake.py", dst)
                fit = [ln for ln in out.splitlines() if ln.startswith("FIT")]
                check(f"sample {os.path.basename(f)} profiles", code == 0, fit[0] if fit else out[-200:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"\n{len(FAILS)} failed" if FAILS else "\nall checks passed")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
