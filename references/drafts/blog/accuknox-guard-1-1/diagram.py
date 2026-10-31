"""How AccuKnox Guard 1.1 turns an input into a block decision, per its model card.

Source: huggingface.co/Accuknoxtechnologies/accuknox-guard-1.1 (README, Usage). The firewall layers in the
bottom band come from the diagram in the published technical post.
Run: python diagram.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONTS = Path(r"D:\AccuKnox\help\.claude\skills\accuknox-gated-content\assets\fonts")
OUT = Path(__file__).parent / "assets" / "diagram-decision-model.png"
NAVY, ACCENT, INK, MUTED, LINE = "#11206D", "#003BF6", "#0D1B4B", "#595959", "#D5D9E4"
S = 2
W, H = 1200 * S, 760 * S


def F(w, s):
    return ImageFont.truetype(str(FONTS / f"Inter-{w}.ttf"), s * S)


im = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(im)


def box(x, y, w, h, title, body, hi=False):
    d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + h) * S], radius=14 * S,
                        fill="#EEF2FF" if hi else "#F7F8FB", outline=ACCENT if hi else LINE, width=(3 if hi else 2) * S)
    d.text(((x + w / 2) * S, (y + 22) * S), title, font=F("Bold", 19), fill=NAVY if hi else INK, anchor="mt")
    yy = y + 54
    for ln in body:
        d.text(((x + w / 2) * S, yy * S), ln, font=F("Regular", 15), fill=MUTED, anchor="mt")
        yy += 22


def arrow(x1, y1, x2, y2, label=None):
    d.line([x1 * S, y1 * S, x2 * S, y2 * S], fill="#8A8F9E", width=3 * S)
    d.polygon([(x2 * S, y2 * S), ((x2 - 10) * S, (y2 - 7) * S), ((x2 - 10) * S, (y2 + 7) * S)], fill="#8A8F9E")
    if label:
        d.text((((x1 + x2) / 2) * S, (y1 - 12) * S), label, font=F("Medium", 13), fill=MUTED, anchor="mb")


d.text((48 * S, 36 * S), "One forward pass returns a probability. You decide where to block.",
       font=F("Bold", 26), fill=INK)
d.text((48 * S, 76 * S), "AccuKnox Guard 1.1 answers a fixed yes or no question about the input. It does not generate a verdict as text.",
       font=F("Regular", 16), fill=MUTED)

box(48, 130, 250, 170, "Input", ["A user prompt, a document,", "an email or a tool output,", "or a prompt and response pair"])
box(360, 130, 310, 170, "Decision model, 4.54B", ["Fine-tuned from d3-mini", "(Qwen3.5-4B base, LoRA)", "Reads input plus typed question", "No text generation"], hi=True)
box(732, 130, 190, 170, "P(block)", ["A probability", "from 0 to 1", "for example 0.93"])
box(984, 130, 170, 170, "Threshold", ["0.5 by default", "Tune per app", "Allow or block"])
arrow(298, 215, 356, 215)
arrow(670, 215, 728, 215)
arrow(922, 215, 980, 215)

d.rounded_rectangle([48 * S, 340 * S, 1152 * S, 470 * S], radius=14 * S, fill="#FBFBFD", outline=LINE, width=2 * S)
d.text((70 * S, 360 * S), "The typed question goes in with every input. It is the one the model was trained on.", font=F("SemiBold", 16), fill=INK)
q = ["Should this input be blocked before it reaches an AI agent? It may be a harmful request,",
     "a jailbreak attempt, or a prompt injection hidden inside a document or tool response.",
     "true: must be blocked        false: benign, safe to pass, even if it uses alarming words"]
for i, ln in enumerate(q):
    d.text((70 * S, (392 + i * 24) * S), ln, font=F("Regular", 15), fill=NAVY if i < 2 else MUTED)

d.line([515 * S, 340 * S, 515 * S, 310 * S], fill="#8A8F9E", width=3 * S)
d.polygon([(515 * S, 304 * S), (508 * S, 316 * S), (522 * S, 316 * S)], fill="#8A8F9E")
d.rounded_rectangle([48 * S, 524 * S, 1152 * S, 700 * S], radius=14 * S, fill="#F3F4F8", outline=LINE, width=2 * S)
d.text((70 * S, 544 * S), "Guard 1.1 feeds the AccuKnox Prompt Firewall, which sits inline in the request path", font=F("SemiBold", 17), fill=INK)
for i, t in enumerate(["Static rules", "Semantic checks", "Multi-turn intent", "LLM judge"]):
    x = 70 + i * 268
    d.rounded_rectangle([x * S, 590 * S, (x + 246) * S, 660 * S], radius=10 * S, fill="white", outline=LINE, width=2 * S)
    d.text(((x + 123) * S, 614 * S), t, font=F("Medium", 17), fill=INK, anchor="mt")
d.text((48 * S, 724 * S), "Sources: AccuKnox Guard 1.1 model card on Hugging Face, and the AccuKnox Prompt Firewall architecture.",
       font=F("Regular", 13), fill="#8A8F9E")
im.save(OUT)
print("wrote", OUT.name)
