# OpenShift onboarding, things to confirm before the doc goes public

Raised while writing `docs/how-to/vm-security/agentless/openshift-vm-scanning.md` from
`Onboarding OpenShift Steps.md`, `Part 1.mp4`, and `Part 2.mp4`. Nothing here blocks
publishing the page, but items 1 to 4 change what the doc tells a customer to do.

## 1. How does a customer find their tenant ID

The steps doc says "Note the tenant ID (readable from the JWT token)". In the recording the
tenant ID is obtained by pasting the JWT into a public JWT decoder and reading the claims.

We cannot ship that instruction. It tells customers to paste a live credential into a third
party website. Either the tenant ID is visible somewhere in the AccuKnox UI and the doc
should point at that screen, or the schedule should read it from the token the way the
prototype implies it does. Right now the doc says "ask AccuKnox support if you are not
sure", which is a placeholder.

## 2. The artifact endpoint URL

Steps doc: `https://cspm.<domain>/api/v1/artifact`, flagged "confirm exact URL".
Recording: `https://cspm.demo.accuknox.com/api/v1/artifact/`, with a trailing slash.
Rest of help docs, for the SaaS tenant: `https://cspm.accuknox.com/api/v1/artifact/`.

The doc currently uses `https://cspm.accuknox.com/api/v1/artifact/`. Confirm the trailing
slash is required or at least harmless, and confirm what onprem customers should use.

## 3. Two different fields both called "label"

The Create Schedule form has a top-level `Labels` field, placeholder `app=frontend`, and a
separate `artifactAPI → label` field. The steps doc describes the first one as "to scan only
specific VMs, add labels matching those VMs".

The form also has a `vmSelector` field, described in the console as a label query over VMs,
which sounds like the field that actually restricts which VMs get scanned. `Labels` at the
top of a form generated from a CRD is normally just metadata labels on the Schedule object
itself.

Which field restricts the VM set, `Labels` or `vmSelector`? The doc currently says "give
each schedule a VM label selector" without naming the field, so it is not wrong, just vague.
Please confirm and I will name the field and add the exact syntax.

## 4. Uninstall leaves resources behind

The steps doc says uninstall the operator, then delete the catalog source. Removing an
operator through OLM does not delete the custom resources it created, so the Schedule
instances and the secret survive.

The doc now tells customers to delete the Schedule instances first, then uninstall, then
delete the secret. Confirm that order is right, and whether any other resource needs
cleaning up (leftover snapshots or PVCs if a scan was interrupted mid-run).

## 5. Ordering error in the source steps

Step 1 of the source doc lists "Click Create" as item 5 and "Availability, select
Cluster-wide CatalogSource" as item 6. In the console, Availability is a radio button on the
form, before Create, and Cluster-wide is already the default. The doc has this in the right
order now.

## 6. Console navigation is version specific

The recording shows OpenShift 4.22 with **Ecosystem → Software Catalog**. Older OpenShift
versions call this **Operators → OperatorHub**. Do we need to state a minimum OpenShift
version on the page, or add the older path as an aside?

## 7. Fields present in the UI but missing from the steps doc

`scansHistoryLimit` (defaults to 3), `namespaceSelector`, `vmSelector`, and under `template`
a `claims` list and a `skipMalwareScan` toggle. I documented `scansHistoryLimit` and left
the rest out. Should `skipMalwareScan` be surfaced, given the description says malware
scanning is CPU intensive and disabled by default?

## 8. The prerequisite check script

Mentioned in the recording at 01:20, a script or binary customers run to validate the
`VolumeSnapshotClass` and CSI driver prerequisites before onboarding. Does not exist yet. If
it ships, the Prerequisites section of the doc should link to it rather than listing manual
checks.

## 9. Time to first findings

The meeting notes say roughly 10 minutes from onboarding to findings landing in the app, and
that the UI should show a loading state rather than an empty findings view during that
window. The doc says "allow roughly 10 minutes from the end of the scan", and the prototype
now has a waiting screen for exactly this. Confirm the number and whether the clock starts
at schedule creation or at scan completion.

## 10. Part 2 recording

`Part 2.mp4` is 2:23 and shows the findings view in the AccuKnox platform, not the
uninstall flow. The uninstall flow is at 23:10 in `Part 1.mp4` and is verbal, with the
Installed Operators and Sources screens visible. If a dedicated offboarding recording exists
somewhere, it did not come through.
