---
title: Count Images in Registry
description: Get the count of images stored in the DockerHub, AWS ECR, GCR, and ACR registries using the command line.
---

??? "**DockerHub**"

    To get the count of dockerhub images please use the following the command after connecting your dockerhub repository to the commandline using dockerdesktop application.

    ```sh
    docker images <repository-name>
    ```

    **Note:** Replace the <repository-name\> with your repository name.

??? "**AWS ECR**"

    To get the count of the ECR Repository images the users need to connect the AWS account using AWS CLI and use the following command for getting the image count in each repository

    ```sh
    aws ecr describe-images --repository-name <repository-name> --query "length(imageDetails[])"
    ```

    **Note:** Replace the <repository-name\> with your repository name.

??? "**GCR**"

    To get the count of images stored in the GCR registry using the gcloud command line tool use the following command

    ```sh
    gcloud container images list-tags gcr.io/<PROJECT_ID>/<REPOSITORY_NAME> --format='get(digest)' | wc -l
    ```

    **Note:** Replace the <PROJECT_ID\> with your Google Cloud project ID and <REPOSITORY_NAME\> with the name of the GCR repository you want to count images.

??? "**ACR**"

    To get the count of images stored in an Azure Container Registry (ACR) using Azure CLI use the following command

    ```sh
    az acr repository show-tags --name <ACR_NAME> --repository <REPOSITORY_NAME> --output json --query "length(@)"
    ```

    **Note:** Replace <ACR_NAME\> with the name of your Azure Container Registry and <REPOSITORY_NAME\> with the name of the ACR repository you want to count images