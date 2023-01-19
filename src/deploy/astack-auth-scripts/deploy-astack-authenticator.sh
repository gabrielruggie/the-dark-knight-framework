#!/bin/bash

# Deploys new container with name `astack-authenticator`
# Includes metadata such as region, port and allows public web users to access url
# -> we will do our own authentication with this image
# Lastly, set env variables to be used in the container
gcloud run deploy astack-authenticator \
--image gcr.io/ymbl-development-gcp/astack-authenticator:latest \
--region us-central1 \
--port 8002 \
--allow-unauthenticated \
--add-cloudsql-instances ymbl-development-gcp:us-central1:dk-dev-instance \
--set-env-vars "API_VERSION=beta-v1.0" \
--set-env-vars "POSTGRES_USER=dk-admin-gruggie" \
--set-env-vars "POSTGRES_PASSWORD=TheDarkKnight33" \
--set-env-vars "POSTGRES_DB=dk-beta-db-1" \
--set-env-vars "POSTGRES_UXPATH=/cloudsql/ymbl-development-gcp:us-central1:dk-dev-instance" \
--set-env-vars "TOKEN_EXPIRE_TIME_MINUTES=60" \
--set-env-vars "TOKEN_SECRET_KEY=dktokentestkey" \
--set-env-vars "TOKEN_ALGORITM=HS256" \
--set-env-vars "REDIS_PASSWORD=TheDarkKnight33" \
--set-env-vars "DK_VALIDATION_KEY=dk-validation-key" \
--set-env-vars "IS_LOCAL_CONTAINER=0"