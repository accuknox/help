For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/import-export-individual-rules.md).

Prisma Cloud lets you import and export rules from one Console to another. Every rule created in Prisma Cloud under the **Defend** section has copy and export buttons in the **Actions** menu. An import button is located at the bottom of every rule table.

## Copying rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/import-export-individual-rules\#copying-rules)

To copy a rule:

1. Go to **Defend > Runtime > {Vulnerabilities \| Compliance \| Access}**.

2. Click **Actions > Copy** for the rule you want to copy.











A dialog box named **Edit copy of….** opens.

3. Make any desired changes to the copied rule.

4. Click **Save**.


## Exporting rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/import-export-individual-rules\#exporting-rules)

Click **Actions > Export** next to any rule to export it in json format.

**Example**

AskCopy

```
{
  "name": "Default - ignore Prisma Cloud components",
  "owner": "system",
  "modified": "2017-05-31T20:47:21.573Z",
  "effect": "alert",
  "resources": {
    "hosts": [\
      "*"\
    ],
    "images": [\
      "docker.io/twistlock/private:console*"\
    ],
    "labels": [\
      "*"\
    ],
    "containers": [\
      "twistlock_console"\
    ],
    "services": []
  },
  .
  .
  .
}
```

## Importing rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/import-export-individual-rules\#importing-rules)

A rule can be imported into Console in JSON format. To capture a rule in JSON format, use the export function described above.

[PreviousCustom runtime rules](https://docs.prismacloud.io/admin-guide/runtime-defense/custom-runtime-rules) [NextATTACK explorer](https://docs.prismacloud.io/admin-guide/runtime-defense/attack)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
