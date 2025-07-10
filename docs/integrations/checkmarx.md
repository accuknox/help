---
title: Checkmarx (SAST, SCA, KICS, Container Scan) Integration with AccuKnox
description: Use Checkmarx SAST with AccuKnox to detect code flaws in CI/CD pipelines and enrich results with metadata for analysis.
---

# Checkmarx (SAST, SCA, KICS, Container Scan) Integration with AccuKnox

This integration fetches **SAST, SCA, KICS, and Container scan** results from **Checkmarx One** and sends them to **AccuKnox** to visualize and prioritize vulnerabilities across projects.

## Prerequisites

- Docker installed
- `.env` file created with the necessary variables (see below)

## Environment Variables

Below are the required variables to configure the integration:

### Checkmarx Variables

| Variable            | Description                                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `CX_API_KEY`        | API token to authenticate with Checkmarx One [Generate API Key](https://docs.checkmarx.com/en/34965-68618-generating-an-api-key.html) |
| `CX_PROJECT`        | Project filter (supports wildcards and exclusion)                                                                                     |
| `CX_PRIMARY_BRANCH` | `true` to consider only the primary branch of projects                                                                                |

#### `CX_PROJECT` Usage Guide:

- `{"*":"*"}` → All projects, all branches
- `{"*dvwa*":"*"}` → Only projects with _dvwa_ in the name, all branches
- `{"*dvwa*":"main"}` → Only projects with _dvwa_ in the name and branch = `main`
- `{-*dvwa*:"main"}` → Exclude projects with _dvwa_ in the name; only include `main` branch from others

### AccuKnox Variables

| Variable       | Description                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `AK_ENDPOINT`  | AccuKnox API endpoint (e.g., `https://cspm.demo.accuknox.com`)                                                           |
| `AK_LABEL`     | Label to tag the findings in AccuKnox UI [Create Labels](https://help.accuknox.com/how-to/how-to-create-labels/?h=label) |
| `AK_TENANT_ID` | Tenant ID in AccuKnox platform [Get Tenant ID](https://help.accuknox.com/how-to/how-to-create-tokens/?h=token)           |
| `AK_TOKEN`     | API token to authenticate with AccuKnox [Generate Token](https://help.accuknox.com/how-to/how-to-create-tokens/?h=token) |

## Sample `.env` file

```dotenv
CX_API_KEY=eyJhbGciOiJIUzUxMiIsInR5..................
CX_PROJECT={"*":"*"}
CX_PRIMARY_BRANCH=false
AK_ENDPOINT=https://cspm.demo.accuknox.com
AK_LABEL=cxprime
AK_TENANT_ID=123
AK_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tl...............
```

## Run the Integration

```bash
docker run --rm -it \
  --env-file .env \
  -v $PWD:/app/data/ \
  accuknox/checkmarx-one-job:1.4
```

![Integration Diagram](./images/checkmarx-sast/image1.png)

The script fetches results from Checkmarx One using the API key and project filter, then forwards them to AccuKnox for visualization and risk prioritization.

## Schedule the Scan with Cron (Optional)

To automate the Checkmarx and AccuKnox integration (e.g., every 30 minutes or daily), you can schedule it using a cron job on your system.

### 1. Create a Shell Script

Save the following script as `run_checkmarx.sh` in your project directory:

```bash
#!/bin/bash

cd /path/to/your/project

docker run --rm \
  --env-file .env \
  -v $(pwd):/app/data/ \
  accuknox/checkmarx-one-job:1.4
```

Replace `/path/to/your/project` with the absolute path to your working directory where the `.env` file is located.

Make the script executable:

```bash
chmod +x run_checkmarx.sh
```

### 2. Add a Cron Job

To run the scan automatically every 5 minutes:

Open your crontab:

```bash
crontab -e
```

Add this line to the bottom:

```bash
*/5 * * * * /path/to/your/project/run_checkmarx.sh >> /path/to/your/project/checkmarx_cron.log 2>&1
```

This schedules the scan every 5 minutes and logs the output to a file named `checkmarx_cron.log`.

You can change the schedule as needed. Examples:

- Every 5 minutes: `*/5 * * * *`
- Daily at 2 AM: `0 2 * * *`
- Weekly on Sunday at midnight: `0 0 * * 0`

### 3. Monitor the Output

To monitor the output of scheduled scans, check the log file:

```bash
tail -f /path/to/your/project/checkmarx_cron.log
```

### Tips

- Always use absolute paths in cron jobs (cron does not know your working directory).
- Ensure Docker can be run without `sudo` (or update the script accordingly).
- Make sure the `.env` file is valid and in the correct location.

## View Results in AccuKnox SaaS

To view the Checkmarx findings:

1. Navigate to the AccuKnox Console.
2. Go to **Issues > Findings**.
3. Select one of the following categories to view the identified vulnerabilities:
    - CX SAST
    - CX SCA
    - CX KICS
    - CX Containers

![AccuKnox Dashboard](./images/checkmarx-sast/image2.png)

## Notes

- Make sure your `.env` file does not contain trailing spaces or special characters that could break parsing.
- The `AK_LABEL` helps categorize data inside the AccuKnox dashboard (e.g., `cxprime`, `checkmarx-scan`). [Learn More](https://help.accuknox.com/how-to/how-to-create-labels/?h=label)
- To schedule this job, you can embed this in a CI/CD pipeline or cron job runner.
