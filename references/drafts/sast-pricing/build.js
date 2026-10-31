const AK = "C:/Users/AtharvaShah/AppData/Roaming/Claude/local-agent-mode-sessions/skills-plugin/34734d1b-d3df-40ca-9bdf-6cb987baf225/b6eab119-908c-4c81-87d5-3dbb18242d4e/skills/ak-pptx/scripts/ak.js";
const ak = require(AK); const { C } = ak;
(async () => {
  const pres = ak.createDeck({ title: "SAST Pricing Model" });
  const s = ak.contentSlide(pres, {
    eyebrow: "SAST pricing proposal",
    title: "Price SAST per Contributing Developer, Not per Project",
    notes: "Partners and customers tell us they run monorepos and cannot say how many projects they have. A per project price forces them to guess, and every guess becomes a negotiation. Our proposal is to price by contributing developer, the number of people who commit code in the last 90 days. On the left, Veracode charges per application, which hurts monorepo and microservice teams. Checkmarx charges per contributing developer. We follow the Checkmarx unit but keep repos and projects unlimited. On the right are the four rules: count people, scan everything, volume bands, and a yearly true-up. Next step: Rahul to set the per developer rate and the band thresholds."
  });
  const rows = [
    { lab: "VERACODE · PER APPLICATION", t: "A monorepo has no clear app count", ic: "tb:TbBoxMultiple", mark: "tb:TbCircleX", mc: C.red, hi: false },
    { lab: "CHECKMARX · PER DEVELOPER", t: "Headcount is easy to count", ic: "tb:TbUsers", mark: "tb:TbCircleCheck", mc: C.blue, hi: false },
    { lab: "ACCUKNOX · PROPOSED", t: "Per developer, unlimited repos", ic: "tb:TbUsersGroup", mark: "tb:TbCircleCheck", mc: C.accent, hi: true },
  ];
  const x0 = 0.6, w0 = 5.7, h0 = 1.4, g = 0.15; let y = 1.65;
  for (const r of rows) {
    ak.card(s, { x: x0, y, w: w0, h: h0, accent: r.hi ? "accent" : (r.mark.includes("X") ? "red" : "blue"), fill: r.hi ? C.tintAccent : C.white });
    await ak.icon(s, r.ic, { x: x0 + 0.3, y: y + 0.45, s: 0.5 });
    ak.text(s, r.lab, { x: x0 + 1.05, y: y + 0.3, w: 3.6, h: 0.28, fontSize: 10, bold: true, color: r.hi ? C.accent : C.blue });
    ak.text(s, r.t, { x: x0 + 1.05, y: y + 0.6, w: 3.6, h: 0.6, fontSize: 16, bold: true, color: C.ink, valign: "top" });
    await ak.icon(s, r.mark, { x: x0 + w0 - 0.75, y: y + 0.5, s: 0.4, color: r.mc });
    y += h0 + g;
  }
  const pts = [
    ["tb:TbUsers", "Count people, not projects", "A contributing developer is a unique committer to scanned repos in the last 90 days."],
    ["tb:TbInfinity", "Scan everything", "Repos, monorepos and projects are unlimited for each developer."],
    ["tb:TbChartBar", "Volume bands", "The rate per developer drops at each band. Bots and read-only users are free."],
    ["tb:TbRefresh", "Yearly true-up", "We recount at renewal. No mid-term overage fees."],
  ];
  const x1 = 6.9, w1 = 5.85; y = 1.65;
  for (const [ic, t, b] of pts) {
    await ak.icon(s, ic, { x: x1, y: y + 0.08, s: 0.42 });
    ak.text(s, t, { x: x1 + 0.7, y: y, w: w1 - 0.7, h: 0.36, fontSize: 18, bold: true, color: C.ink });
    ak.text(s, b, { x: x1 + 0.7, y: y + 0.4, w: w1 - 0.7, h: 0.62, fontSize: 14, color: C.body, valign: "top" });
    y += 1.2;
  }
  ak.text(s, "Competitor models: Nat Natraj's note of 23 Oct 2026, based on third-party estimates. Rates and bands: Sales Ops.", { x: 0.6, y: 6.38, w: 12.1, h: 0.3, fontSize: 12, color: C.muted });
  await ak.finalize(pres, "D:/AccuKnox/help/references/drafts/sast-pricing/sast-pricing-model-v1.pptx");
})().catch(e => { console.error(e); process.exit(1); });
