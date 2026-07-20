# Django sample app with deploy actions example

[![codecov](https://codecov.io/gh/painassasin/django-example-deploy/graph/badge.svg?token=t5mL2nsrzR)](https://codecov.io/gh/painassasin/django-example-deploy)
[![Deploy](https://github.com/painassasin/django-example-deploy/actions/workflows/deploy.yaml/badge.svg)](https://github.com/painassasin/django-example-deploy/actions/workflows/deploy.yaml)

This repository provides an example of deploying a Django application.  
The application itself has no functional logic — the focus is entirely on the workflows.

## Continuous Integration

This workflow runs on every push to the `main` branch (when we merge a PR) or on PR creation.  
It performs the following basic checks:

- Linting
- Testing
- Build

For linting, `ruff` is used, but additional checks can be configured as needed.

During the test stage, standard Django unit tests are executed against a PostgreSQL database.  
After that, a coverage report is generated and sent to Codecov (this step is optional).

In the final stage, the Docker image is built **only** — it is **not** pushed to any registry.  
This simply verifies that the build completes without errors.

## Continuous Delivery

This workflow runs when a tag is pushed to the `main` branch.  
The job will only trigger for tags on `main` — this is configured via the GitHub environment settings.

Stages:

- Build and Push
- Deploy

In the first stage, the Docker image is built and pushed to Docker Hub,  
tagged with both the current version (from the Git tag) and `latest`, for example:  
`deploy-example:latest`, `deploy-example:1.1.2`

Then the deployment stage begins.

First, an environment file (`.env`) is prepared.  
The image tag to run is extracted from the Git tag, stripping the leading `v`.  
Other variables are populated from the secrets defined in the `production` environment.

The deployment process then performs the following actions:

- Connects to the server and stops the currently running containers
- Overwrites the `.env`, `docker-compose.yaml`, and `nginx.conf` files on the server  
  (no other files are present on the server)
    - A dedicated Docker Compose file for production (`docker-compose.deploy.yaml`) is used
- Starts the new containers
- Cleans up old containers (images older than 24 hours are pruned)

## Additional data

To simplify CI/CD operations, I deliberately avoid using caching and "long" server pause on deploy.