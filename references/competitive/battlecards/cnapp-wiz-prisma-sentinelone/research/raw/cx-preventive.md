> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/cloud-workload-preventive-action.md).

# Cloud workload preventive action

Learn how Cortex XSIAM cloud workload preventive actions block Kubernetes deployments and fail CI pipelines.

Some Cloud Workload policies provide a **Prevent and Create an Issue** action that enforces compliance during deployments.

### **Prevention action for runtime stage policies**

The Prevent action at Runtime applies only to Kubernetes Workload Images assets.

When a Kubernetes Workload image violates a policy, the Kubernetes Admission Controller (on clusters where the KSPM Connector is deployed and Admission Control is enabled) can block it from being admitted to the cluster.

For all other asset types within the policy scope, no runtime prevention will occur. Instead, the violation will result in an Issue being created.

### **Prerequisites**

Ensure that your cluster has the Posture Management (KSPM) Connector deployed with the Admission Controller functionality enabled.

You can manage these deployments from the Kubernetes Connectivity Management page.

To access the [Kubernetes Connectivity Management](/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources/administration-and-troubleshooting.md), navigate to the following URL in your tenant environment: https\://\[TENANT-ADDRESS]/cwp/k8s-management.

### **Important considerations**

* **Recommended Approach**: Begin with the **Create an Issue** action to validate results before selecting **Prevent and Create an Issue**. This helps prevent potential disruptions to your applications or development workflows.
* **Impact on New Deployments**: The **Prevent and Create an Issue** action affects only new or future deployments that meet the prevention criteria. It does not impact cloud workload assets that are already deployed.

### **Prevention action for CI stage Policies**

Prevention actions in the CI stage triggers a pipeline failure by returning an exit code of 2 in the CI tool.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/cloud-workload-preventive-action.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
