Scrape ID: 01a1361f-eb0b-72c3-9e78-08dffd94c24c
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

The **Audit Log** tab shows changes to your policy configuration.

AIDR records policy configuration changes each time you save a policy.

Each logged event contains:

- **Time** \- Date and time of the event
- **User** \- User who performed the action
- **Action** \- Description of the action performed
- **Target** \- ID of the affected policy
- **Message** \- Short summary of the event
- **Old** \- Previous value of the resource
- **New** \- Updated value of the resource

Changed values in the **Old** and **New** fields are highlighted in yellow.

Filter activity logs by date range and attributes.
The search bar refines results with:

- Completion suggestions for available attributes and their values
- Filter dialog (funnel icon)
- Date range control

Click the gear icon to select which columns are visible in the log table.

Sort the table by clicking column headers.

Example policy change event log

```json
{
  "source": "ppi_f7lrnyvjyy67qwhfaedt6e75c34bdctm",
  "target": "aidr_app_protected_input_policy",
  "action": "update",
  "user": "user@example.com",
  "message": "AIDR policy \"App/Agent Protected Input\" updated by user@example.com",
  "old": {
    "access_rules": [\
      ...\
    ],
    "description": "Enforces guardrails on raw user input at the app/agent boundary. Blocks prompt injection, PII, and secrets.",
    "detectors": [\
      {\
        "detector_name": "prompt_injection",\
        "settings": {\
          "action": "block"\
        },\
        "state": "disabled"\
      },\
      {\
        "detector_name": "pii_entity",\
        "settings": {\
          "rules": [\
            ...\
          ]\
        },\
        "state": "disabled"\
      }\
    ],
    "name": "App/Agent Protected Input",
    "version": "v1.1"
  },
  "new": {
    "access_rules": [\
      ...\
    ],
    "description": "Enforces guardrails on raw user input at the app/agent boundary. Blocks prompt injection, PII, and secrets.",
    "detectors": [\
      {\
        "detector_name": "prompt_injection",\
        "settings": {\
          "action": "block"\
        },\
        "state": "enabled"\
      },\
      {\
        "detector_name": "pii_entity",\
        "settings": {\
          "rules": [\
            ...\
          ]\
        },\
        "state": "enabled"\
      }\
    ],
    "name": "App/Agent Protected Input",
    "version": "v1.1"
  }
}
```

## Search bar [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity\#search-bar "Direct link to Search bar")

By default, the log viewer displays events from the past two hours.

To customize your search:

- Click the funnel icon to open the filter dialog, enter your criteria, and click **Search**.
The search syntax appears in the search bar, and matching results display in the table.
- Place your cursor in the search bar to view a dropdown of available search parameters. Start typing to filter the list and use autocompletion to build your query.
- Enter your query manually. For more information, see [search syntax](https://aidr-docs.crowdstrike.com/docs/audit/using-secure-audit-log/searching-the-logs#search-syntax).

## Date range [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity\#date-range "Direct link to Date range")

All searches must include a time range, with the default set to the most recent two hours.

The date range selector next to the search button provides several options:

- **Quick selections** \- Select a relative range of 1, 7, or 30 days.
- **Relative** \- Define a custom relative date range.
- **Between** \- Search for log events between two specific dates.
- **Before** \- Search for events that occurred before a specific date.
- **After** \- Search for events that occurred after a specific date.

You can apply a time range filter directly from the logs table.
Add a time field to the table columns, then hover over its value in a row.
Click the plus icon next to it to filter by that exact date or set it as a range boundary.

## Event details [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity\#event-details "Direct link to Event details")

To view all fields for an event, click its row in the search results. The row expands to show every event field, including those not currently visible in the table.

If a field (such as **Old** or **New**) contains JSON data, it displays as an interactive JSON tree.

- [Search bar](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity#search-bar)
- [Date range](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity#date-range)
- [Event details](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity#event-details)
