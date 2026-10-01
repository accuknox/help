# Campaign Brief Fields

Fill every field before a campaign gets a slide. These keys match one campaign block in
`campaigns.json`, so `build_deck.py` reads them directly. Write `[bracket]` for any fact nobody has
given, and name the person who will fill it.

| Key | What goes in it | Example |
|---|---|---|
| `id` | Short slug | `ctem` |
| `name` | Product name as the buyer knows it | CTEM |
| `channel` | LinkedIn, or X and Reddit for developer products | LinkedIn |
| `goal` | The one result that counts | Demo requests from security leaders who still test with a yearly pentest |
| `offer` | What the buyer gets for the form fill | Demo plus a free external attack-surface scan |
| `cta` | The button, matched to the offer | Request Demo |
| `fallback` | The assessment offer that replaces the main offer when leads stay at zero after $500. It stays on the demo form | Free AI red-team assessment of one model endpoint |
| `budget` | Always a $1,000 group cap, split across two campaigns | Prospecting $850 lifetime, 28 days. Retargeting $150 lifetime, days 15 to 28 |
| `flight` | 4 weeks unless the brief says otherwise | 4 weeks, 2026-10-19 to 2026-11-15 |
| `flight_bar` | Start and end week on the deck calendar | `[1, 5]` |
| `icp` | Job titles, the forecast, company size, industries, geography. No seniority facet | See the Q4 2026 file |
| `form` | A question headline and two multiple-choice questions, neutral answer first | Get a free attack-surface scan of your domain |
| `kpi` | The targets the kill rules test | CTR 0.6%+, CPC under $15, CPL under $400, 2+ demos held |
| `why` | One or two sentences on why this buyer acts now | Goes into the speaker notes |
| `pick` | Which ad should win, and why | Goes on the creative slide |
| `ads` | Three ads: one product proof plus two photo or screenshot ads. No plain gradients | Each with headline, body, tagline, intro, LinkedIn headline and button |

An ad that ships as a finished image uses `image_only` with the image path, and the renderer skips
it.
