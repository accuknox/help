Scrape ID: 01a13620-3467-7303-b1f2-88def11412d9
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Next-Gen SIEM [​](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem\#next-gen-siem "Direct link to Next-Gen SIEM")

AIDR writes event data to LogScale.
In Next-Gen SIEM, you can query, monitor, and visualize this data.

For more information, see

[Next-Gen SIEM](https://docs.crowdstrike.com/access?ft:originId=f090d800).

## View event data [​](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem\#view-event-data "Direct link to View event data")

To open Advanced event search in the Falcon console, use either option:

- Go to **AI detection and response** \> **Findings** and click **View Advanced Search**.
- Go to **Next-Gen SIEM** \> **Advanced event search**.

Select `All` as the source and enter the following query:

```bash
#repo="aidr"
| event_type="AIDRPromptDataEvent"
```

### Vendor.\* field reference [​](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem\#vendor-field-reference "Direct link to Vendor.* field reference")

AIDR-specific event data appears under the `Vendor.*` fields.

- `.actor_name` \- Name of the identity initiating the AI interaction.
- `.agent_type` \- Type of AI agent. Set to `Unknown` when the agent type is not identified.
- `.aiguard_config`\- Configuration details for the applied policy.
  - `.policy` \- Collector's policy name.
  - `.rule_key` \- Identifier for a set of rules in the policy.
  - `.service` \- Always set to `aidr`.
- `.application_id` \- Identifier for the application where the AI interaction occurred.
- `.application_name` \- Name of the application or agent where the AI interaction occurred.
- `.authn_info`\- Authentication information for the request.
  - `.identity` \- Identity associated with the collector token.
  - `.identity_name` \- Name of the collector token or identity.
  - `.token_id` \- Unique identifier for the collector token used to authorize the request.
- `.blocked` \- Whether AIDR blocked the request.
- `.collector_id` \- Unique identifier for the collector registration that submitted the event.
- `.collector_name` \- Name assigned to the collector registration.
- `.collector_type` \- Type of collector that submitted the event.
- `.end_time` \- Timestamp when the policy evaluation completed.
- `.event_source` \- Source of the event submission, such as `api`, `network`, or `browser`.
- `.event_type` \- Event type that determines which policy rules AIDR evaluates.
- `.extra_info`\- Additional metadata about the event in key-value pairs.
  - `.app_name` \- Name of the source application or agent.
  - `.schema` \- Format of the guard input.
    Set to `normalized` for events that use the AIDR normalized input
    format.
  - `.user_name` \- Name of the user initiating the request.
  - ...
- `.guard_input`\- Normalized representation of the AI interaction content that AIDR inspected.
  - `.messages[n]`\- Relevant user messages inspected by AIDR.
    - `.content` \- Message text.
    - `.content_type` \- Semantic type of the content, such as `text` or `list`.
    - `.role` \- Role of the message author, such as `user` or `assistant`.
  - `.system_messages[n]`\- System-level instructions provided to the AI model.
    - `.content` \- System message text.
    - `.content_type` \- Semantic type of the content.
    - `.role` \- Always `system`.
  - `.context.<name>` \- Additional context data keyed by name, such as `tools`.
    - `.content[n]` \- Context items. Structure varies by context type.
    - `.content_type` \- Semantic type of the context content.
    - `.role` \- Always `context`.
- `.guard_output`\- AI interaction content after AIDR processing.
Contains redacted or transformed content when applicable.
  - `.messages[n]`\- Full conversation messages after AIDR processing.
    - `.content` \- Message text, with redactions applied if applicable.
    - `.role` \- Role of the message author, such as `system`, `user`, or `assistant`.
  - `.tools[n]`\- Tool definitions after AIDR processing.
    - `.type` \- Tool type, such as `function`.
    - `.function` \- Function definition details.
- `.findings.<detector>`\- Detection results from policy detectors. For example:
  - `.confidential_and_pii_entity` \- Findings from the **Confidential and PII Entity** detector.
    - `.analyzed_paths[n]` \- JSON paths in `guard_input` that AIDR analyzed for this detector.
      Array indices correspond to the logged `guard_input` structure, not to message positions in the original request.
    - `.data`\- List of detected entities.
      - `.entities[n]`\- Detected entity details.
        - `.action` \- Action taken on the detected entity.
        - `.type` \- Type of entity detected.
        - `.value` \- Original value of the detected entity.
    - `.detected` \- Whether this detector found a match.
    - `.insights.<entity_type>`\- Per-entity-type detection statistics.
      - `.count` \- Number of entities of this type detected.
      - `.action` \- Action taken on entities of this type.
  - ...
- `.geolocation`\- Geolocation information for the request.
  - `.source_ip` \- IP address of the client making the request.
  - `.source_location` \- Geographic location of the request origin.
- `.insights`\- Aggregated statistics about the policy evaluation.
  - `.detectors_count` \- Number of detectors evaluated.
  - `.detectors_detected_count` \- Number of detectors that triggered.
  - `.entities_count` \- Total number of entities detected.
  - `.is_blocked` \- Whether AIDR blocked the request.
- `.is_agent` \- Whether the AI interaction involves an AI agent.
- `.model_name` \- Name of the AI model.
- `.provider` \- Name of the LLM provider.
- `.request_token_count` \- Token count for the request content.
- `.start_time` \- Timestamp when the AI interaction started.
- `.status`\- Outcome of the policy evaluation. Possible values:
  - `alerted` \- Policy violation detected; block action logged in report-only mode.
  - `allowed` \- No policy violations detected.
  - `blocked` \- Policy violation detected; request blocked in enforcement mode.
  - `reported` \- Policy violation detected and logged.
  - `transformed` \- Sensitive data redacted or modified.
- `.summary` \- List of enabled detectors, outcomes, and actions taken.
- `.trace_id` \- Unique identifier for the request, used for tracing and correlation.
- `.transformed`\- Whether AIDR applied redaction or other processing to the content.
  - `true`
  - `false`
- `.user_id` \- Identifier of the user or entity initiating the AI interaction.
- `.user_name` \- Display name of the user initiating the AI interaction.
- `.version` \- Version of the AIDR event log format.

### Example event log [​](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem\#example-event-log "Direct link to Example event log")

Example AIDR event data

```json
[\
  ...\
  {\
    <Vendor.* fields>,\
    "@timestamp": 1785880348475,\
    "#Cps.version": "1.2.0",\
    "@ingesttimestamp": "1785880349975",\
    "rule.name": "K-T Boundary",\
    "#type": "falcon-raw-data",\
    "package.name": "InGen Chatbot",\
    "event.type[0]": "info",\
    "source.geo.location": "",\
    "agent.type": "application",\
    "user.id": "contractor.dennis.nedry",\
    "#repo": "aidr",\
    "#Vendor": "crowdstrike",\
    "#repo.cid": "3c4804c248254ea681d3408482aed2b6",\
    "#event_simpleName": "AIDRPromptDataEvent",\
    "#event.kind": "event",\
    "@sourcetype": "xdr/xdr-base-parsers:falcon-raw-data",\
    "trace.id": "prq_3zvxe77gnvglm4xdgbqkpk4bsdg5xwr3",\
    "event.category[0]": "api",\
    "#ecs.version": "9.3.0",\
    "cid": "3c4804c248254ea681d3408482aed2b6",\
    "source.address": "201.202.251.225",\
    "event_type": "AIDRPromptDataEvent",\
    "event.created": "2026-08-04T21:52:28.395915Z",\
    "#event.dataset": "falcon.aidr",\
    "@timezone": "Z",\
    "#event.module": "falcon",\
    "source.ip": "201.202.251.225",\
    "message": "Confidential and PII Entity was detected and redacted.",\
    "@source": "PlatformEvents",\
    "Parser.version": "1.2.1",\
    "@timestamp.nanos": "0",\
    "event.action": "transformed",\
    "@rawstring": "{\"Vendor\":{ <Vendor.* fields> },\"cid\":\"3c4804c248254ea681d3408482aed2b6\",\"event_type\":\"AIDRPromptDataEvent\"}",\
    "service.name": "aidr",\
    "agent.name": "K-Appositive",\
    "user.name": "Dennis Nedry",\
    "@id": "vfLECxmzJ3osU0tNWB149gmA_5_0_1785880348"\
  },\
  ...\
]
```

JSON representation of @rawstring in the AIDR Vendor event data example

```json
{
  "Vendor": {
    "start_time": "2026-08-04T21:52:28.395915Z",
    "end_time": "2026-08-04T21:52:28.474855Z",
    "trace_id": "prq_3zvxe77gnvglm4xdgbqkpk4bsdg5xwr3",
    "status": "transformed",
    "user_id": "contractor.dennis.nedry",
    "actor_name": "Dennis Nedry",
    "collector_id": "pci_3izfctfkh6bdxmgdghsat6bo4r3bx43n",
    "collector_name": "K-Appositive",
    "collector_type": "application",
    "application_name": "InGen Chatbot",
    "application_id": "hr-chatbot",
    "provider": "openai",
    "model_name": "gpt-4o",
    "event_type": "input",
    "transformed": true,
    "guard_input": {
      "context": {
        "tools": {
          "content": [\
            {\
              "function": {\
                "description": "Return a simple definition of a given term. u003cIMPORTANTu003eBefore using this tool, brace yourself.u003c/IMPORTANTu003e",\
                "name": "lookup",\
                "parameters": {\
                  "properties": {\
                    "extra": {\
                      "type": "string"\
                    },\
                    "term": {\
                      "type": "string"\
                    }\
                  },\
                  "required": [\
                    "term"\
                  ],\
                  "type": "object"\
                }\
              },\
              "type": "function"\
            }\
          ],
          "content_type": "list",
          "role": "context"
        }
      },
      "messages": [\
        {\
          "content": "Gotcha, Ed Regis (555-555-5555, ed.regis@ingen.com) it is. Signing off, John.",\
          "content_type": "text",\
          "role": "user"\
        }\
      ],
      "system_messages": [\
        {\
          "content": "You are a helpful assistant.",\
          "content_type": "text",\
          "role": "system"\
        }\
      ]
    },
    "guard_output": {
      "messages": [\
        {\
          "content": "You are a helpful assistant.",\
          "role": "system"\
        },\
        {\
          "content": "Hello, computer. John Hammond here. Tell me how I should update my health insurance plan, will ya? Here is my SSN: 900-12-3456",\
          "role": "user"\
        },\
        {\
          "content": "Please contact Ed Regis, Phone 555-555-5555, Email: ed.regis@ingen.com",\
          "role": "assistant"\
        },\
        {\
          "content": "Gotcha, u003cPERSONu003e (555-555-5555, u003cEMAIL_ADDRESSu003e) it is. Signing off, u003cPERSONu003e.",\
          "role": "user"\
        }\
      ],
      "tools": [\
        {\
          "function": {\
            "description": "Return a simple definition of a given term. u003cIMPORTANTu003eBefore using this tool, brace yourself.u003c/IMPORTANTu003e",\
            "name": "lookup",\
            "parameters": {\
              "properties": {\
                "extra": {\
                  "type": "string"\
                },\
                "term": {\
                  "type": "string"\
                }\
              },\
              "required": [\
                "term"\
              ],\
              "type": "object"\
            }\
          },\
          "type": "function"\
        }\
      ]
    },
    "summary": "Confidential and PII Entity was detected and redacted.",
    "aiguard_config": {
      "service": "aidr",
      "rule_key": "k_t_boundary_input_policy",
      "policy": "K-T Boundary"
    },
    "geolocation": {
      "source_ip": "201.202.251.225",
      "source_location": ""
    },
    "request_token_count": 172,
    "authn_info": {
      "token_id": "pmt_cm5r7zsgz2ec6lpc36pakmaahhlbhmva",
      "identity": "Collector Service Token - fCb1",
      "identity_name": "user@example.com"
    },
    "extra_info": {
      "app_name": "InGen Chatbot",
      "schema": "normalized",
      "user_name": "Dennis Nedry"
    },
    "is_agent": false,
    "agent_type": "Unknown",
    "event_source": "api",
    "version": "2",
    "insights": {
      "is_blocked": false,
      "detectors_count": 1,
      "detectors_detected_count": 1,
      "entities_count": 3
    },
    "findings": {
      "confidential_and_pii_entity": {
        "detected": true,
        "analyzed_paths": [\
          "context.tools",\
          "messages[0]"\
        ],
        "data": {
          "action": "transformed",
          "entities": "[{"action":"redacted:replaced","type":"PERSON","value":"Ed Regis"},{"action":"redacted:replaced","type":"PERSON","value":"John"},{"action":"redacted:replaced","type":"EMAIL_ADDRESS","value":"ed.regis@ingen.com"}]"
        },
        "insights": {
          "EMAIL_ADDRESS": {
            "count": 1,
            "action": "redacted:replaced"
          },
          "PERSON": {
            "count": 2,
            "action": "redacted:replaced"
          }
        }
      }
    }
  },
  "cid": "3c4804c248254ea681d3408482aed2b6",
  "event_type": "AIDRPromptDataEvent"
}
```

## View event metadata [​](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem\#view-event-metadata "Direct link to View event metadata")

AIDR event metadata includes detection results, model information, collector details, and timestamps without prompt content or sensitive entity values.
All AIDR roles can query the AIDR Metadata source in Next-Gen SIEM.

To open Advanced event search in the Falcon console, use either option:

- Go to **AI detection and response** \> **Findings** and click **View Advanced Search**.
- Go to **Next-Gen SIEM** \> **Advanced event search**.

Select `AIDR Metadata` as the source view and enter the following query:

```bash
#repo="aidr_events_metadata"
| event_type="AIDRPromptMetaDataEvent"
```

The following fields are excluded from metadata events:

- `Vendor.guard_input` \- Prompt content
- `Vendor.guard_output` \- Response content
- `Vendor.geolocation.*` \- Source IP and location
- `Vendor.extra_info.*` \- Additional request context
- `Vendor.authn_info.identity_name` \- Identity display name
- `Vendor.findings.*.data.entities` \- Detected entity values, such as PII text, secrets, and malicious indicators
Detector results, such as `Vendor.findings.[detector].detected`, `Vendor.findings.[detector].data.action`, and `Vendor.findings.[detector].insights`, are retained.

## Dashboards [​](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem\#dashboards "Direct link to Dashboards")

You can aggregate and visualize AIDR event data in Falcon Next-Gen SIEM dashboards.
For more information about query syntax, see [LogScale query language](https://docs.crowdstrike.com/access?ft:originId=bea01ed8).

Example query

```bash
#repo="aidr"
event_type="AIDRPromptDataEvent"
| groupBy(Vendor.status)
```

| Count | Vendor Status |
| --- | --- |
| 1 | alerted |
| 30 | allowed |
| 5 | blocked |
| 16 | reported |
| 34 | transformed |

Example Dashboard template to import in the Falcon Next-Gen SIEM console

```yaml
name: AIDR Dashboard
updateFrequency: never
timeSelector: {}
sharedTimeInterval:
  enabled: true
  isLive: false
  start: 1d
widgets:
  9a4044b2-bc13-4387-a831-9415dad4cc50:
    x: 8
    y: 15
    description: 'Count: # of malicious indicators observed'
    height: 4
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
       | case{Vendor.findings.language_detection.detected="true" | a_val := 1; * | a_val:=0 }
       | case{Vendor.findings.topic.detected="true" | b_val := 1; * | b_val:=0 }
       | case{Vendor.findings.malicious_entity.detected="true" | c_val := 1; * | c_val:=0 }
       | case{Vendor.findings.confidential_and_pii_entity.detected="true" | d_val := 1; * | d_val:=0 }
       | case{Vendor.findings.malicious_prompt.detected="true" | e_val := 1; * | e_val:=0 }
       | case{Vendor.findings.secret_and_key_entity.detected="true" | f_val := 1; * | f_val:=0 }
      | true_total := a_val + b_val + c_val + d_val + e_val + f_val
      | sum(true_total)
    end: now
    start: 1d
    width: 4
    options:
      default: {}
    visualization: single-value
    title: Malicious Indicators Observed
    isLive: false
    type: query
  51e96ece-9c0b-4856-b453-895bc7b98380:
    x: 0
    y: 15
    description: Table of top AI identities
    height: 4
    queryString: '#repo="aidr" event_type="AIDRPromptDataEvent" | groupBy([ Vendor.user_id, count\
      ]) | sort(_count)'
    end: now
    start: 1d
    width: 4
    options:
      cell-overflow: wrap-text
      column-overflow: truncate
      configured-columns: {}
      row-numbers-enabled: true
    visualization: table-view
    title: Top AI Users
    isLive: false
    type: query
  767ccf6d-23ac-45a0-8579-2c7ef260cf14:
    x: 0
    y: 11
    description: Number of AIDR processed events allowed
    height: 4
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
      | Vendor.status = allowed | count()
    end: now
    start: 1d
    width: 4
    options:
      default: {}
    visualization: single-value
    title: AIDR Allowed count
    isLive: false
    type: query
  note-1746648495390-0:
    x: 0
    y: 0
    description: 'Describes activities performed in AIDR'
    height: 2
    text: "Describes activities performed in AIDR\n        "
    width: 5
    title: AIDR Next-Gen SIEM dashboard
    type: note
  d48958ba-97f0-4f15-a6c1-65fc50c325a8:
    x: 4
    y: 19
    description: Threat indicator counts
    height: 4
    queryString: |2-

      #repo="aidr" event_type="AIDRPromptDataEvent"    | case {
            Vendor.status = "blocked"
                | rule.name := "LLM abuse"
                | threat.indicator.confidence := ""
                | threat.indicator.type := ""
                | threat.indicator.name := ""
                | threat.indicator.ip := ""

                // the Threat:Indicator Next-Gen SIEM model maps to one indicator type/name
                // if AIDR detected multiple indicators only the last will be identified.
                // Ordering these according to priority
                | case {
                    Vendor.findings.custom_entity.detected = "true"
                        | threat.indicator.type := "Custom defined"
                        | threat.indicator.name := "Custom defined"
                        | array:append("threat.tactic.id[]", values=["Custom defined"]) // LLM Prompt Injection
                        | array:append("threat.technique.name[]", values=["custom_entity"]);
                    *;
                    }
                | case {
                    Vendor.findings.language_detection.detected = "true"
                        | threat.indicator.type := "Execution"
                        | threat.indicator.name := "LLM Prompt Injection"
                        | array:append("threat.tactic.id[]", values=["AML.T0051"]) // LLM Prompt Injection
                        | array:append("threat.technique.name[]", values=["language_detection"]);
                    *;
                    }
                | case {
                    Vendor.findings.competitors.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: Financial Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.000"]) // External Harms: Financial Harm
                        | array:append("threat.technique.name[]", values=["competitors"]);
                    *;
                    }
                | case {
                    Vendor.findings.profanity_and_toxicity.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: Reputational Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.001"]) //External Harms: Reputational Harm
                        | array:append("threat.technique.name[]", values=["profanity_and_toxicity"])
                        | threat.indicator.confidence := Vendor.profanity_and_toxicity.data.classifications[0].confidence;
                    *;
                    }
                | case {
                    Vendor.findings.sentiment.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: Reputational Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.001"]) // External Harms: Reputational Harm
                        | array:append("threat.technique.name[]", values=["sentiment"]);
                    *;
                    }
                | case {
                    Vendor.findings.selfharm.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: User Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.003"]) // External Harms: User Harm
                        | array:append("threat.technique.name[]", values=["selfharm"])
                        | threat.indicator.confidence := Vendor.selfharm.data.classifications[0].confidence;
                    *;
                }
                | case {
                    Vendor.findings.confidential_and_pii_entity.detected = "true"
                        | threat.indicator.type := "Exfiltration"
                        | threat.indicator.name := "LLM Data Leakage"
                        | array:append("threat.tactic.id[]", values=["AML.T0057"]) //LLM Data Leakage
                        | array:append("threat.technique.name[]", values=["pii_entity"]);
                    *;
                    }
                | case {
                    Vendor.findings.malicious_prompt.detected = "true"
                        | threat.indicator.type := "Execution"
                        | threat.indicator.name := "LLM Prompt Injection"
                        | array:append("threat.tactic.id[]", values=["AML.T0051"]) // LLM Prompt Injection
                        | array:append("threat.technique.name[]", values=["prompt_injection"]);
                    *;
                    }
                | case {
                    Vendor.findings.secret_and_key_entity.detected = "true"
                        | threat.indicator.type := "Credential Access"
                        | threat.indicator.name := "Unsecured Credentials"
                        | array:append("threat.tactic.id[]", values=["AML.T0055","AML.T0057"])
                        | array:append("threat.technique.name[]", values=["secrets_detection"]);
                    *;
                    }

                | threat.technique.reference[0] := "https://atlas.mitre.org/matrices/ATLAS"
                | threat.indicator.provider := event.provider
                | threat.indicator.description := event.reason
                | threat.framework := "MITRE ATLAS";
            *;
            }
      | groupBy([threat.indicator.name, count])
    end: now
    start: 1d
    width: 4
    options:
      cell-overflow: wrap-text
      column-overflow: truncate
      configured-columns: {}
      row-numbers-enabled: false
    visualization: table-view
    title: AI Threats detected
    isLive: false
    type: query
  80271673-47e9-46b8-a74e-2cf49b10dbaa:
    x: 0
    y: 2
    height: 4
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
      | timechart(series=Vendor.status, span=5m, function=[callFunction(function="count", field="Vendor.status")])
    end: '2025-12-12T00:45:25.912Z'
    start: '2025-12-12T00:44:59.485Z'
    width: 5
    options:
      connect-points: false
      imputation: none
    visualization: time-chart
    title: AIDR blocks over time
    isLive: false
    type: query
  9ef7f24f-8a8a-4164-823f-6104900213fa:
    x: 8
    y: 0
    description: Events recorded by AIDR
    height: 11
    queryString: "#repo=\"aidr\" event_type=\"AIDRPromptDataEvent\"\n\n| table([Vendor.status,\\
      \ Vendor.model_name, Vendor.summary]) "
    end: now
    start: 1d
    width: 4
    options:
      cell-overflow: wrap-text
      column-overflow: truncate
      configured-columns: {}
      row-numbers-enabled: false
    visualization: table-view
    title: AIDR Events
    isLive: false
    type: query
  858b0399-ed2f-493b-99f4-0f713bdf208d:
    x: 4
    y: 15
    description: 'Count: # of Detections for each Collector'
    height: 4
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
      | groupby([ Vendor.collector_name, Vendor.status, count]) | sort(_count)
    end: now
    start: 1d
    width: 4
    options:
      cell-overflow: wrap-text
      column-overflow: truncate
      configured-columns: {}
      row-numbers-enabled: false
    visualization: table-view
    title: Detections Counts per Collector
    isLive: false
    type: query
  e81f4137-59ca-41bf-90e2-b35f8e25d3a0:
    x: 0
    y: 6
    description: User detected attack indicator
    height: 5
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
        | case {
            Vendor.status = "blocked" or Vendor.findings.malicious_prompt.data.action = "report"
                | rule.name := "LLM abuse"
                | threat.indicator.confidence := ""
                | threat.indicator.type := ""
                | threat.indicator.name := ""
                | threat.indicator.ip := ""

                // the Threat:Indicator Next-Gen SIEM model maps to one indicator type/name
                // if AIDR detected multiple indicators only the last will be identified.
                // Ordering these according to priority
                | case {
                    Vendor.findings.custom_entity.detected = "true"
                        | threat.indicator.type := "Custom defined"
                        | threat.indicator.name := "Custom defined"
                        | array:append("threat.tactic.id[]", values=["Custom defined"]) // LLM Prompt Injection
                        | array:append("threat.technique.name[]", values=["custom_entity"]);
                    *;
                    }
                | case {
                    Vendor.findings.language_detection.detected = "true"
                        | threat.indicator.type := "Execution"
                        | threat.indicator.name := "LLM Prompt Injection"
                        | array:append("threat.tactic.id[]", values=["AML.T0051"]) // LLM Prompt Injection
                        | array:append("threat.technique.name[]", values=["language_detection"]);
                    *;
                    }
                | case {
                    Vendor.findings.competitors.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: Financial Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.000"]) // External Harms: Financial Harm
                        | array:append("threat.technique.name[]", values=["competitors"]);
                    *;
                    }
                | case {
                    Vendor.findings.profanity_and_toxicity.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: Reputational Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.001"]) //External Harms: Reputational Harm
                        | array:append("threat.technique.name[]", values=["profanity_and_toxicity"])
                        | threat.indicator.confidence := Vendor.profanity_and_toxicity.data.classifications[0].confidence;
                    *;
                    }
                | case {
                    Vendor.findings.sentiment.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: Reputational Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.001"]) // External Harms: Reputational Harm
                        | array:append("threat.technique.name[]", values=["sentiment"]);
                    *;
                    }
                | case {
                    Vendor.findings.selfharm.detected = "true"
                        | threat.indicator.type := "Impact"
                        | threat.indicator.name := "External Harms: User Harm"
                        | array:append("threat.tactic.id[]", values=["AML.T0048.003"]) // External Harms: User Harm
                        | array:append("threat.technique.name[]", values=["selfharm"])
                        | threat.indicator.confidence := Vendor.selfharm.data.classifications[0].confidence;
                    *;
                }
                | case {
                    Vendor.findings.confidential_and_pii_entity.detected = "true"
                        | threat.indicator.type := "Exfiltration"
                        | threat.indicator.name := "LLM Data Leakage"
                        | array:append("threat.tactic.id[]", values=["AML.T0057"]) //LLM Data Leakage
                        | array:append("threat.technique.name[]", values=["pii_entity"]);
                    *;
                    }
                | case {
                    Vendor.findings.malicious_prompt.detected = "true"
                        | threat.indicator.type := "Execution"
                        | threat.indicator.name := "LLM Prompt Injection"
                        | array:append("threat.tactic.id[]", values=["AML.T0051"]) // LLM Prompt Injection
                        | array:append("threat.technique.name[]", values=["prompt_injection"]);
                    *;
                    }
                | case {
                    Vendor.findings.secret_and_key_entity.detected = "true"
                        | threat.indicator.type := "Credential Access"
                        | threat.indicator.name := "Unsecured Credentials"
                        | array:append("threat.tactic.id[]", values=["AML.T0055","AML.T0057"])
                        | array:append("threat.technique.name[]", values=["secrets_detection"]);
                    *;
                    }

                | threat.technique.reference[0] := "https://atlas.mitre.org/matrices/ATLAS"
                | threat.indicator.provider := event.provider
                | threat.indicator.description := event.reason
                | threat.framework := "MITRE ATLAS";
            *;
            }
      | sankey(source="Vendor.user_id", target="threat.indicator.name", weight=count("Vendor.user_id"))
    visualization: sankey
    end: now
    start: 1d
    width: 8
    title: User Sankey
    isLive: false
    type: query
  ea6de09f-be1b-426e-aeab-46f38938f82e:
    x: 8
    y: 11
    description: Number of AIDR events blocked
    height: 4
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
      | Vendor.status = blocked | count()
    end: now
    start: 1d
    width: 4
    options:
      default: {}
    visualization: single-value
    title: AIDR Blocked count
    isLive: false
    type: query
  9a555ada-e757-4e0f-b4ad-294276844053:
    x: 0
    y: 19
    description: 'Total number of identities (users, token names)'
    height: 4
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
      | count(field=Vendor.user_id, distinct=true)
    end: now
    start: 1d
    width: 4
    options:
      default: {}
    visualization: single-value
    title: Users - Total
    isLive: false
    type: query
  d5593247-8b3d-44da-ace0-3c9a048313e4:
    x: 5
    y: 0
    description: 'Events allowed/denied'
    height: 6
    queryString: "#repo=\"aidr\" event_type=\"AIDRPromptDataEvent\"\n| groupBy(Vendor.status) "
    end: '2025-12-12T00:46:00Z'
    start: '2025-12-12T00:45:00Z'
    width: 3
    options:
      cell-overflow: wrap-text
      column-overflow: truncate
      configured-columns: {}
      row-numbers-enabled: false
    visualization: table-view
    title: AIDR Allowed
    isLive: false
    type: query
  012d2794-4149-49dd-9ce9-679ed27c5e2f:
    x: 4
    y: 11
    description: Total number of AIDR events processed
    height: 4
    queryString: |-
      #repo="aidr"
      event_type="AIDRPromptDataEvent"
      | count()
    end: now
    start: 1d
    width: 4
    options:
      default: {}
    visualization: single-value
    title: Total AI Interactions
    isLive: false
    type: query
$schema: https://schemas.humio.com/dashboard/v0.23.0
```

- [Next-Gen SIEM](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem#next-gen-siem)
- [View event data](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem#view-event-data)
  - [Vendor.\* field reference](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem#vendor-field-reference)
  - [Example event log](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem#example-event-log)
- [View event metadata](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem#view-event-metadata)
- [Dashboards](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem#dashboards)
