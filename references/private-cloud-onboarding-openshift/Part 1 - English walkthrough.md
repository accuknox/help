# Part 1 recording, English walkthrough

Source: `Part 1.mp4` (24:48) and `Part 1.srt`. The demo is spoken in Hindi. This is the
English content, condensed to what is actually demonstrated. Timestamps point at the
video. Presenter is Murtaza (Surya Tyagi's Meet account), with Pavan and Ayush on the call.

The demo is a Google Meet screen share, so the OpenShift console occupies a small window
inside a 1920x1080 frame and a self-view thumbnail covers the lower right of the shared
screen for the first four minutes. Screenshots in the help doc are cropped and upscaled
around that.

## 00:00 to 01:45, prerequisites

The only capability being offered right now is VM scanning for VMs sitting on the Red Hat
OpenShift platform. Before onboarding, the customer environment needs:

- A `VolumeSnapshotClass` resource available in the cluster.
- One of the available `VolumeSnapshotClass` objects marked default.
- All VMs on the cluster using the same CSI driver. Murtaza notes this is normally true
  anyway, since nobody installs two storage solutions for the same thing.

He offers to provide a script or a binary, hosted somewhere like S3, that the customer runs
against their own cluster and that reports whether the prerequisites are met. That artifact
does not exist yet.

## 01:45 to 02:35, why the catalog step exists

The solution is operator based, so the operator has to be installed. OpenShift lists
operators under **Ecosystem → Software Catalog**, and installed ones under **Installed
Operators**. The AccuKnox operator is not in the Software Catalog by default, so it has to
be added to the catalog first.

Path shown: **Administration → Cluster Settings → Configuration**, search OperatorHub, open
**Sources**, click **Create CatalogSource**.

## 02:35 to 03:30, create the catalog source

Fields filled on screen:

- CatalogSource name: `accuknoxscanner` (any value)
- Display name: `accuknox_scanner` (any value)
- Publisher name: `accuknox` (any value)
- Image URL: `public.ecr.aws/k9v9d5v2/omni-operator-index:v0`
- Availability: Cluster-wide CatalogSource

Then **Create**.

## 03:30 to 04:10, wait for READY

The new source appears in the Sources list. It shows `TRANSIENT_FAILURE` briefly, then
`READY`. Once it is READY the catalog is added and the operator shows up in the Software
Catalog.

## 04:10 to 05:35, install the operator

Search `accuknox` in the Software Catalog. The tile **AccuKnox VM Scanning**, provided by
AccuKnox Inc., appears. Click it, click **Install**. Every default on the Install Operator
page is kept, including the namespace. Click **Install**.

The recording sits on the installing screen for about 70 seconds. Once done, the operator
appears under **Installed Operators**.

## 05:35 to 06:35, start the schedule

Open the operator, go to the **Schedule** tab, click **Create Instance**. Murtaza recaps
the flow so far: list the operator in the catalog, install it in one click, then create a
schedule.

Fields:

- Name: anything, he uses `scanner`.
- Labels: if you want to scan only particular VMs, put labels here that match those VMs.
  Multiple schedulers can be created, each with its own labels, so different sets of VMs
  get scanned on different schedules. For a general scan, leave it empty.

## 06:35 to 07:10, endpoint

`endpoint` is where scan results are sent. He types
`https://cspm.demo.accuknox.com/api/v1/artifact/`.

## 07:10 to 08:25, token and label in the AccuKnox UI

He switches to the AccuKnox platform, goes to Settings, and creates a token, then creates a
label. The label created in the AccuKnox UI is the same label that goes into the schedule.
He names both around `openshift`.

## 08:25 to 08:55, tenant ID

The `tenantID` field needs the AccuKnox platform tenancy ID. He obtains it by pasting the
JWT into a JWT decoder and reading the claims, which include the tenant ID. He reuses the
tenant ID from an older token since it is the same tenant.

## 08:55 to 10:50, create the secret

The token is not pasted into the schedule directly. It goes into a Kubernetes secret that
the schedule then references.

Path: **Workloads → Secrets → Create → Key/value secret**.

- Secret name: `omni`
- Key: `token`
- Value: the token pasted in

He initially creates it in the `default` project, then redoes it in the
`openshift-operators` namespace so it matches where the operator was installed. He repeats
that the same namespace has to be used for `cronJobNamespace`.

## 10:50 to 12:10, schedule, timezone, template

- `timeZone`: any value, case sensitive against the tz database. He uses `Asia/Kolkata`.
- Concurrency: how many scans run at once. He leaves it at 1 for the demo.
- `schedule`: a cron expression. It is 16:45 during the demo so he sets `50 16 * * *`, then
  later edits it to `48 16 * * *` to trigger sooner. He notes the schedule can be edited
  from the UI at any time with no reinstall.
- `template → clusterName`: any value, this is what shows as the asset name in the AccuKnox
  UI. He uses an `openshift`/`omni` style name.

Everything else is left at defaults. Click **Create**.

## 12:10 to 12:30, the VM under test

One VM exists, in the `default` namespace. He says the namespace does not matter, a VM can
be in any namespace. The schedule shows phase `Awaiting`.

## 12:30 to 13:20, editing the schedule

He edits the cron expression down to a minute away so the demo does not have to wait, and
confirms this is editable from the UI.

## 13:20 to 14:15, how the scan actually works

There is an operator and there is a scheduler. At the scheduled time the scheduler starts a
pod. That pod discovers every VM available inside the virtualization environment. For each
discovered VM it creates a volume snapshot. It then scans that snapshot, sends the result to
the SaaS, and deletes the resources it created.

## 15:10 to 16:30, the scan running

Discovery completes. A snapshot appears, visible in the PVC list. A second pod starts, the
PVC is attached to it, and that pod runs the scan and sends the result to the SaaS.

## 16:30 to 18:50, side conversation

Not product content. Recording confirmation, a noisy VM server Rahul has been complaining
about, and small talk.

## 18:50 to 19:30, scan complete

The scan status reads **Completed**. It will run again tomorrow per the configured cron, or
the schedule can be edited at any time from the UI.

## 19:30 to 20:20, results reaching the platform

They log in to the CSPM side and see `storing data`, meaning the artifact was received. The
asset ID reflects the cluster name and the label set earlier.

## 20:20 to 21:00, adding and removing VMs

Question from Pavan: if a new VM is added, does anything need to change? No. The next
schedule run rediscovers the available VMs, so the count can go up or down and nothing has
to be reconfigured. Discovery is always fresh.

To scan a particular VM on one cadence and another VM on a different cadence, create
multiple schedulers and control which VMs each one picks up with matching labels.

## 21:00 to 22:40, transfer time

A 30 MB artifact file is being stored. They estimate one to two minutes for it to land.

## 23:10 to 24:00, uninstall

Same path as install. Go to Installed Operators and uninstall it in a single click. To also
remove it from the catalog, go to **Cluster Settings → Configuration → OperatorHub →
Sources** and delete the catalog source. That cleans it up.

## 24:00 to end

Cut off mid-question from Ayush about two types of status. Nothing further demonstrated.
