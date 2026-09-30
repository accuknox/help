> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aiintro.md).

# Introduction to Artificial Intelligence

Artificial intelligence (AI) enables computers and machines to simulate human intelligence and problem-solving. Common AI examples include digital assistants, self-driving cars, and tools like ChatGPT.

In computer science, AI includes machine learning and deep learning, which create algorithms inspired by the human brain's decision-making. These systems 'learn', in a manner similar to humans, from data and improve their accuracy in making predictions over time.

Recent AI advancements, like ChatGPT, mark significant progress, especially in natural language processing (NLP). Today, generative AI can understand and create human language, images, videos, software code, and even molecular structures.\
AI applications are growing rapidly, providing new opportunities to streamline business processes, and enabling new use cases that were not possible before.

### What is a Large Language Model?

A large language model (LLM) is a computational model recognized for its ability to perform general-purpose language generation and various natural language processing tasks like classification. LLMs develop these capabilities by learning statistical patterns from vast amounts of data during an intensive training process. They can generate text - a form of generative AI, by taking an input and predicting the next token or word repeatedly.

Some prominent LLMs include OpenAI's GPT series (such as GPT-3.5 and GPT-4, used in ChatGPT and Microsoft Copilot), Google's Gemini, Meta's LLaMA models, Anthropic's Claude models, and Mistral AI's models.

### Security Risks and Attack Vectors in Large Language Model Deployments

When insecure models and deployments are used, several types of attacks can occur, many of which align with the OWASP (Open Web Application Security Project ) Top 10 for LLMs:

* **Data Poisoning Attacks**: In "Training Data Poisoning", malicious actors manipulate the training data to introduce biases or vulnerabilities into the model, causing it to make incorrect or harmful predictions.
* **Model Inversion Attacks**: Attackers can infer sensitive information about the training data by querying the model, potentially leading to data breaches and loss of intellectual property.
* **Adversarial Attacks**: Reflecting OWASP's "Adversarial Input," crafted inputs can deceive the model into making incorrect predictions, which is particularly dangerous in critical applications like autonomous driving or medical diagnosis.
* **Evasion Attacks**: Evasion attacks are a prevalent threat to machine learning models during inference. This type of attack involves crafting inputs that appear normal to humans but are misclassified by machine learning systems. For instance, an adversary might alter a few pixels in an image prior to submission, causing an image recognition system to misidentify it.
* **Model Extraction Attacks**: Attackers can approximate a model's functionality by repeatedly prompting it, effectively stealing the intellectual property and potentially using it for malicious purposes.
* **Data Leakage**: If a model unintentionally reveals sensitive information it was trained on or data that is used in inference, it can lead to breaches of confidential or personal data.
* **Model Manipulation**: Unauthorized access to the model can allow attackers to alter its parameters or behavior, leading to compromised functionality and trustworthiness.
* **Inference Attacks**: Attackers exploit the model to deduce whether specific data was part of the training set, potentially exposing sensitive information.

These attacks highlight the importance of implementing robust security measures, as outlined by the OWASP Top 10 for LLMs, in the deployment and maintenance of large language models and other AI systems.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/ai-security-posture-management/aiintro.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
