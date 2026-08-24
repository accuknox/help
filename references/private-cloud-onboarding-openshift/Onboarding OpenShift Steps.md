# Onboarding OpenShift Steps

# OpenShift VM Scanning: Onboarding Steps

## Prerequisites

1. A `VolumeSnapshotClass` object must exist in the customer's environment.
2. At least one `VolumeSnapshotClass` must be marked default.
3. All VMs on the cluster must use the same CSI driver (normally true by default anyway).
4. A prerequisite-check script/binary can be handed to the customer to validate this in their own cluster before onboarding.

## Step 1: Add AccuKnox to the Operator Catalog

1. Go to **Administration \> Cluster Settings \> Configuration**.
2. Search for "OperatorHub".
3. Open **OperatorHub \> Sources \> Create CatalogSource**.
4. Fill in:
    - Name: any (e.g. accuknox-scanner)
    - Display name: any
    - Publisher: any (e.g. accuKnox)
    - Tags: optional
    - Image: public.ecr.aws/k9v9d5v2/omni-operator-index:v0
5. Click **Create**.
6. Availability \> Select "Cluster-wide CatalogSource" ⚠️
7. Wait for status to show **Ready**. This confirms the catalog is added.

## Step 2: Install the Operator

1. Go to **Ecosystem \> Software Catalog**.
2. Search for the AccuKnox operator (now listed since the catalog was added).
3. Click **Install**, keep all defaults.
4. Confirm it shows up under **Installed Operators** once done.

## Step 3: Set Up Token, Label, and Secret

1. In the AccuKnox UI, go to **Settings \> Tokens** and create a token.
2. In the AccuKnox UI, go to **Settings \> Labels and**  create a label. The same label name is reused in the scan schedule config later.
3. Note the tenant ID (readable from the JWT token). ⚠️
4. In OpenShift, go to **Workloads \> Secrets \> Create Secret** **\> Key/Value secret**
    - Secret name: any (e.g. Omni)
    - Key: any (e.g. test-token)
    - Value: Add the token created in step 3.1
    - Note the Namespace (e.g. `openshift-operators`)⚠️

## Step 4: Create the Scan Schedule

1. Go to the installed operator, open the **Schedule** tab, click **Create Instance**.
2. Fill in:
    - Name: any
    - Labels (optional): to scan only specific VMs, add labels matching those VMs. You can create multiple schedulers with different labels to scan different VM sets on different schedules.⚠️⚠️
    - Endpoint: where scan results get sent, format looks like `<https://cspm.<domain>>/api/v1/artifact` ⚠️ (confirm exact URL)
    - Label: same label created in Step 3.2
    - Tenant ID: from Step 3.3
    - Secret key: same key created in Step 3.4
    - Secret name: same name used in Step 3.4 (e.g. Omni)
    - cronJobNamespace: same namespace as the Secret in Step 3.4 (e.g. `openshift-operators`)
    - Schedule: Schedule exact cron expression of when to run the scan. This can be edited later
    - Concurrency: Defines the number of scans running at once.
    - Template \> Cluster name, any value. This will be used as asset name for scan findings on the Accuknox platform
    - Time zone: Any available time zone. Case sensitive with regards to the time zone database
3. Click **Create**.

## Uninstall Steps

1. Go to **Installed Operators**, select the AccuKnox operator, click **Uninstall**.
2. To also remove it from the catalog: go to **Cluster Settings \> Configuration \> OperatorHub \> Sources** and remove the catalog source there.
