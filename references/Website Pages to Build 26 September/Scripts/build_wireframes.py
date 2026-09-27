"""Inline wf.css and the tab script into each wireframe source."""
import pathlib, re, base64, io
from PIL import Image
REPO = pathlib.Path(__file__).resolve().parents[3]

HERE = pathlib.Path(__file__).parent
CSS = (HERE / "wf.css").read_text(encoding="utf-8")
JS = """
document.getElementById('notes').addEventListener('change', e => document.body.classList.toggle('hide-notes', !e.target.checked));
document.querySelectorAll('[data-tabs]').forEach(root => {
  const tabs = [...root.querySelectorAll('[role=tab]')];
  const pick = t => {
    tabs.forEach(x => { const on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1;
      document.getElementById(x.getAttribute('aria-controls')).hidden = !on; });
    t.focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => pick(t));
    t.addEventListener('keydown', e => {
      if (e.key === 'ArrowRight') pick(tabs[(i + 1) % tabs.length]);
      if (e.key === 'ArrowLeft') pick(tabs[(i - 1 + tabs.length) % tabs.length]);
    });
  });
});
"""
def embed(m):
    path, alt, cap = m.group(1).split("|")
    im = Image.open(REPO / path).convert("RGB")
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "WEBP", quality=82, method=6)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return (f'<figure class="shot"><img src="data:image/webp;base64,{b64}" alt="{alt}">'
            f'<figcaption>{cap}</figcaption></figure>')


for src, out in [("shadow", "new-page-shadow-ai-discovery.html"), ("dspm", "new-page-dspm-indian-banks.html")]:
    t = re.sub(r"<!--IMG:(.*?)-->", embed, (HERE / "src" / f"{src}.src.html").read_text(encoding="utf-8"))
    (HERE.parent / "Prototype HTMLs" / out).write_text(t.replace("/*CSS*/", CSS).replace("/*JS*/", JS), encoding="utf-8")
    print(out)
