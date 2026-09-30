> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aiaec.md).

# AI Application Ecosystem Components

The AI application ecosystem comprises several critical components that work together to enable the functionality of AI-driven applications. Here are the main parts along with examples:

### Model Endpoint

The model endpoint is the interface through which applications interact with the AI model. It acts as an access point for sending inputs to the model and receiving outputs. The endpoint is responsible for managing requests, routing them to the appropriate model instance, and returning the results to the application.

**Example**: An Azure OpenAII deployment using OpenAI's GPT-4, which allows developers to integrate natural language processing capabilities into their applications by sending text prompts and receiving generated text in response.

**Example**: Amazon Web Services (AWS) EC2 instances with GPU acceleration running Llama2 by Meta, which supports an application that communicates with the EC2 instance.

### Model

The model is the core component of the AI ecosystem. It is the trained machine learning model that takes input data, processes it, and produces output. In the context of large language models (LLMs), this involves understanding and generating human-like text based on the given input.

**Example**: OpenAI's GPT-4 model, which can generate coherent and contextually relevant text, answer questions, and perform various other natural language processing tasks.

### Plugin

A plugin is an auxiliary but highly capable model or tool that acts as a helper to the primary AI model. Plugins extend the functionality of the main model by providing specialized capabilities, such as accessing inference datasets, performing specific computations, or interfacing with other services. This approach, known as retrieval-augmented generation (RAG), enhances the primary model's ability to generate more accurate and contextually relevant outputs.

**Example**: A weather plugin integrated with an AI chatbot that allows the chatbot to fetch and provide real-time weather updates based on user queries. Another example is a language translation plugin that helps the main model translate text between different languages.

### Training Datasets

Training is a fundamental stage in the AI development process where the model learns to perform its tasks by processing large amounts of data. During this phase, the model is exposed to various examples and adjusts its internal parameters to minimize errors in predictions or classifications. The dataset is the integral part of the process, with the insights learned by the model influenced by the training data.

**Example**: Training a model like GPT-4 involves using vast text corpora from various sources to help the model understand language patterns, context, and nuances, enabling it to generate coherent and contextually relevant text.

### Inference Datasets

Inference datasets are specialized collections of data used during the inference phase of AI models, which is the stage where the model makes predictions or generates outputs based on new input data. Unlike training datasets, which are used to teach the model how to understand and process information, inference datasets help improve the model's performance by providing realistic, real-world data inputs for better contextual answering.

**Example**: when building a chatbot for customers to learn more about their spending habits, the financial institutions will use the transactions of the customer as inference data to provide contextually accurate answers

### Example Scenario

AI-Powered Customer Support Chatbot

To illustrate how these components work together, consider an AI-powered customer support chatbot:

* **Model Endpoint**: The chatbot application interacts with the GPT-4 model through the Azure OpenAI Deployment, which serves as the model endpoint. This endpoint handles user queries, processes them, and directs them to the GPT-4 model to generate responses.
* **Model**: ​​The GPT-4 model receives the user's query, processes i, and generates a relevant and contextually appropriate response based on the information and nuances provided in the query.
* **Plugin**: The chatbot integrates a customer database plugin that allows it to fetch user-specific inference data, such as order status or account details, to provide more personalized and accurate support. The customer database used by the plugin is the Inference Dataset.
* **Training Dataset**: The chatbot undergoes fine-tuning\* using a dataset of previous customer interactions and support tickets, making it adept at handling common inquiries and issues in the specific industry.\
  \*Refer to the section below, What is Fine-Tuning for more details.
* **Application**: The customer support platform integrates the chatbot with a user-friendly interface.

#### What is Fine-Tuning?

Fine-tuning in machine learning refers to the process of adapting a pre-trained model to perform specific tasks or cater to particular use cases. This technique has become essential in deep learning, especially for training foundation models used in generative AI.

Fine-tuning leverages data (similarly to training) in order to adjust the responses of the model to certain inputs, making it more suitable for the intended business case.

#### What is Retrieval-Augmented Generation?

Retrieval-Augmented Generation (RAG) enhances large language model (LLM) responses by incorporating information from knowledge bases and other sources. This allows the model to reference up-to-date inference data before generating a response, improving contextual accuracy. This approach is cost-effective and ensures the output remains relevant, accurate, and useful across different contexts.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/ai-security-posture-management/aiaec.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
