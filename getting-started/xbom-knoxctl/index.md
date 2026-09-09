---
title: Generate xBOM via knoxctl
description: Use the local knoxctl UI to generate SBOM, CBOM, and AIBOM files and push results to your AccuKnox tenant.
---

# Generate xBOM via knoxctl

Use the `knoxctl` local UI to interactively scan filesystems, container images, and AI/ML models, then push results directly to your AccuKnox tenant.

**Prerequisites:**

- `knoxctl` binary installed on your system
- AccuKnox project, labels, and access key created — see [Common Prerequisites](xbom-setup.md#common-prerequisites)

!!! note
    Windows-specific installation steps for `knoxctl` are not documented on this page. Use the official [knoxctl documentation](https://help.accuknox.com/knoxctl/) and [GitHub repository](https://github.com/accuknox/accuknox-cli-v2) to get the current installation method and binaries.

---

## Step 1: Run knoxctl

Open your terminal and verify the installation:

```bash
./knoxctl.exe -h
```

![knoxctl help output](images/xbom/image025.png)

This displays all available commands and options.

## Step 2: Launch the knoxctl UI

Start the local UI server:

```bash
./knoxctl.exe ui
```

The UI will be available at:

- [http://localhost:10100/](http://localhost:10100/)
- [http://127.0.0.1:10100](http://127.0.0.1:10100)

Open either URL in your browser.

![knoxctl UI](images/xbom/image027.png)

## Step 3: Configure BOM Settings

In the knoxctl UI:

1. Navigate to **BOM Settings**.
2. Add the following configuration:

    - **Control Panel URL:** `https://cspm.accuknox.com`
    - **API Token:** Paste the access key you created in the prerequisites step.

3. Click **Save Settings**.

    ![Save BOM Settings](images/xbom/image029.png)

## Step 4: Sync Projects and Labels

1. Click **Refresh** for projects and labels.
2. The UI will display all projects available on your tenant.
3. All associated labels will be visible.

    ![Sync projects and labels](images/xbom/image031.png)

---

## Generate BOM Files

After completing the setup steps above, you can generate different types of BOM files.

**Options available in all BOM types:**

- **Sign artifact with cosign (ECDSA P-256):** Optional checkbox to cryptographically sign the generated BOM.
- **CLI Preview:** The UI displays the equivalent `knoxctl` command for your configuration — useful for automation.

### SBOM (Software Bill of Materials)

In the knoxctl UI:

1. Navigate to **Software Bill**.
2. Configure the following settings:

    - **Source:** Path to your project folder
    - **Output Scheme:** Select the output schema
    - **Exclude Pattern:** (Optional) Add any patterns to exclude

3. Click **Generate SBOM**.

    ![Generate SBOM](images/xbom/image033.png)

4. Download the generated file from the interface.
5. The generated SBOM will also appear in the UI under **SBOM** > **Projects** > [Your Project Name].

    ![SBOM in dashboard](images/xbom/image035.png)

### CBOM (Cryptographic Bill of Materials)

CBOM can be generated for either filesystem projects or container images.

In the knoxctl UI:

1. Navigate to **Software Bill**.
2. Select **Source Code** as the scan type.
3. Configure the following settings:

    - **Source Path:** Path to your project folder
    - **Project Name:** (Optional) Name of your project
    - **Group / Module:** (Optional) Specify group or module
    - **Version:** (Optional) Project version

4. Click **Generate CBOM**.

    ![Generate CBOM](images/xbom/image037.png)

5. Download the generated file from the interface.
6. The generated CBOM will also appear in the UI under **SBOM** > **Projects** > [Your Project Name].

### AIBOM (AI Bill of Materials)

#### Option 1: Hugging Face Model Scanning

In the knoxctl UI:

1. Navigate to **Software Bill**.
2. Select **Hugging Face** as the source type.
3. Configure the following settings:

    - **Model Identifier:** Format: `owner/model-name` (e.g., `meta-llama/Llama-2-7b`)
    - **API Token:** (Optional) Hugging Face API token
    - **Override Name:** Custom name for the model
    - **Override Version:** Custom version identifier
    - **Manufacturer:** Model manufacturer/creator

4. Click **Generate AIBOM**.

    ![Generate AIBOM - Hugging Face](images/xbom/image039.png)

5. Download the generated file from the interface.
6. The generated AIBOM will also appear in the UI under **SBOM** > **Projects** > [Your Project Name].

#### Option 2: AWS Bedrock Model Scanning

In the knoxctl UI:

1. Navigate to **Software Bill**.
2. Select **AWS Bedrock** as the source type.
3. Configure the following settings:

    - **AWS Region:** `us-east-1` (or your preferred region)
    - **Model ID Filter:** (Optional) Leave blank for all models
    - **Credentials:** Choose one of the following:

        - **Use Default Credential Chain** (if AWS credentials are already configured in your terminal)
            - Default chain: env vars → `~/.aws/credentials` → IAM role
        - **Custom Keys:**
            - Access Key ID
            - Secret Access Key
            - Session Token: (Optional) Temporary session token

    - **Override Name:** Leave blank to use model ID
    - **Override Version:** Leave blank for git SHA
    - **Manufacturer:** Override manufacturer name

4. Click **Generate AIBOM**.

    ![Generate AIBOM - AWS Bedrock](images/xbom/image041.png)

5. Download the generated file from the interface.
6. The generated AIBOM will also appear in the UI under **SBOM** > **Projects** > [Your Project Name].
