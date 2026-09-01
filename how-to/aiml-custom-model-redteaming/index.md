---
title: Custom Model Red Teaming
description: Red team a single model on Bedrock, NVIDIA Triton, or vLLM with the AccuKnox Custom Model collector, without onboarding a full cloud account.
hide:
  - toc
---

# Custom Model Red Teaming

<style>
  .nt-card-title{
    text-align: center;
  }

  .nt-card-img img{
    color: #00025;
  }
</style>

The **Custom Model** collector red teams a single model over its HTTP inference endpoint, without onboarding a full cloud account. The flow works for any LLM exposed over HTTP. Pick your serving platform to get started.

::cards:: cols=3

- title: AWS Bedrock
  image: ./icons/aws-bedrock.svg
  url: /how-to/aiml-bedrock-collector/

- title: NVIDIA Triton
  image: ./icons/nvidia-triton.svg
  url: /how-to/aiml-triton-collector/

- title: vLLM
  image: ./icons/vllm.svg
  url: /how-to/aiml-vllm-collector/

::/cards::

!!! note "Secret tokens for custom models"
    Managed Bedrock onboarding uses a Bedrock API key. Self-hosted targets such as NVIDIA Triton and vLLM have **no default secret token**, so leave the token empty unless your endpoint sits behind an auth proxy or was started with an API key.

!!! tip "Prefer full-account coverage?"
    To scan every model in a cloud account automatically, use the [AWS AI/ML Onboard](aiml-aws-onboard.md), [Azure AI/ML Onboard](aiml-azure-onboard.md), or [GCP AI/ML Onboard](aiml-gcp-onboard.md) flows instead.
