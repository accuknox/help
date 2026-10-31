import json, re, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
SK = sys.argv[1]; DOC = "un/word/document.xml"
C = json.load(open("comments.json", encoding="utf8"))
AN = {"human approval for agent actions": "Agent controls are still maturing"}
def text_of(p): return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)).replace("&amp;", "&").replace("&apos;", "'")
for k, txt in C.items():
    anchor = AN.get(k, k)
    out = subprocess.run([sys.executable, SK + "/scripts/comment.py", "un/", txt, "--author", "Atharva Shah (AccuKnox)", "--initials", "AS"], capture_output=True, text=True, encoding="utf8")
    cid = re.findall(r'w:id="(\d+)"', out.stdout)[0]
    x = open(DOC, encoding="utf8").read()
    for m in re.finditer(r"<w:p[ >].*?</w:p>", x, flags=re.S):
        if anchor in text_of(m.group(0)): break
    else: raise SystemExit("nf " + anchor)
    p = m.group(0); pe = p.find("</w:pPr>") + len("</w:pPr>")
    p2 = p[:pe] + f'<w:commentRangeStart w:id="{cid}"/>' + p[pe:-6] + f'<w:commentRangeEnd w:id="{cid}"/><w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="{cid}"/></w:r></w:p>'
    open(DOC, "w", encoding="utf8").write(x[:m.start()] + p2 + x[m.end():]); print("comment", cid, anchor)
