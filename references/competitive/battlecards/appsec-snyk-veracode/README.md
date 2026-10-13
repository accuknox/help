# AppSec comparison set

Three branded A4 PDFs for prospects, built from one Google Sheet.

Sheet: [AccuKnox_vs_Snyk_vs_Veracode_vs_Checkmarx](https://docs.google.com/spreadsheets/d/1hbJFz14lS7VCQk34PP9wZFCKFYpN2drOlPs_lJkTtVM/edit).
The build reads the "Detailed Comparison" tab, exported to `detailed.json`.

## Three PDFs and Their Build Source

| Path | What it holds |
| --- | --- |
| `accuknox-appsec-comparison-scorecard.pdf` | Four vendors, 51 capabilities |
| `accuknox-vs-snyk.pdf` | Head-to-head with Snyk |
| `accuknox-vs-veracode.pdf` | Head-to-head with Veracode |
| `build.py` | The set's SPEC: themes, strengths, sources and docs links. Calls `../../pdf-engine/engine.py` |
| `data.py` | Parses the sheet, holds every override and the short AccuKnox lines |
| `detailed.json`, `aspm.json`, `ref.json` | Raw exports of the three sheet tabs |
| `search-results-raw.txt` | Competitor documentation URLs found on 2026-10-13 |

## One Command Rebuilds All Three PDFs

```bash
cd references/competitive/battlecards/appsec-snyk-veracode
python build.py
```

The build needs `playwright` with Chromium, `pypdf` and `Pillow`. It loads Space Grotesk and
Hanken Grotesk from Google Fonts, so it needs network access.

## Nine Ratings Were Corrected Against Vendor Docs

Competitor ratings were checked against vendor documentation on 2026-10-13. Each change lives in
`OVERRIDES` in `data.py`, with its source URL.

| Vendor | Row | Sheet said | PDF says | Source |
| --- | --- | --- | --- | --- |
| Snyk | 9 Secret scanning | Partial | Yes | [Snyk Secrets](https://snyk.io/product/snyk-secrets/) |
| Snyk | 11 Scan profiles | Partial | Yes | [Built-in scan profiles](https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-api-web/start-scanning/overview-scan-settings/built-in-scan-profiles) |
| Snyk | 12 MFA and TOTP | Partial | Yes | [2FA with TOTP](https://developers.probely.com/api/tutorials/target-authentication/how-to-setup-2fa-totp-target-login-form/) |
| Snyk | 13 Vulnerability coverage | Partial | Yes | [Snyk API & Web](https://snyk.io/product/dast-api-web/) |
| Snyk | 14 Retest workflow | Partial, "manually diffing" | Partial, "not confirmed" | no source found |
| Snyk | 24 API discovery | No | Partial | [Snyk API & Web](https://snyk.io/product/dast-api-web/) |
| Snyk | 25 Spec ingestion | Partial | Yes | [Snyk API & Web](https://snyk.io/product/dast-api-web/) |
| Veracode | 24 API discovery | No | Partial | [Discover external assets](https://docs.veracode.com/r/Discover_external_assets) |
| Veracode | 25 Spec ingestion | Partial | Yes | [Dynamic Analysis](https://docs.veracode.com/r/veracode_dynamic) |

AccuKnox cells for rows 6, 12 and 43 were reworded. The Detailed tab won over the Summary tab on
the six rows where they disagree (8, 45, 47, 48, 49, 50).

Four AccuKnox reference URLs in the sheet's "Accuknox-reference" tab return 403 because the pages
do not exist. The build uses these pages instead: `how-to/findings-lifecycle`,
`use-cases/rules-engine-ticket-creation`, `getting-started/runtime-sec-arch` and
`support-matrix/kubearmor-support-matrix`.

## Three Open Items Need a Human

- Checkmarx ratings come straight from the sheet. No Checkmarx documentation was opened.
- No public source was found for Snyk or Veracode deployment models (rows 37 to 39) or compliance
  frameworks (rows 34 and 35).
- The one slop-scorer CRIT is "Comprehensive", the name of AccuKnox's DAST scan tier.
