# API Security Module Overview

The **API Security** module provides deep visibility and continuous risk assessment for your APIs by analyzing live traffic, identifying unknown endpoints, and highlighting potential security exposures. It is designed to help teams reduce API attack surface, maintain compliance, and strengthen their API posture across environments.

## Key Features

### 📊 Real-Time API Inventory

Once enabled, this module automatically builds a comprehensive API Inventory by observing real-time traffic through supported connectors. APIs are categorized based on various attributes:

- **Authentication Status**: Authenticated vs Unauthenticated
- **Exposure Level**: Internal vs External
- **Data Sensitivity**: Detection of PII, tokens, credentials, etc.

Each API is assigned a **risk score** based on:

- Traffic behavior
- Exposure patterns
- Sensitive data indicators

### 🔍 Continuous Risk Detection

The system continuously detects and classifies risky APIs using advanced traffic analysis, including:

- **Shadow APIs**: Endpoints observed in traffic but not listed in specifications or documentation.
- **Zombie APIs**: Deprecated or outdated APIs still receiving traffic and remaining accessible.
- **Orphan APIs**: APIs with no clear ownership, often overlooked in governance and vulnerability scans.

### 🗂 Logical Grouping

To support better manageability and analysis, APIs can be **logically grouped** based on different parameters. This helps teams efficiently track and manage critical APIs.