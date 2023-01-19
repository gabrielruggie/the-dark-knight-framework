#!/bin/bash

# Deploys new container with name `astack-welcome`
# Includes metadata such as region, port and allows public web users to access url
# -> we will do our own authentication with this image
# Lastly, set env variables to be used in the container
gcloud run deploy ymbl-query-backend \
--image gcr.io/ymbl-development-gcp/ymbl-query-backend:latest \
--region us-central1 \
--port 8100 \
--allow-unauthenticated \
--add-cloudsql-instances ymbl-development-gcp:us-central1:dk-dev-instance \
--set-env-vars "REDIS_PASSWORD=TheDarkKnight33" \
--set-env-vars "POSTGRES_USER=dk-admin-gruggie" \
--set-env-vars "POSTGRES_PASSWORD=TheDarkKnight33" \
--set-env-vars "POSTGRES_DB=dk-beta-db-1" \
--set-env-vars "POSTGRES_UXPATH=/cloudsql/ymbl-development-gcp:us-central1:dk-dev-instance" \
--set-env-vars "IS_LOCAL_CONTAINER=0"