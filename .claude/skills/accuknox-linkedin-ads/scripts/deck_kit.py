"""AccuKnox slide primitives for python-pptx, with entrance animations that
survive the Google Slides import.

Brand values come from the ak-pptx skill: navy 0000C8 header and footer bars,
Space Grotesk headings, Inter body, 10 x 5.625 inch canvas.

Animations: Google Slides keeps "fade in" and "fly in" on import, and keeps the
slide fade transition. Every animation here starts with the slide, one item
after another, so a presenter never has to click to reveal a shape. Verified on
2026-10-01 by an import, export and XML round trip.
"""
import re
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"

NAVY = "0000C8"
BLUE = "0046FF"
PURPLE = "6464FF"
RED = "C80019"
WHITE = "FFFFFF"
OFF = "F2F4FA"
LIGHT = "D6E4F7"
LIGHT_RED = "FFF0F2"
SOFT = "EEF3FF"
INK = "0D1B4B"
MID = "44507A"
DEEP = "05082A"
GREEN = "0A7D4F"
AMBER = "B26A00"

HEAD = "Space Grotesk"
BODY = "Space Grotesk"
W, H = 10.0, 5.625
SIDE = 0.45


def rgb(hex_):
    return RGBColor.from_string(hex_)


def new_deck():
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    return prs


def blank(prs, bg=WHITE):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(bg)
    s._anim = []
    return s


# ---------------------------------------------------------------- text


def _apply_runs(par, text, size, color, font, bold, italic=False):
    """Write text into a paragraph. **double stars** mark a bold run.
    A [bracketed] gap renders bold amber on light backgrounds, so nobody launches with one open."""
    parts = re.split(r"(\*\*[^*]+\*\*|\[[^\]]+\])", text)
    light_bg = color in (INK, MID)
    for part in parts:
        if not part:
            continue
        r = par.add_run()
        is_b = part.startswith("**") and part.endswith("**")
        is_slot = part.startswith("[") and part.endswith("]")
        r.text = part[2:-2] if is_b else part
        f = r.font
        f.size = Pt(size)
        f.name = font
        f.bold = bold or is_b or (is_slot and light_bg)
        f.italic = italic
        f.color.rgb = rgb(AMBER if (is_slot and light_bg) else color)


