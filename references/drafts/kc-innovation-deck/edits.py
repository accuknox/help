# Tracked changes and comments for the AccuKnox profile in the KuppingerCole draft.
import re, sys, json
sys.stdout.reconfigure(encoding="utf-8")
AUTH = "Atharva Shah (AccuKnox)"
DATE = "2026-10-26T12:00:00Z"
DOC = "un/word/document.xml"

INS = [  # (paragraph anchor text, insert after this exact text, new text)
    ("founded in August 2020", "is a private company backed by venture capital.",
     " AccuKnox holds US patents on kernel-level security enforcement. The most recent, US Patent 12,730,882 B2, was granted on September 8, 2026. It tracks unknown processes in the kernel and blocks them only when they try to reach sensitive assets."),
    ("The firewall is stateful", "so it catches attacks that escalate gradually over several messages.",
     " An independent review of AI firewall architectures by analyst Andrew Green found it to be the only explicitly stateful AI firewall among the six vendors compared."),
    ("AccuKnox uses supervised", "topic classification, and perplexity scoring.",
     " The guardrail model behind these verdicts, AccuKnox Guard 1.1, ranked first of 41 open guardrail models on the independent GuardRate leaderboard on Hugging Face (October 16, 2026 snapshot). It scored 0.808, with a 13.7% false-positive rate and 72.3 ms p95 latency at 4.5 billion parameters."),
    ("references include Airbus", "which runs 18 AI teams under an AI center of excellence.",
     " Further references include a US Department of War research organization, which selected AccuKnox after a 12-month proof of concept of eight vendors. A global airline protects more than 40 AI agents across AWS Bedrock, Azure AI Foundry, and Copilot Studio. A leading Asian stock exchange runs an on-premises proof of concept."),
]
REPL = [  # (paragraph anchor, old text, new text)
    ("human approval for agent actions", "or human approval for agent actions",
     "or human approval for actions of third-party agents, although human approval is the default in AccuKnox's own AgentZ platform"),
]
NEW_BULLET = ("Stateful Prompt Firewall that tracks risk across conversation turns",
              "Guardrail model ranked first of 41 on the independent GuardRate leaderboard")

COMMENTS = {  # paragraph anchor -> comment text
    "founded in August 2020": "Factual addition. US Patent 12,730,882 B2, \"System and method for tainting suspicious process and applying targeted rules thereof\". Inventors Rahul Arvind Jadhav and Barun Acharya. Filed December 8, 2023, granted September 8, 2026, 18 claims. Claim 1 covers kernel-level telemetry, in-kernel tracking of unknown processes, an in-kernel taint flag when a process reaches for a sensitive asset, and blocking with automatic risk escalation. This mechanism sits under the ModelArmor agent sandbox described in the runtime control paragraph. Evidence: USPTO grant certificate, attached.",
    "The firewall is stateful": "Factual addition. Source: Andrew Green, \"AI Firewall Architectures, Intent Analysis, and You\", July 2026, https://accuknox.com/wp-content/uploads/AI-Firewall-Architectures-Intent-Analysis-and-You.pdf. The paper compares AccuKnox, Check Point (Lakera), Cloudflare, F5 (CalypsoAI), HiddenLayer and Palo Alto Networks (Prisma AIRS). It lists AccuKnox as the only stateful design. As the paper states, AccuKnox supplied its own architecture details. The session state is an in-memory key-value and vector store keyed by session, agent and user. It holds a rolling summary, an embedding trajectory, a tool-call ledger and a cumulative risk score.",
    "AccuKnox uses supervised": "Factual addition. Source: HiveTrace GuardRate leaderboard, https://hivetrace-guardrateleaderboard.hf.space/, snapshot October 16, 2026: 41 models, 19 benchmark groups, 44 datasets, 5 languages. HiveTrace ran the AccuKnox evaluation itself and posted it at https://huggingface.co/spaces/hivetrace/GuardRateLeaderboard/discussions/1. The runner-up scored 0.764 with a 21.8% false-positive rate. For balance, Guard 1.1 scores 0.706 on the GuardRate prompt-injection group against 0.905 for the runner-up. The model powers the Prompt Firewall and AI Guardrails.",
    "references include Airbus": "Factual addition, all three anonymized under customer agreements. US Department of War research organization: on-premises, air-gapped AI security across classified networks, with KubeArmor runtime enforcement, the Prompt Firewall and a sandbox per model. Global airline: public case study at https://accuknox.com/case-studies/aviation, with 1,500+ models inventoried, runtime security risk down 90% and data leakage risk down 85%. Asian stock exchange: 36 test cases across browser, endpoint, agent and API surfaces, fully on premises. Summaries attached.",
    "human approval for agent actions": "Clarification for consistency with the AI and automation paragraph of this profile. That paragraph states that in AgentZ, mutating actions are denied by default and human approval is the default setting. The gap applies to third-party agent platforms only.",
    "Challenger in the Innovation, Market": "We ask the analyst to review the Innovation rating against the facts added above. The Innovation Leadership section lists six innovative features. Per this profile, two are generally available in AccuKnox: behavioral analysis of AI agents (ModelArmor learned baselines, goal hijacking detection) and continuous red teaming that reruns after every model change. Three are partly available: human approval (default in AgentZ), natural-language investigation through AskADA, and blocking of abusive request patterns. The new facts are the GuardRate first place, the independent finding that the Prompt Firewall is the only stateful design of six reviewed, and the September 2026 patent.",
}

