# -*- coding: utf-8 -*-
"""Rewrite the online Google Sheet from netskope_data.py through the Sheets API.

An XLSX cell holds one hyperlink, so the XLSX route cannot carry several
[LINK] anchors per cell. This script writes rich-text cells directly.

Three tabs: Summary, Comparison, Sources. Comparison has five columns:
ID, Capability, AccuKnox, Netskope, Edge. Status, text and links share a cell.

Run:  py -3.11 references/competitive/battlecards/netskope/push_sheet.py
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import netskope_data as d  # noqa: E402

SHEET_ID = "1lwmd_SXI43toqkLhjRJUlusFfutf43U8zld36c21sgU"
# call node on the CLI entry directly, because gws.cmd routes arguments
# through cmd.exe, which mangles the quotes inside a JSON body
GWS = ["node", "D:/Atharva/Software/nodejs/npm/node_modules/@googleworkspace/cli/run.js"]
FONT = "Space Grotesk"


def rgb(h):
    return {"red": int(h[0:2], 16) / 255, "green": int(h[2:4], 16) / 255, "blue": int(h[4:6], 16) / 255}


NAVY, PRIMARY, INK, MUTE = rgb("11206D"), rgb("0046FF"), rgb("1B223B"), rgb("5A637D")
LAV, GREY_BG, WHITE = rgb("ECECFB"), rgb("EEF0F6"), rgb("FFFFFF")
GREEN_LT, GREEN_DK, PURPLE = rgb("E7F6EE"), rgb("0B7A42"), rgb("4D4DD9")
BORDER = rgb("C4CCDE")

EDGE_BG = {d.AK: GREEN_LT, d.NS: GREY_BG, d.PAR: LAV, d.NA: GREY_BG}
EDGE_FG = {d.AK: GREEN_DK, d.NS: NAVY, d.PAR: PURPLE, d.NA: MUTE}


def u16(s):
    return len(s.encode("utf-16-le")) // 2


class Rich:
    """Build a cell string plus its textFormatRuns."""

    def __init__(self):
        self.text = ""
        self.runs = []

    def add(self, s, **fmt):
        self.runs.append({"startIndex": u16(self.text), "format": fmt})
        self.text += s
        return self

    def link(self, url, label="[LINK]"):
        return self.add(label, link={"uri": url}, foregroundColor=PRIMARY, underline=True, bold=True)

    def links(self, keys):
        for i, k in enumerate(keys):
            if i:
                self.add(" ")
            self.link(d.SOURCES[k][2])
        return self

    def cell(self, bg=WHITE, size=10, wrap=True, valign="TOP", halign="LEFT", bold=False, color=INK):
        runs = [r for r in self.runs if r["startIndex"] < u16(self.text)]
        return {
            "userEnteredValue": {"stringValue": self.text},
            "textFormatRuns": runs,
            "userEnteredFormat": {
                "backgroundColor": bg,
                "wrapStrategy": "WRAP" if wrap else "OVERFLOW_CELL",
                "verticalAlignment": valign,
                "horizontalAlignment": halign,
                "padding": {"top": 6, "bottom": 6, "left": 6, "right": 6},
                "textFormat": {"fontFamily": FONT, "fontSize": size, "bold": bold, "foregroundColor": color},
                "borders": {s: {"style": "SOLID", "color": BORDER} for s in ("top", "bottom", "left", "right")},
            },
        }


def plain(s, **kw):
    return Rich().add(s).cell(**kw)


def blank(bg=WHITE):
    return {"userEnteredFormat": {"backgroundColor": bg}}


def header(values, size=11):
    return [Rich().add(v).cell(bg=NAVY, size=size, bold=True, color=WHITE, valign="MIDDLE") for v in values]


def rows_request(sheet_id, start_row, rows, per=3):
    """One updateCells per `per` rows, so no single request passes the
    32,767-character Windows command-line limit."""
    return [{"updateCells": {
        "start": {"sheetId": sheet_id, "rowIndex": start_row + i, "columnIndex": 0},
        "rows": [{"values": r} for r in rows[i:i + per]],
        "fields": "userEnteredValue,textFormatRuns,userEnteredFormat"}}
        for i in range(0, len(rows), per)]


def merge(sheet_id, r0, r1, c0, c1):
    return {"mergeCells": {"range": {"sheetId": sheet_id, "startRowIndex": r0, "endRowIndex": r1,
                                     "startColumnIndex": c0, "endColumnIndex": c1},
                           "mergeType": "MERGE_ALL"}}


def widths(sheet_id, px):
    return [{"updateDimensionProperties": {
        "range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
        "properties": {"pixelSize": w}, "fields": "pixelSize"}} for i, w in enumerate(px)]


def status_rich(status, text, keys):
    r = Rich()
    r.add(d.status_label(status) + "\n", bold=True, foregroundColor=GREEN_DK if status.startswith("GA") and "Roadmap" not in status else PURPLE if status != "Not documented" else MUTE)
    r.add(text + "\n")
    r.links(keys)
    return r


# ================================================================ requests
S_SUM, S_CMP, S_SRC, S_TMP = 101, 102, 103, 199


def gws_batch(reqs):
    body = json.dumps({"requests": reqs}, ensure_ascii=False)
    out = subprocess.run(
        GWS + ["sheets", "spreadsheets", "batchUpdate",
         "--params", json.dumps({"spreadsheetId": SHEET_ID}), "--json", body],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if '"error"' in out.stdout or out.returncode:
        print(out.stdout[-1500:], out.stderr[-1500:])
        raise SystemExit("batchUpdate failed")


def chunks(reqs, limit=12000):
    cur, size = [], 0
    for r in reqs:
        n = len(json.dumps(r, ensure_ascii=False))
        if cur and size + n > limit:
            yield cur
            cur, size = [], 0
        cur.append(r)
        size += n
    if cur:
        yield cur


def current_sheets():
    out = subprocess.run(GWS + ["sheets", "spreadsheets", "get", "--params",
                          json.dumps({"spreadsheetId": SHEET_ID, "fields": "sheets.properties(sheetId,title)"})],
                         capture_output=True, text=True, encoding="utf-8").stdout
    data = json.loads(out[out.index("{"):])
    return [s["properties"]["sheetId"] for s in data["sheets"]]


def reset_tabs():
    old = current_sheets()
    reqs = [{"addSheet": {"properties": {"sheetId": S_TMP, "title": "tmp-rebuild"}}}] if S_TMP not in old else []
    reqs += [{"deleteSheet": {"sheetId": sid}} for sid in old if sid != S_TMP]
    for sid, title, idx, frozen in ((S_SUM, "Summary", 0, 0), (S_CMP, "Comparison", 1, 1), (S_SRC, "Sources", 2, 1)):
        reqs.append({"addSheet": {"properties": {
            "sheetId": sid, "title": title, "index": idx,
            "gridProperties": {"rowCount": 120, "columnCount": 6, "frozenRowCount": frozen, "hideGridlines": True}}}})
    reqs.append({"deleteSheet": {"sheetId": S_TMP}})
    gws_batch(reqs)


def summary():
    sid = S_SUM
    reqs = widths(sid, [230, 120, 120, 100, 560])
    sc = d.score()
    rows, merges = [], []
    rows.append([Rich().add(f"{d.AK_NAME} vs {d.NS_NAME}").cell(size=16, bold=True, color=NAVY, wrap=False)] + [blank()] * 4)
    merges.append((0, 1, 0, 5))
    rows.append([Rich().add(f"16 capabilities in 6 categories. Every cell links to the vendor's own page. Sources read on {d.READ_ON}.")
                 .cell(size=10, color=MUTE, wrap=False)] + [blank()] * 4)
    merges.append((1, 2, 0, 5))
    rows.append([blank()] * 5)
    rows.append(header(["Category", d.TICK + " AccuKnox", d.TICK + " Netskope", "⚖️ Parity", "Capabilities in the category"]))
    for cid, cname in d.CATEGORIES:
        cr = [x for x in d.ROWS if x["cat"] == cid]
        rows.append([
            plain(f"{cid}. {cname}", bold=True, color=NAVY, valign="MIDDLE"),
            plain(str(sum(x["edge"] == d.AK for x in cr)), halign="CENTER", valign="MIDDLE", bold=True, color=GREEN_DK),
            plain(str(sum(x["edge"] == d.NS for x in cr)), halign="CENTER", valign="MIDDLE", bold=True, color=NAVY),
            plain(str(sum(x["edge"] == d.PAR for x in cr)), halign="CENTER", valign="MIDDLE", bold=True, color=PURPLE),
            plain(", ".join(f"{x['id']} {x['capability']}" for x in cr), valign="MIDDLE"),
        ])
    rows.append([
        plain("Total", bold=True, color=WHITE, bg=PRIMARY, valign="MIDDLE"),
        plain(str(sc[d.AK]), bold=True, color=WHITE, bg=PRIMARY, halign="CENTER", valign="MIDDLE"),
        plain(str(sc[d.NS]), bold=True, color=WHITE, bg=PRIMARY, halign="CENTER", valign="MIDDLE"),
        plain(str(sc[d.PAR]), bold=True, color=WHITE, bg=PRIMARY, halign="CENTER", valign="MIDDLE"),
        plain(d.PART + " F2 Licensing is not scored until AccuKnox confirms its licensing unit.", bg=LAV, valign="MIDDLE"),
    ])
    rows.append([blank()] * 5)

    def block(title, items):
        r0 = len(rows)
        rows.append(header([title, "", "", "", "Fact and source"]))
        merges.append((r0, r0 + 1, 0, 4))
        for head, rich in items:
            r = len(rows)
            rows.append([plain(head, bold=True, color=NAVY, valign="MIDDLE"), blank(), blank(), blank(), rich.cell()])
            merges.append((r, r + 1, 0, 4))
        rows.append([blank()] * 5)

    block("Why AccuKnox", [(h, Rich().add(t + " ").links(k)) for h, t, k in d.BETTER_FASTER_CHEAPER])
    block("Where Netskope leads", [(h, Rich().add(t + " ").link(d.SOURCES[k][2])) for h, t, k in d.NETSKOPE_LEADS])
    block("Legend", [(i, Rich().add(t)) for i, t in d.LEGEND]
          + [("⚖️", Rich().add("Parity. Both vendors ship the capability."))])

    reqs += rows_request(sid, 0, rows)
    reqs += [merge(sid, *m) for m in merges]
    return reqs


def comparison():
    sid = S_CMP
    reqs = widths(sid, [44, 170, 430, 430, 210])
    rows, merges = [header(["ID", "Capability", "AccuKnox", "Netskope", "Edge"])], []
    for cid, cname in d.CATEGORIES:
        r = len(rows)
        rows.append([Rich().add(f"{cid}.  {cname}").cell(bg=LAV, size=11, bold=True, color=PRIMARY, wrap=False, valign="MIDDLE")]
                    + [blank(LAV)] * 4)
        merges.append((r, r + 1, 0, 5))
        for x in [x for x in d.ROWS if x["cat"] == cid]:
            edge = Rich().add(d.EDGE_LABEL[x["edge"]] + "\n", bold=True, foregroundColor=EDGE_FG[x["edge"]]).add(x["why"])
            rows.append([
                plain(x["id"], bold=True, color=PRIMARY, halign="CENTER"),
                plain(x["capability"], bold=True, color=NAVY),
                status_rich(x["ak_status"], x["ak"], x["ak_src"]).cell(),
                status_rich(x["ns_status"], x["ns"], x["ns_src"]).cell(),
                edge.cell(bg=EDGE_BG[x["edge"]]),
            ])
    reqs += rows_request(sid, 0, rows)
    reqs += [merge(sid, *m) for m in merges]
    reqs.append({"setBasicFilter": {"filter": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": len(rows),
                                                          "startColumnIndex": 0, "endColumnIndex": 5}}}})
    return reqs


def sources():
    sid = S_SRC
    reqs = widths(sid, [100, 300, 80, 150])
    used = {}
    for x in d.ROWS:
        for k in x["ak_src"] + x["ns_src"]:
            used.setdefault(k, []).append(x["id"])
    rows = [header(["Vendor", "Page", "Link", "Used in rows"])]
    for k, (v, title, url) in d.SOURCES.items():
        rows.append([
            plain(v, bold=True, color=NAVY if v == "AccuKnox" else MUTE),
            plain(title),
            Rich().link(url).cell(halign="CENTER"),
            plain(", ".join(used.get(k, [])) or "Summary"),
        ])
    reqs += rows_request(sid, 0, rows)
    return reqs


if __name__ == "__main__":
    reset_tabs()
    allreqs = summary() + comparison() + sources()
    for part in chunks(allreqs):
        gws_batch(part)
    print("sheet updated:", f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")
