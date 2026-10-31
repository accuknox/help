[Skip to content](https://help.accuknox.com/how-to/vm-security/agentless/cloud-vm-scanning/#cloud-based-vm-scanning-agentless)

Copy page

Copy page

Copy page as Markdown for LLMs

View as Markdown ↗

View this page as plain text

Open in ChatGPT ↗

Ask questions about this page

Open in Claude ↗

Ask questions about this page

# Cloud Based VM Scanning (Agentless) [¶](https://help.accuknox.com/how-to/vm-security/agentless/cloud-vm-scanning/\#cloud-based-vm-scanning-agentless "Permanent link")

Agent-less VM scanning is supported for AWS, GCP, Azure, and OpenShift.
Support for OCI and Nutanix is planned.

![VM Scanning](https://help.accuknox.com/how-to/vm-security/agentless/image.png)

## Public Clouds - AWS, GCP, Azure [¶](https://help.accuknox.com/how-to/vm-security/agentless/cloud-vm-scanning/\#public-clouds-aws-gcp-azure "Permanent link")

This guide assumes that Terraform and the respective cloud provider CLI are
installed. You should have received the Terraform code from AccuKnox.

```
terraform/
├── aws
│   ├── cloud-init.yaml -> ../cloud-init.yaml
│   ├── main.tf
│   ├── otel-collector-config.yaml -> ../otel-collector-config.yaml
│   ├── provider.tf
│   ├── terraform.tfvars.example
│   └── variables.tf
├── azure
│   ├── cloud-init.yaml -> ../cloud-init.yaml
│   ├── main.tf
│   ├── otel-collector-config.yaml -> ../otel-collector-config.yaml
│   ├── provider.tf
│   ├── terraform.tfvars.example
│   └── variables.tf
├── cloud-init.yaml
├── gcp
│   ├── cloud-init.yaml -> ../cloud-init.yaml
│   ├── main.tf
│   ├── otel-collector-config.yaml -> ../otel-collector-config.yaml
│   ├── provider.tf
│   ├── terraform.tfvars.example
│   └── variables.tf
└── otel-collector-config.yaml
```

Each cloud provider directory includes a `terraform.tfvars.example` file.
Update the file according to your requirements and save it as
`terraform.tfvars`.

```
cd aws
cp terraform.tfvars.example terraform.tfvars
```

- Artifact API tokens can be created under Settings -> Tokens.
- Labels can be created under Settings -> Labels.

After configuration, run `terraform apply` to provision the required
infrastructure in the corresponding cloud account.

```
terraform apply
```

Was this page helpful?











Thanks for your feedback!












Thanks for your feedback! Help us improve this page by using our [feedback form](https://help.accuknox.com/how-to/vm-security/agentless/cloud-vm-scanning/...).


Back to top