#!/bin/bash

# Deploys new container with name `ymbl-static-frontend`
# Includes metadata such as region, port and allows public web users to access url
# -> we will do our own authentication with this image
# Lastly, set env variables to be used in the container
gcloud run deploy ymbl-static-frontend \
--image gcr.io/ymbl-development-gcp/ymbl-static-frontend:latest \
--region us-central1 \
--cpu-throttling \
--min-instances 1 \
--port 3000 \
--allow-unauthenticated \
--add-cloudsql-instances ymbl-development-gcp:us-central1:dk-dev-instance \