def text(s, x, y, w, h, content, size=12, color=INK, font=BODY, bold=False,
         align="l", anchor="t", italic=False, spacing=None, bullets=False, after=4):
    """Add a text box. content is a string or a list of paragraphs."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.02)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    paras = content if isinstance(content, list) else [content]
    for i, ptxt in enumerate(paras):
        par = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        par.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
        par.space_after = Pt(after)
        if spacing:
            par.line_spacing = spacing
        if bullets:
            ptxt = "•  " + ptxt
        _apply_runs(par, ptxt, size, color, font, bold, italic)
    return tb


def shape(s, kind, x, y, w, h, fill=None, line=None, lw=0.75, radius=None):
    k = {"rect": MSO_SHAPE.RECTANGLE, "round": MSO_SHAPE.ROUNDED_RECTANGLE,
         "oval": MSO_SHAPE.OVAL, "chevron": MSO_SHAPE.CHEVRON, "pent": MSO_SHAPE.PENTAGON,
         "arrow": MSO_SHAPE.RIGHT_ARROW, "trap": MSO_SHAPE.TRAPEZOID,
         "diamond": MSO_SHAPE.DIAMOND, "down": MSO_SHAPE.DOWN_ARROW}[kind]
    sh = s.shapes.add_shape(k, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill:
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
    else:
        sh.fill.background()
    if line:
        sh.line.color.rgb = rgb(line)
        sh.line.width = Pt(lw)
    else:
        sh.line.fill.background()
    if radius is not None and kind == "round":
        sh.adjustments[0] = radius
    sh.shadow.inherit = False
    return sh


def label(sh, content, size=12, color=WHITE, font=BODY, bold=False, align="c", anchor="m", pad=0.08):
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(pad)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    paras = content if isinstance(content, list) else [content]
    for i, ptxt in enumerate(paras):
        par = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        par.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
        par.space_after = Pt(2)
        _apply_runs(par, ptxt, size, color, font, bold)
    return sh


def line(s, x1, y1, x2, y2, color=MID, width=1.25, arrow=False, dash=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(width)
    ln = c.line._get_or_add_ln()
    if dash:
        etree.SubElement(ln, "{http://schemas.openxmlformats.org/drawingml/2006/main}prstDash").set("val", "dash")
    if arrow:
        t = etree.SubElement(ln, "{http://schemas.openxmlformats.org/drawingml/2006/main}tailEnd")
        t.set("type", "triangle")
        t.set("w", "med")
        t.set("h", "med")
    return c


def picture(s, path, x, y, w=None, h=None):
    path = str(path)
    kw = {}
    if w:
        kw["width"] = Inches(w)
    if h:
        kw["height"] = Inches(h)
    return s.shapes.add_picture(path, Inches(x), Inches(y), **kw)


def notes(s, content):
    s.notes_slide.notes_text_frame.text = content


# ---------------------------------------------------------------- chrome


def header(s, title, logo=None, kicker=None):
    shape(s, "rect", 0, 0, W, 0.62, fill=NAVY)
    size = 19 if len(title) <= 52 else max(14, int(19 * 52 / len(title)))
    text(s, SIDE, 0.0, 7.9, 0.62, title, size=size, color=WHITE, font=HEAD, bold=True, anchor="m")
    if logo:
        picture(s, logo, W - SIDE - 1.25, 0.18, w=1.25)
    if kicker:
        text(s, SIDE, 0.7, 9.1, 0.3, kicker, size=10, color=BLUE, bold=True)


def footer(s, n, label_="AccuKnox  |  Paid Ads Playbook  |  Internal"):
    shape(s, "rect", 0, H - 0.28, W, 0.28, fill=NAVY)
    text(s, SIDE, H - 0.28, 7.5, 0.28, label_, size=8, color=WHITE, anchor="m")
    text(s, W - SIDE - 1, H - 0.28, 1, 0.28, str(n), size=8, color=WHITE, anchor="m", align="r")


def card(s, x, y, w, h, title, body, accent=BLUE, fill=WHITE, tsize=12.5, bsize=10, title_color=INK):
    box = shape(s, "rect", x, y, w, h, fill=fill, line="D5DBEE")
    shape(s, "rect", x, y, w, 0.06, fill=accent)
    text(s, x + 0.14, y + 0.14, w - 0.28, 0.4, title, size=tsize, color=title_color, font=HEAD, bold=True)
    by = 0.52 if len(title) * tsize < w * 105 else 0.72
    tb = text(s, x + 0.14, y + by, w - 0.28, h - by - 0.08, body, size=bsize, color=INK, after=3)
    return box, tb


def stat(s, x, y, w, h, number, unit, caption, fill=NAVY, ncolor=WHITE, ucolor="B9C2FF"):
    box = shape(s, "rect", x, y, w, h, fill=fill)
    shape(s, "rect", x, y, w, 0.06, fill=RED)
    nsize = 36 if len(number) <= 7 else int(36 * 7 / len(number))
    text(s, x, y + 0.2, w, 0.75, number, size=nsize, color=ncolor, font=HEAD, bold=True, align="c")
    text(s, x + 0.1, y + 0.95, w - 0.2, 0.3, unit, size=10.5, color=ucolor, bold=True, align="c")
    text(s, x + 0.15, y + 1.25, w - 0.3, h - 1.3, caption, size=9, color=WHITE, align="c")
    return box


def table(s, x, y, w, rows, col_w, size=9, head_fill=NAVY, row_h=0.3, zebra=True, bold_first_col=False):
    nr, nc = len(rows), len(rows[0])
    gt = s.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(w), Inches(row_h * nr))
    t = gt.table
    for j, cw in enumerate(col_w):
        t.columns[j].width = Inches(cw)
    for i, r in enumerate(rows):
        t.rows[i].height = Inches(row_h)
        for j, val in enumerate(r):
            cell = t.cell(i, j)
            cell.margin_left = cell.margin_right = Inches(0.06)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame
            tf.word_wrap = True
            par = tf.paragraphs[0]
            head = i == 0
            _apply_runs(par, str(val), size, WHITE if head else INK, BODY,
                        head or (bold_first_col and j == 0))
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(head_fill if head else (OFF if zebra and i % 2 == 0 else WHITE))
    return gt


# ---------------------------------------------------------------- motion


def anim(s, *shapes, effect="fade", step=250, start=150):
    """Queue shapes to animate in, in order, when the slide opens."""
    for sh in shapes:
        s._anim.append((sh, effect))
    s._anim_cfg = (step, start)


def _effect_xml(spid, effect, delay):
    """One entrance effect, shaped like the XML PowerPoint itself writes. Node ids are
    the literal {ID}, numbered in document order by finalize()."""
    set_vis = (f'<p:set><p:cBhvr><p:cTn id="{{ID}}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/>'
               f'</p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst>'
               f'<p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>')
    if effect == "fade":
        preset, sub = 10, 0
        body = (f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{{ID}}" dur="500"/>'
                f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>')
    else:
        preset = 2
        sub, ax, frm = {"fly_up": (4, "ppt_y", "1+#ppt_h/2"), "fly_left": (8, "ppt_x", "0-#ppt_w/2"),
                        "fly_right": (2, "ppt_x", "1+#ppt_w/2")}[effect]
        other = "ppt_x" if ax == "ppt_y" else "ppt_y"
        body = ""
        for attr, f0, f1 in ((other, f"#{other}", f"#{other}"), (ax, frm, f"#{ax}")):
            body += (f'<p:anim calcmode="lin" valueType="num"><p:cBhvr additive="base"><p:cTn id="{{ID}}" dur="500" fill="hold"/>'
                     f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>{attr}</p:attrName></p:attrNameLst></p:cBhvr>'
                     f'<p:tavLst><p:tav tm="0"><p:val><p:strVal val="{f0}"/></p:val></p:tav><p:tav tm="100000"><p:val>'
                     f'<p:strVal val="{f1}"/></p:val></p:tav></p:tavLst></p:anim>')
    return (f'<p:par><p:cTn id="{{ID}}" fill="hold"><p:stCondLst><p:cond delay="{delay}"/></p:stCondLst><p:childTnLst>'
            f'<p:par><p:cTn id="{{ID}}" presetID="{preset}" presetClass="entr" presetSubtype="{sub}" fill="hold" grpId="0" nodeType="withEffect">'
            f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{set_vis}{body}</p:childTnLst></p:cTn></p:par>'
            f'</p:childTnLst></p:cTn></p:par>')


def finalize(prs):
    """Write the fade transition and the entrance timing onto every slide.
    Effects start with the slide, one after another, so nobody has to click."""
    for s in prs.slides:
        el = s._element
        tr = etree.SubElement(el, f"{{{P_NS}}}transition")
        tr.set("spd", "med")
        etree.SubElement(tr, f"{{{P_NS}}}fade")
        items = getattr(s, "_anim", [])
        if not items:
            continue
        step, start = getattr(s, "_anim_cfg", (250, 150))
        seen, effects, bld = set(), [], []
        for i, (sh, eff) in enumerate(items):
            if sh.shape_id in seen:
                continue
            seen.add(sh.shape_id)
            effects.append(_effect_xml(sh.shape_id, eff, start + len(effects) * step))
            if sh._element.tag.endswith("}sp") and sh.has_text_frame:
                bld.append(f'<p:bldP spid="{sh.shape_id}" grpId="0" animBg="1"/>')
        xml = (f'<p:timing xmlns:p="{P_NS}"><p:tnLst><p:par><p:cTn id="{{ID}}" dur="indefinite" restart="never" nodeType="tmRoot">'
               f'<p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="{{ID}}" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
               f'<p:par><p:cTn id="{{ID}}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/><p:cond evt="onBegin" delay="0">'
               f'<p:tn val="2"/></p:cond></p:stCondLst><p:childTnLst>{"".join(effects)}</p:childTnLst></p:cTn></p:par>'
               f'</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
               f'<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
               f'</p:childTnLst></p:cTn></p:par></p:tnLst>'
               + (f'<p:bldLst>{"".join(bld)}</p:bldLst>' if bld else "") + '</p:timing>')
        n = iter(range(1, 100000))
        xml = re.sub(r"\{ID\}", lambda m: str(next(n)), xml)
        el.append(etree.fromstring(xml))
    return prs


# ---------------------------------------------------------------- AccuKnox master template
# assets/ppt-template.pptx is a copy of "PPT Template.pptx" from the doc-ppt-template
# repo. Its rules: layout 0 is the front cover and layout 1 the back cover, both with
# finished artwork where only the words change. Layout 4 is every content slide.
TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "ppt-template.pptx"
TNAVY = "11206D"
NAVY_TXT = "B8C4E8"


def from_template(path=TEMPLATE):
    """Open the master template and drop its example slides, keeping the layouts."""
    prs = Presentation(str(path))
    sld_ids = prs.slides._sldIdLst
    for sid in list(sld_ids):
        prs.part.drop_rel(sid.rId)
        sld_ids.remove(sid)
    return prs


def _ph(slide, idx):
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            return ph
    return None


def _drop_ph(slide, idx):
    ph = _ph(slide, idx)
    if ph is not None:
        ph._element.getparent().remove(ph._element)


def _fill_ph(ph, content, size, color, bold, align="c", top=None, height=None):
    if top is not None:
        left, width = ph.left, ph.width
        ph.left, ph.width, ph.top, ph.height = left, width, Inches(top), Inches(height)
    tf = ph.text_frame
    tf.word_wrap = True
    tf.clear()
    par = tf.paragraphs[0]
    par.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER}[align]
    _apply_runs(par, content, size, color, HEAD, bold)
    return ph


def _clean(slide):
    for idx in (10, 11, 12):
        _drop_ph(slide, idx)


def cover(prs, title, scope=None):
    """Front cover on layout 0. Title plus an optional row of (number, label) pairs."""
    s = prs.slides.add_slide(prs.slide_layouts[0])
    s._anim = []
    _clean(s)
    ph = _ph(s, 0)
    _fill_ph(ph, title, 26, WHITE, True, top=1.86, height=1.1)
    _drop_ph(s, 1)
    if scope:
        x0, w0 = ph.left / 914400, ph.width / 914400
        cw = w0 / len(scope)
        for i, (num, lab) in enumerate(scope):
            a = text(s, x0 + i * cw, 3.0, cw, 0.4, num, size=18, color=WHITE, font=HEAD, bold=True, align="c")
            b = text(s, x0 + i * cw, 3.4, cw, 0.3, lab, size=9, color=NAVY_TXT, font=HEAD, align="c")
            anim(s, a, b, effect="fade", step=150)
    return s


def closing(prs, headline="SEE US IN ACTION", contact="support@accuknox.com"):
    """Back cover on layout 1. Change the words, nothing else."""
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s._anim = []
    _clean(s)
    _fill_ph(_ph(s, 0), headline, 22, WHITE, True, top=2.02, height=0.62)
    if contact:
        _fill_ph(_ph(s, 1), contact, 13, NAVY_TXT, False, top=2.66, height=0.44)
    else:
        _drop_ph(s, 1)
    return s


def content(prs, title):
    """A content slide on layout 4: the template's navy title band, white body."""
    s = prs.slides.add_slide(prs.slide_layouts[4])
    s._anim = []
    _clean(s)
    size = 22 if len(title) <= 42 else max(16, int(22 * 42 / len(title)))
    ph = _ph(s, 0)
    tf = ph.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(0.4)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    _apply_runs(tf.paragraphs[0], title, size, WHITE, HEAD, True)
    return s


def link(shape, target_slide):
    """Make a shape jump to another slide when clicked."""
    shape.click_action.target_slide = target_slide