def W(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def text_of(p):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))

def find_para(x, anchor):
    for m in re.finditer(r"<w:p[ >].*?</w:p>", x, flags=re.S):
        if anchor in text_of(m.group(0)).replace("&amp;", "&").replace("&apos;", "'"):
            return m
    raise SystemExit("anchor not found: " + anchor)

rid = [9000]
def nid():
    rid[0] += 1; return rid[0]

def run_rpr(p, pos):
    # rPr of the run that contains position pos
    start = p.rfind("<w:r>", 0, pos); s2 = p.rfind("<w:r ", 0, pos); start = max(start, s2)
    seg = p[start:pos]
    m = re.search(r"<w:rPr>.*?</w:rPr>", seg, flags=re.S)
    return m.group(0) if m else ""

def ins_run(rpr, t):
    return f'<w:ins w:id="{nid()}" w:author="{AUTH}" w:date="{DATE}"><w:r>{rpr}<w:t xml:space="preserve">{W(t)}</w:t></w:r></w:ins>'

def del_run(rpr, t):
    return f'<w:del w:id="{nid()}" w:author="{AUTH}" w:date="{DATE}"><w:r>{rpr}<w:delText xml:space="preserve">{W(t)}</w:delText></w:r></w:del>'

def split_at(p, needle):
    # returns (index inside a w:t where needle sits, the w:t open tag, rpr)
    for m in re.finditer(r"(<w:t[^>]*>)([^<]*)</w:t>", p):
        k = m.group(2).find(W(needle))
        if k >= 0:
            return m, k
    raise SystemExit("needle not found: " + needle)

x = open(DOC, encoding="utf8").read()

for anchor, after, new in INS:
    m = find_para(x, anchor); p = m.group(0)
    tm, k = split_at(p, after)
    cut = tm.start(2) + k + len(W(after))
    rpr = run_rpr(p, tm.start())
    p = p[:tm.start(1)] + '<w:t xml:space="preserve">' + p[tm.end(1):]; cut += len('<w:t xml:space="preserve">') - len(tm.group(1))
    p2 = p[:cut] + f'</w:t></w:r>{ins_run(rpr, new)}<w:r>{rpr}<w:t xml:space="preserve">' + p[cut:]
    x = x[:m.start()] + p2 + x[m.end():]

for anchor, old, new in REPL:
    m = find_para(x, anchor); p = m.group(0)
    tm, k = split_at(p, old)
    a = tm.start(2) + k; b = a + len(W(old))
    rpr = run_rpr(p, tm.start())
    sh = len('<w:t xml:space="preserve">') - len(tm.group(1)); p = p[:tm.start(1)] + '<w:t xml:space="preserve">' + p[tm.end(1):]; a += sh; b += sh
    p2 = p[:a] + f'</w:t></w:r>{del_run(rpr, old)}{ins_run(rpr, new)}<w:r>{rpr}<w:t xml:space="preserve">' + p[b:]
    x = x[:m.start()] + p2 + x[m.end():]

# new bullet after the stateful Prompt Firewall strength, inserted paragraph mark
m = find_para(x, NEW_BULLET[0]); p = m.group(0)
ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, flags=re.S).group(0)
mark = f'<w:ins w:id="{nid()}" w:author="{AUTH}" w:date="{DATE}"/>'
if "<w:rPr>" in ppr:
    ppr2 = ppr.replace("<w:rPr>", "<w:rPr>" + mark, 1)
else:
    ppr2 = ppr.replace("</w:pPr>", f"<w:rPr>{mark}</w:rPr></w:pPr>")
rpr = run_rpr(p, len(p) - 10)
newp = f"<w:p>{ppr2}{ins_run(rpr, NEW_BULLET[1])}</w:p>"
x = x[:m.end()] + newp + x[m.end():]

open(DOC, "w", encoding="utf8").write(x)
json.dump(COMMENTS, open("comments.json", "w", encoding="utf8"), ensure_ascii=False)
open("inserted-text.md", "w", encoding="utf8").write("\n\n".join([n for _, _, n in INS] + [r[2] for r in REPL] + [NEW_BULLET[1]] + list(COMMENTS.values())))
print("edits applied")
