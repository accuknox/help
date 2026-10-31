[Skip to content](https://help.accuknox.com/getting-started/dspm-overview/#data-security-posture-management)

Copy page

Copy page

Copy page as Markdown for LLMs

View as Markdown ↗

View this page as plain text

Open in ChatGPT ↗

Ask questions about this page

Open in Claude ↗

Ask questions about this page

# Data Security Posture Management [¶](https://help.accuknox.com/getting-started/dspm-overview/\#data-security-posture-management "Permanent link")

AccuKnox Data Security Posture Management (DSPM) finds sensitive data in your buckets, databases and SaaS apps, and shows where it sits. The scanner runs on a machine you own, in the region that holds the data. It reads a sample with read-only access, classifies it in memory, and sends only a findings file to the AccuKnox console. To set up the scanner, see [Onboard the DSPM Scanner](https://help.accuknox.com/getting-started/dspm-onboarding/).

## Product Tour [¶](https://help.accuknox.com/getting-started/dspm-overview/\#product-tour "Permanent link")

Watch the two-minute tour of AccuKnox DSPM.

AccuKnox DSPM - Find Sensitive Data in Your Cloud - YouTube

Tap to unmute

[AccuKnox DSPM - Find Sensitive Data in Your Cloud](https://www.youtube.com/watch?v=8foYZBdQtDQ) [AccuKnox](https://www.youtube.com/channel/UCLqK0vGQTa2ctjnbNzvP52Q)

AccuKnox735 subscribers

[Watch on](https://www.youtube.com/watch?v=8foYZBdQtDQ)

[Risk](https://help.accuknox.com/getting-started/dspm-overview/#__tabbed_1_1)[Regions](https://help.accuknox.com/getting-started/dspm-overview/#__tabbed_1_2)[Connect S3](https://help.accuknox.com/getting-started/dspm-overview/#__tabbed_1_3)[Findings](https://help.accuknox.com/getting-started/dspm-overview/#__tabbed_1_4)[Evidence](https://help.accuknox.com/getting-started/dspm-overview/#__tabbed_1_5)[Assets](https://help.accuknox.com/getting-started/dspm-overview/#__tabbed_1_6)

![The DSPM risk overview dashboard with data alerts by severity, findings trends, the top 10 data findings, the top assets and accounts with findings, open tickets, and data distribution by store type](https://help.accuknox.com/getting-started/images/dspm/preview/dspm-proto-dashboard-risk.png)

- Data alerts by severity, and findings trends over time.
- The top 10 data findings, and the assets and accounts with the most findings.
- Open tickets, and the spread of data across store types.

![Sensitive data findings ranked by country, with the same counts plotted on a world map](https://help.accuknox.com/getting-started/images/dspm/preview/dspm-proto-dashboard-region.png)

- Findings ranked by the country that holds the data.
- The same counts plotted on a world map.

![The S3 source settings, which include buckets by tag or by name pattern, scan every publicly exposed bucket, and let AccuKnox AI review results for false positives](https://help.accuknox.com/getting-started/images/dspm/preview/dspm-proto-configure-s3.png)

- Pick the buckets to scan by tag or by name pattern.
- Scan every publicly exposed bucket.
- Let AccuKnox AI review the results for false positives.

![The Data Security findings list, grouped by finding name, with the impacted assets, their status and sensitive record counts](https://help.accuknox.com/getting-started/images/dspm/preview/dspm-proto-findings-list.png)

- Findings grouped by name, such as an access key in plain text.
- The impacted assets, their status and the sensitive record count for each finding.

![The evidence tab of a finding, with each file behind the finding, its type, path and the sensitive data types found in it](https://help.accuknox.com/getting-started/images/dspm/preview/dspm-proto-finding-evidence.png)

- Each file behind the finding, with its type and path.
- The sensitive data types found in each file.

![The overview of a data asset, with total risks, sensitive records by data type, tags, file types, and security configuration such as encryption and public access](https://help.accuknox.com/getting-started/images/dspm/preview/dspm-proto-asset-overview.png)

- Total risks, and sensitive records by data type.
- Tags and file types in the asset.
- Security configuration, such as encryption and public access.

## Architecture [¶](https://help.accuknox.com/getting-started/dspm-overview/\#architecture "Permanent link")

![The AccuKnox DSPM platform connects to AWS, Azure and Google Cloud, Kubernetes environments, SaaS data sources, and on-premises databases and file systems, and runs data discovery, data classification and data security controls](https://help.accuknox.com/getting-started/images/dspm/integration-ecosystem-dspm.webp)

## How the Scanner Works [¶](https://help.accuknox.com/getting-started/dspm-overview/\#how-the-scanner-works "Permanent link")

| Item | Detail |
| --- | --- |
| Access | Read-only. The scanner code has no write path |
| Where it runs | A VM or a Kubernetes job in your cloud account, in the region that holds the data |
| What it reads | Up to 10,000 rows or documents per table or collection, and files up to 100 MB |
| What leaves | One findings file per data store, sent to the AccuKnox console over HTTPS |
| Schedule | Nightly, per data store |

Your cloud account, one regionDSPM scannerVM or Kubernetes CronJobRuns nightlyRead-only accessNo inbound portsRead-onlyRead-only roleRole assignmentData in this accountOther AWS accountsOther Azure subscriptionsFindings, HTTPS 443Image pull, HTTPS 443AccuKnox consoleContainer registry

Nothing connects inbound to the scanner. Each region gets its own scanner.

Your cloud account, one regionDatabasesObject storesSaaS appsParse filesCSV, Excel, ParquetJSON, PDF, OfficeArchives, OCRClassify in memory159 detectors62 country packsConfidence per findingFindings fileRows stream inHTTPS, findings onlyAccuKnox console

Database rows never touch disk. Parsed files sit in memory-backed scratch space until the run ends.

Deployment options

| Deployment | Use it when | How it runs |
| --- | --- | --- |
| VM with systemd timers | The default for most teams | One timer per data store starts one short-lived container each night |
| Kubernetes CronJob | You already run EKS or AKS | The same image on a schedule, with IRSA or workload identity as the credential |
| Event-driven function | You want new objects scanned as they land | An AWS Lambda handler scans one object or table per event from S3 notifications, SQS or DynamoDB streams |

Each data store gets its own instance, which is one environment file. S3 gets one instance per AWS account, Blob Storage one per storage account, and a database one per server. A failure in one instance never touches another.

The container runs with a read-only root filesystem, all Linux capabilities dropped and no privilege escalation.

## Supported Data Stores [¶](https://help.accuknox.com/getting-started/dspm-overview/\#supported-data-stores "Permanent link")

| Asset type | AWS | Azure | Self-managed | SaaS |
| --- | --- | --- | --- | --- |
| Object storage | S3 | Blob Storage, ADLS Gen2 |  | Google Drive |
| Relational databases | RDS and Aurora for PostgreSQL, MySQL, MariaDB and SQL Server | Azure Database for PostgreSQL and MySQL, Azure SQL Database and Managed Instance | PostgreSQL, MySQL, MariaDB, SQL Server |  |
| Document and key-value databases | DocumentDB, DynamoDB (event-driven mode) | Cosmos DB for NoSQL and for MongoDB | MongoDB |  |
| SaaS applications |  |  |  | Google Workspace Drive, Salesforce |
| Secret stores for database passwords | Secrets Manager | Key Vault |  |  |

Not supported

Google Cloud Storage, SMB or NFS file shares, Oracle Database, and data warehouses such as Snowflake.

What the scanner reads in each data store

| Data store | What the scanner reads |
| --- | --- |
| Amazon S3 | Every object in the bucket. Files up to 100 MB, archives unpacked |
| Azure Blob Storage, ADLS Gen2 | Every blob in the container. Archive-tier, page and soft-deleted blobs are skipped |
| PostgreSQL, MySQL, MariaDB, SQL Server, including RDS, Aurora and Azure | All non-system schemas, up to 10,000 rows per table |
| MongoDB, Amazon DocumentDB | All non-system collections, up to 10,000 documents each, nested fields included |
| Amazon DynamoDB | Tables, up to 10,000 items. Event-driven mode only |
| Cosmos DB for NoSQL | Every container of the database, up to 10,000 items each |
| Cosmos DB for MongoDB | Same as MongoDB. Request-rate throttling is retried |
| Google Workspace Drive | A user's My Drive or a shared drive. Docs, Sheets and Slides are exported and read |
| Salesforce | Every business object with records, text fields, and the files attached to records |

**File formats.** CSV and TSV, Excel workbooks sheet by sheet, Parquet, JSON and JSON Lines, XML, PDF, Word, PowerPoint, images through OCR, and zip, tar, gz and bz2 archives unpacked recursively. The scanner reads any other format as plain text.

## What the Scanner Detects [¶](https://help.accuknox.com/getting-started/dspm-overview/\#what-the-scanner-detects "Permanent link")

The scanner ships 283 data classes. Each finding carries a confidence tier, and the console receives findings at or above the confidence floor you set. The default floor is Likely.

| Confidence tier | Meaning | Example |
| --- | --- | --- |
| Very likely | A validated shape plus corroboration | A checksum-valid national ID in a column named for it |
| Likely | One strong signal | A valid email, or a card number with a valid checksum |
| Possible | A plausible shape only | Nine digits in SSN groups. Never reported on its own |

Data classes by category

| Category | Data classes | Examples |
| --- | --- | --- |
| Regional compliance | 117 | US SSN and ITIN, Indian Aadhaar, PAN and GST, UK National Insurance number, Spanish DNI and NIE, Canadian SIN. Each is checked with its public check-digit algorithm where one exists |
| Credentials and secrets | 114 | AWS access and secret keys, Azure storage keys and SAS tokens, GCP service account keys, tokens from GitHub, Slack, Stripe, OpenAI and more than 50 other vendors, JWTs, private key headers, password hashes |
| Healthcare data (PHI) | 21 | NHS number, US Medicare beneficiary ID, NPI and DEA numbers, claim and prescription numbers, medical record numbers, ICD-10 and NDC codes |
| PII | 19 | Email, phone numbers, person names, street addresses, dates of birth, public IP addresses, IMEI, VIN, passport machine-readable zones |
| Financial data | 10 | Payment card numbers by issuer prefix and checksum, IBAN, SWIFT/BIC, bank account and ABA routing numbers, cryptocurrency wallet addresses |
| Entropy-based secret | 1 | Random-looking tokens with supporting evidence. Off by default |
| Technical identifier | 1 | UUIDs. Shipped disabled |

The catalogue labels 226 data classes Restricted, 29 Confidential and 28 Internal. It rates 165 Critical, 63 High, 23 Medium, 29 Low and 3 Lowest.

The 62 country packs

AE, AR, AT, AU, BE, BG, BR, CA, CH, CL, CN, CZ, DE, DK, EE, EG, ES, FI, FR, GB, GH, GR, HK, HR, HU, ID, IE, IL, IN, IS, IT, JP, KR, LK, LT, LU, LV, MX, MY, NG, NL, NO, NZ, PH, PK, PL, PT, RO, RS, RU, SA, SE, SG, SI, SK, TH, TR, TW, UA, US, VN and ZA.

Enable the packs for the countries you operate in. The same list decides which national phone-number formats the scanner recognises. Generic detectors such as email, cards, IBAN, secrets and IP addresses always run.

The scanner never reports documented example keys, test card numbers, epoch timestamps, or values on your allow list.

## Compliance Mapping [¶](https://help.accuknox.com/getting-started/dspm-overview/\#compliance-mapping "Permanent link")

282 of the 283 data classes carry the regulation clauses they fall under. Filter findings by a framework in the console to list the assets that hold data under that framework. The scanner shows where regulated data sits. It does not assess the controls around that data.

Frameworks and data classes

| Framework | Data classes | What it covers |
| --- | --- | --- |
| GDPR (EU) | 78 | National identifiers of EU member states, contact details, dates of birth, health and financial identifiers. Cited to Articles 4, 9 and 32 |
| UK GDPR and Data Protection Act 2018 | 12 | National Insurance number, NHS number, UK passport and driving licence, UTR, sort code |
| PCI DSS v3.2.1 and v4.0 | 107 | Card numbers under Requirements 3.4 and 3.5.1. Credential and key classes under Requirements 3.6, 3.7 and 8.3 |
| HIPAA and HITECH | 26 | Health identifiers, member, claim and prescription numbers, plus SSN, date of birth and account numbers under 45 CFR 164.514(b)(2) |
| CPRA and CCPA (California) | 21 | SSN, cards, bank accounts, contact details, health identifiers |
| GLBA, FTC Safeguards and US state breach-notification laws | 12 | SSN, ITIN, EIN, alien registration number, bank account, routing and SWIFT numbers |
| India DPDP Act 2023 and SPDI Rules 2011 | 17 | Aadhaar, PAN, GST, passport, financial information, passwords |
| South Africa POPIA | 9 | ID number, passport, driver licence, traffic register number, phone numbers |
| Korea PIPA | 4 | Resident and foreigner registration numbers, driver licence, passport |
| Canada PIPEDA | 3 | SIN, postal code, OHIP number |
| Australia and New Zealand Privacy Acts | 6 | TFN, Medicare, IHI, BSB, IRD, NHI |
| Philippines Data Privacy Act | 6 | UMID, TIN, passport, mobile numbers |
| Nigeria and Ghana Data Protection Acts | 3 | NIN, vehicle registration, Ghana Card |
| Argentina Ley 25.326 and Chile Ley 19.628 | 4 | CUIT, DNI, RUT |
| Germany SGB V | 2 | Physician and practice numbers |
| NIST SP 800 series, OWASP, CIS AWS Foundations Benchmark, SOC 2 | 110 | Every credential and secret class: cloud keys, vendor tokens, private keys, password hashes |

Each data class also cites its CWE weaknesses and MITRE ATT&CK techniques. Coverage follows the country packs you enable.

## Data Privacy [¶](https://help.accuknox.com/getting-started/dspm-overview/\#data-privacy "Permanent link")

The scanner discards every row and file after classification. The findings file holds each matched value cut at 200 characters, and the console shows that value masked to its last four characters.

Security details

| Question | Answer |
| --- | --- |
| What access does the scanner hold? | Read-only grants only. The code has no path that writes to, deletes from or changes a data store |
| Where does classification happen? | On the VM or cluster in your account. The language model for names runs inside the container. No data goes to an external service |
| What leaves your account? | One zipped findings file per data store, uploaded over HTTPS with a bearer token |
| What is in a finding? | The data type, category, confidence, evidence, location, occurrence count, a hash of the value, and the matched value cut at 200 characters |
| What stays on the VM? | The findings file, in a root-owned directory, removed after 30 days. Downloaded files are gone when the run ends |
| How are credentials handled? | Platform identity where possible: instance role, managed identity, workload identity, Entra tokens. A required password sits in a root-only file, Key Vault or Secrets Manager. Logs redact SAS tokens and account keys |
| Does data cross regions? | No. The AWS role denies other regions by condition. On Azure, storage firewalls and role scopes limit the scanner to its region |
| How is the image updated? | You pin an image tag. Each run pulls that tag when the registry is reachable and runs the cached image when it is not. You can mirror the image into your own registry |

## Run the Console On-Premises [¶](https://help.accuknox.com/getting-started/dspm-overview/\#run-the-console-on-premises "Permanent link")

AccuKnox can run the scanner, the findings and the console together on-premises or air-gapped. With the on-premises console, nothing leaves your boundary.

Inside your boundaryOutside your boundaryTypical SaaS DSPMData storesScannerFindings, metadataVendor SaaSAccuKnox DSPMData storesScannerAccuKnox consoleNothing leaves

How other DSPM vendors deploy

|  | AccuKnox DSPM | Cyera | Varonis | BigID | IBM Guardium DSPM |
| --- | --- | --- | --- | --- | --- |
| Where scanning runs | A VM or CronJob you own, in the data's region | Cyera's cloud, or an outpost cluster in your cloud | Collectors in your environment, analysis in Varonis SaaS | Cloud scanners, or local scanners in your environment | An analyzer in your cloud account, per region |
| Where the console lives | AccuKnox SaaS, or on-premises or air-gapped | Cyera SaaS | Varonis SaaS | BigID SaaS, or self-hosted on your Kubernetes | IBM SaaS |
| What leaves your environment | Nothing with the on-premises console. One findings file per store with SaaS | Metadata and results | Metadata from the collectors | Nothing when self-hosted | Metadata |
| Air-gapped operation | Console included |  | Offline collector installs only | Possible on your own Kubernetes |  |

Vendor facts come from each vendor's public documentation as of September 2026. Varonis ends its self-hosted product on 31 December 2026. IBM now lists Guardium Discover and Classify in place of a Guardium DSPM module, so the IBM column shows the last documented DSPM analyzer model.

Was this page helpful?











Thanks for your feedback!












Thanks for your feedback! Help us improve this page by using our [feedback form](https://help.accuknox.com/getting-started/dspm-overview/...).


Back to top