> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sarif-ingestion.md).

# Ingest SARIF Data

Upload SAST data from third-party tools (for vendors that support SARIF output) to the Prisma Cloud platform using SARIF (Static Analysis Results Interchange Format) to analyze and remediate SAST issues directly within the platform. This feature is particularly useful for vendors that are not directly supported by Prisma Cloud. When SARIF data findings are uploaded, they are parsed to generate code weaknesses.

If you are using [Veracode](/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/veracode-ingestion.md), consider using the native ingestion feature instead. The native integration includes automatically pulling the data periodically and provides additional fidelity.

Prisma Cloud supports SARIF versions 2.0 and 2.1 and accepts `.zip`, `.json`, and `.sarif` files.

You can upload SARIF files through the Prisma Cloud platform or via the API.

1. Before you begin:
   * Permissions:
     * Grant **System Administrator** or **AppSec** privileges to users who need to view and upload SARIF results. Limit access to read-only for selected repositories by assigning the **Developer** role permissions to users who only need to view and analyze data in specific repositories without the ability to make changes
     * **GRBAC (Generic Role-Based Access Control)**: Viewing will require permissions for Projects > View and access to the selected repositories. Ingesting SARIF files will require permissions for Providers > Create or Update. Deleting old SARIF files will require permissions for Providers > Delete
   * Onboard the repository into the system before SARIF findings for that repository can be uploaded
   * Only upload findings relevant to the repository
   * Ensure that uploaded findings follow the standard SARIF specifications
   * Add the Prisma Cloud IP addresses and hostname for Application Security to an [allow list](/content-collections/get-started/console-prerequisites.md) to enable access to the Prisma Cloud console

## Ingest SARIF via the console

1. Export the required SARIF file from your third-party vendor to your host machine.
2. In Application Security, select **Repositories** > click on a repository > **Add SARIF Findings**.
3. Browse for and select the SARIF file from the displayed dialog box.

   The file is uploaded and the ingestion process begins (up to ten minutes depending on the size of the ingested data). Popups will notify you that the ingestion upload was successful and that the ingestion processing has begun.

## Ingest SARIF via the API

Ingest SARIF files via the API, enabling automation, such as in a CI/CD pipeline:

```curl
curl -X POST "{Prisma Cloud API URL}/code/api/v2/uploads/uploadSarifFile" \
     -H "Authorization: {Prisma Cloud generated token}" \
     -F "file=@{path/to/file.sarif};type=application/octet-stream" \
     -F "repositoryId={Repository ID}" \
     -F "fileName={file name}"
```

**Command properties breakdown**:

* **Prisma Cloud API URL**: Use your tenant API URL (for example, "<https://api3.prismacloud.io>"). For more information, refer to [Enable Access to the Prisma Cloud Console](/content-collections/get-started/console-prerequisites.md)
* **Prisma Cloud generated token**: Use the login endpoint to generate a JWT. Refer to [Prisma Cloud APIs - Login](https://pan.dev/prisma-cloud/api/cspm/app-login/) for more information
* **Repository ID**: Found in the header on the **Repositories** page or the response from the List Repositories List endpoint. Refer to [List Repositories List](https://pan.dev/prisma-cloud/api/code/get-repositories/) for more information

EXAMPLE

```curl
curl -X POST "https://api3.prismacloud.io/code/api/v2/uploads/uploadSarifFile" \
    -H "Authorization: {token}" \
    -F "file=@/Users/user/SARIF/output.sarif;type=application/octet-stream" \
    -F "repositoryId=ee1f4663-8ae6-4b87-a119-1ff75example" \
    -F "fileName=output.sarif"
```

## Example pipeline

The following is an example of a pipeline that scans every push to the main or master branch and sends the results to Prisma Cloud. Before you begin, set the following secrets as repository secrets in your secret management system for your CI pipelines (for example, for GitHub: Settings > Secrets and variables > Actions > Add secrets):

* **PRISMA\_URL**: Base URL for Prisma Cloud login and file upload
* **PRISMA\_USERNAME**: Your Prisma Cloud API ID
* **PRISMA\_PASSWORD**: Your Prisma Cloud API key
* **PRISMA\_REPO\_ID**: Your repository ID in Prisma Cloud

```yaml
name: Prisma Cloud Scan and Upload

on:
  push:
    branches:
      - main
      - master

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Install SAST Tool
        run: |
          pip install semgrep
          sudo apt-get update && sudo apt-get install jq -y

      - name: Run Scan
        run: |
          semgrep --config auto --sarif -o output.sarif

      - name: Upload to Prisma Cloud
        env:
          PRISMA_URL: ${{ secrets.PRISMA_URL }}
          PRISMA_USERNAME: ${{ secrets.PRISMA_USERNAME }}
          PRISMA_PASSWORD: ${{ secrets.PRISMA_PASSWORD }}
          PRISMA_REPO_ID: ${{ secrets.PRISMA_REPO_ID }}
        run: |
          # Authenticate with Prisma Cloud
          AUTH_RESPONSE=$(curl -L "$PRISMA_URL/login" \
                             -H 'Content-Type: application/json; charset=UTF-8' \
                             -H 'Accept: application/json; charset=UTF-8' \
                             -d '{
                                   "password": "'"${PRISMA_PASSWORD}"'",
                                   "username": "'"${PRISMA_USERNAME}"'"
                                 }')

          echo "AUTH_RESPONSE: $AUTH_RESPONSE"

          TOKEN=$(echo $AUTH_RESPONSE | jq -r '.token')
          MESSAGE=$(echo $AUTH_RESPONSE | jq -r '.message')

          echo "Token: $TOKEN"
          echo "Message: $MESSAGE"

          if [ -z "$TOKEN" ]; then
            echo "Error: Failed to retrieve token"
            exit 1
          fi

          # Upload SARIF file to Prisma Cloud
          UPLOAD_RESPONSE=$(curl -v -X POST "$PRISMA_URL/code/api/v2/uploads/uploadSarifFile" \
                          -H "Authorization: $TOKEN" \
                          -F "file=@./output.sarif;type=application/octet-stream" \
                          -F "repositoryId=$PRISMA_REPO_ID" \
                          -F "fileName=output.sarif")

          echo "Upload response: $UPLOAD_RESPONSE"
```

## Manage Code Weaknesses

To view and manage code weaknesses from ingested SARIF findings, refer to [Manage Third-Party Ingested Data](/content-collections/application-security/risk-management/monitor-and-manage-code-build/third-party-ingest-manage.md).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sarif-ingestion.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
