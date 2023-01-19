#!/bin/bash

# Deploys new container with name `astack-authenticator`
# Includes metadata such as region, port and allows public web users to access url
# -> we will do our own authentication with this image
# Lastly, set env variables to be used in the container
gcloud run deploy astack-authenticator-ui \
--image gcr.io/ymbl-development-gcp/astack-authenticator-ui:latest \
--region us-central1 \
--port 3001 \
--cpu-throttling \
--min-instances 1 \
--allow-unauthenticated \
--add-cloudsql-instances ymbl-development-gcp:us-central1:dk-dev-instance \