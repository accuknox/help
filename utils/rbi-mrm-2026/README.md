# RBI Model Risk Management (2026) deliverables

Response assets for the RBI draft *Guidance on Regulatory Principles for Model
Risk Management*, issued 24 June 2026, open for comment until 24 July 2026
([source](https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63006)).

Both assets map the draft, requirement by requirement, to AccuKnox AI and ML
security controls, and are honest about the parts that stay with the regulated
entity. They cover only what the draft asks for.

| File | What it is |
|---|---|
| [blog-rbi-model-risk-management.md](blog-rbi-model-risk-management.md) | The blog. Plain, technical, under 1500 words, SEO front matter (title, meta, slug, keywords, cover-image prompts), inline reference links, six captioned images (three flow/architecture diagrams and three console screenshots). |
| AccuKnox-RBI-Model-Risk-Management-Whitepaper.docx | The white paper, a final copy. Branded DOCX built from `utils/doc-ppt-template/WORD_TEMPLATE_ACCUKNOX.docx`. Front cover, contents, an executive summary, the requirement map in "RBI asks / AccuKnox delivers" form with inline links (no paragraph numbers), a consolidated mapping table, sources, and a 16-figure appendix (four diagrams plus twelve console screenshots). ~21 pages. |
| [build_whitepaper.py](build_whitepaper.py) | Regenerates the white paper. Run with `py -3.11 build_whitepaper.py`. |
| blog-images/ | Six images used in the blog: three flow/architecture diagrams (AI estate, the stateful firewall pipeline, the AI-DR workflow) and three console screenshots, all cropped and captioned. |
| whitepaper-images/ | Appendix images: four diagrams (AI-SPM architecture, managed/on-prem map, firewall pipeline, AI-DR workflow) plus twelve console screenshots. |

## Notes

- Dashboard screenshots come from `utils/brian-demo-screenshots/` (captions in its `DEMO-SUMMARY.md`). Diagrams come from the docs folder (`docs/use-cases/images/aidr`, `ai-overview`) and the AI Security macro deck in `utils/technical-reference/`.
- The white paper's table of contents is a Word field. It fills in when the file
  is opened in Microsoft Word (the document is set to update fields on open) or
  by selecting all and pressing F9. A LibreOffice PDF export will not populate it.
- Writing follows the no-AI-tells style rules in the repo `CLAUDE.md`: no em or en
  dashes, plain words, no marketing filler.
