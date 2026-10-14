Scrape ID: 01a1361d-7609-7799-96f0-9466cc3f2fce
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Site Access Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#site-access-rules "Direct link to Site Access Rules")

Use site access rules to block, redirect, report, or ignore visits to sites monitored by the browser collector.

### Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#requirements "Direct link to Requirements")

Site Access management requires the CrowdStrike-hosted browser extension version **1.x.x**.

The Chrome Web Store edition version **0.6.x** doesn't support Site Access.
To migrate to the CrowdStrike-hosted extension, see:

- [Chrome](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome/migrate)
- [Edge](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/migrate)
- [Firefox](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/firefox/migrate)

### How rules execute [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#how-rules-execute "Direct link to How rules execute")

AIDR evaluates rules in the order they appear.
Each rule matches the visited site against its site collection and applies the configured action.

- `Ignore`, `Block`, and `Redirect` stop execution.
- `Report` and `Continue` proceed to the next rule.
- A site can accumulate multiple report detections before a terminal action.
- If no terminal action matches, AIDR implicitly allows the site.
- After site access evaluation completes, [prompt inspection](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#prompt-rules) applies to supported sites.

### Actions [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#actions "Direct link to Actions")

| Action | Behavior | Execution |
| --- | --- | --- |
| `Continue` | Proceed to next rule without logging | Continues |
| `Ignore` | Allow access without logging or prompt inspection | Stops |
| `Report` | Log access as a detection, continue to next rule | Continues |
| `Block` | Block access and display a custom block message | Stops |
| `Redirect` | Redirect to a specified URL | Stops |

### Configure site access rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#configure-site-access-rules "Direct link to Configure site access rules")

1. Go to the policy details page for a browser collector policy.
2. Open the **Site Access** tab.
3. Click **\+ Add Site Access Rule**.
4. Configure the rule:
   - **If** \- Select a [site collection](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#site-collections).
   - **Then**\- Select an action.
     A gear icon indicates that an action requires additional input:
     - `Block` \- Enter a custom block message.
     - `Redirect` \- Enter the destination URL.
   - **Else** \- Select a fallback action (Continue or another action).
5. Reorder rules by dragging them with the six-dot handle on the left.
6. Click **Save Changes**.

### Site collections [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#site-collections "Direct link to Site collections")

Site collections group sites into reusable sets shared across your AIDR browser collector policies.

#### Select site collection [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#select-a-site-collection "Direct link to Select site collection")

In the **If** dropdown, select a site collection.

#### Create site collection [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#create-a-site-collection "Direct link to Create site collection")

1. In the **If** dropdown, click **\+ Create New Site Collection**.
2. In the **Creating Shared Site Collection** dialog, enter a collection name.
3. Select sites from the catalog.
The catalog includes CrowdStrike-provided GenAI sites and custom sites you've added.
4. Search or filter by category to find sites.
5. (Optional) Enable auto-sync on a category to include all its sites automatically.
6. Click **Create**.

#### Edit site collection [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#edit-a-site-collection "Direct link to Edit site collection")

Click **Edit Site Collection** in a rule.
Changes apply to all policies that reference that collection.

note:

Site collection changes, such as adding or removing sites, may take up to one hour to take effect.
The browser extension checks for monitored site updates on an hourly cycle.

#### Default sites [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#default-sites "Direct link to Default sites")

The **Generative AI** collection includes CrowdStrike-provided sites by default.
You can't delete or modify these sites.
To view the site details, hover over a site row and click the eye icon.

#### Add custom sites [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#add-custom-sites "Direct link to Add custom sites")

To add a site that isn't in your CID catalog:

1. In the **Creating Shared Site Collection** dialog, click **\+ Site**.
2. In the **Create Site** dialog, enter the site properties:
   - **Site Name** (required)
   - **Description** (optional)
   - **Category** (required)
   - **Domains**(required) - One or more domains.
     For each domain, select a match type:
     - **Domain Is** \- Match the exact domain only.
     - **Domain or Subdomain Is** \- Match the domain and all its subdomains.
       AIDR records the domain with a wildcard prefix, like `*.example.com`.

#### Edit or delete custom sites [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#edit-or-delete-custom-sites "Direct link to Edit or delete custom sites")

In the **Creating Shared Site Collection** and **Editing Shared Site Collection** dialogs, custom sites display a comment icon.

Hover over a custom site row to see available options:

- Hover over the comment icon to view the site description.
- Click the pencil icon to edit the custom site.
- Click the delete icon to delete the custom site.

### Prompt Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#prompt-rules "Direct link to Prompt Rules")

Prompt rules execute only if site access evaluation allows access to the site.
If access rules block, redirect, or ignore a site, prompt inspection doesn't run for that site.

Click the **Prompt inspection is applied to <n> inspection sites** button.

- Hover over the button to view the **Prompt Inspection Sites** popup with inspected sites.

- Click the button to open the **Prompt Inspection Sites** panel.

The panel lists supported sites that receive prompt inspection and sites excluded by access rules.
Sites excluded by an access rule display a **Blocked by access rule** label.

If access rules exclude sites from prompt inspection, a warning appears at the bottom of the panel:





warning:





`<n>` sites are blocked by access rules and will not have prompt inspection applied.
Review your site access rules above if this is unintended.


To configure prompt rules, see [Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules).

### Compare to collector site settings [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access\#compare-to-collector-site-settings "Direct link to Compare to collector site settings")

On the collector **Config** page, in the **Sites** section, you can configure how policy rules apply to each supported AI provider domain.
Select `Use Policy`, `Monitor Only`, `Discovery`, or `Disabled` for each domain.

With the browser extension version **1.x.x**, you can apply site access rules to any domain.
You can map collector site settings to site access rules:

| Collector site setting | Site access rule equivalent |
| --- | --- |
| `Use Policy` | No rule needed. Prompt inspection applies by default. |
| `Monitor Only` | No rule needed. Enable **Report Only Mode** on the policy for equivalent behavior. This mode applies to all sites in the policy. |
| `Discovery` | `Report` followed by `Ignore`. Two rules targeting the same collection are required: `Report` is non-terminal and logs the visit, while `Ignore` stops evaluation and prevents prompt inspection. |
| `Disabled` | `Ignore` |

- [Site Access Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#site-access-rules)
  - [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#requirements)
  - [How rules execute](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#how-rules-execute)
  - [Actions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#actions)
  - [Configure site access rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#configure-site-access-rules)
  - [Site collections](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#site-collections)
    - [Select site collection](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#select-a-site-collection)
    - [Create site collection](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#create-a-site-collection)
    - [Edit site collection](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#edit-a-site-collection)
    - [Default sites](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#default-sites)
    - [Add custom sites](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#add-custom-sites)
    - [Edit or delete custom sites](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#edit-or-delete-custom-sites)
  - [Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#prompt-rules)
  - [Compare to collector site settings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access#compare-to-collector-site-settings)
