> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/ai-security-posture-management/unmanaged-ai-models.md).

# Unmanaged AI Models

## Risks and Importance of Tracking

As artificial intelligence (AI) continues to revolutionize industries, many organizations are building AI applications to enhance their product workflows, decision-making, and automation. While many of these models are deployed through managed services (like AWS Bedrock, Google Vertex AI, or Azure AI), they can also run on self-managed cloud infrastructure. The use of unmanaged environments presents unique challenges in terms of security, oversight, and governance. In this article, we explore the nature of unmanaged AI models, why they are important to track, and how Prisma Cloud provides support in managing them.

## Defining Unmanaged Models

Unmanaged AI models refer to AI models that are deployed and operated on self-managed cloud infrastructure, rather than through cloud providers' managed services. While services like AWS Bedrock, Google Vertex, or Azure AI offer integrated environments for deploying AI models with some built-in security, monitoring, and management, unmanaged models are typically hosted on virtual machines (VMs), containers, or other self-managed infrastructure.

These models are often sourced from public repositories like Hugging Face and may be updated, retrained, or fine-tuned using locally stored data. Since these models aren’t integrated into managed services with pre-configured security, it’s easy for organizations to overlook potential risks. This can lead to the proliferation of Shadow AI—AI tools and models used by employees without oversight from IT or security teams. Shadow AI can introduce vulnerabilities by bypassing established security protocols and making it harder for organizations to monitor and manage their AI deployments effectively.

## Risks and Challenges of Unmanaged Models

Tracking and securing unmanaged AI models is crucial due to several risks they present:

1. **Limited Security Oversight**: Without the built-in security features of managed services, unmanaged environments can lack the necessary oversight to prevent vulnerabilities. Security policies may not be uniformly enforced, increasing the risk of unmonitored AI instances that could be vulnerable to exploitation.
2. **Frequent Updates and Retraining**: Many AI models are not static; they undergo frequent updates, retraining, and fine-tuning based on new data. In unmanaged environments, this process can be more ad-hoc, which may result in models being deployed with outdated or insecure configurations, further increasing the attack surface.
3. **Sensitive Data Exposure**: Unmanaged AI models often rely on locally stored or sensitive data. If these models aren’t carefully monitored, it’s possible that they could inadvertently expose confidential information, either through improper access controls or data leakage.
4. **Inconsistent Governance**: In an unmanaged environment, there’s a lack of uniform policies for model validation, testing, and deployment. Without governance in place, it’s harder to ensure that AI models are operating as expected and complying with organizational standards or regulations.
5. **Critical Contexts**: Unmanaged AI models are increasingly being used in sensitive or critical environments where the consequences of a breach or failure could be severe. Whether it's in healthcare, finance, or cybersecurity, unmanaged models can present unique risks if they aren't properly tracked and monitored.

## Supported Cloud Platforms and Model Repositories

Prisma Cloud provides support for identifying and tracking unmanaged AI models across several cloud platforms. Our platform helps organizations discover AI models hosted on self-managed environments and ensures they are adequately protected. Currently, we support the following cloud platforms and model repositories:

### Supported Cloud Platforms

* **AWS**
* **Azure**
* **Google Cloud (GCP)**

### Model Storage

Prisma Cloud identifies model files on Virtual Machines (VMs).

### Supported Model Repositories

**Hugging Face** ([huggingface.co/models](https://huggingface.co/models)): A popular platform for hosting and sharing AI models, including pre-trained models for a variety of tasks.

#### Supported Model Families

We currently support a broad range of AI models across several families:

* **GPT** (Generative Pre-trained Transformer)
* **Llama** (Large Language Model Meta AI)
* **Falcon**
* **Gemma**
* **Mistral**
* **Phi**
* **Qwen**
* **RoBERTa**
* **Jamba**
* **BLOOM** (BigScience Large Open-science Open-access Multilingual)
* **DBRX**
* **Mosaic ML**
* **Grok**

## Conclusion

The growing use of AI in business workflows makes it increasingly important to manage and secure all AI models, whether deployed through managed services or self-managed infrastructures. Unmanaged AI models, in particular, introduce unique risks, such as vulnerabilities, compliance gaps, and sensitive data exposure. Tracking and securing these models is essential to reducing risks and ensuring that AI applications remain safe, secure, and compliant.

With Prisma Cloud’s extensive support for unmanaged AI models across leading cloud platforms and model families, organizations can proactively manage the security of their AI environments and safeguard against potential threats.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/ai-security-posture-management/unmanaged-ai-models.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
