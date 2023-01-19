#!/bin/bash

# Deploys new container with name `astack-rosters`
# Includes metadata such as region, port and allows public web users to access url
# -> we will do our own authentication with this image
# Lastly, set env variables to be used in the container
gcloud run deploy astack-rosters \
--image gcr.io/ymbl-development-gcp/astack-rosters:latest \
--region us-central1 \
--port 8001 \
--allow-unauthenticated \
--add-cloudsql-instances ymbl-development-gcp:us-central1:dk-dev-instance \
--set-env-vars "API_VERSION=beta-v1.0" \
--set-env-vars "POSTGRES_USER=dk-admin-gruggie" \
--set-env-vars "POSTGRES_PASSWORD=TheDarkKnight33" \
--set-env-vars "POSTGRES_DB=dk-dev-database-1" \
--set-env-vars "POSTGRES_UXPATH=/cloudsql/ymbl-development-gcp:us-central1:dk-dev-instance" \
--set-env-vars "TOKEN_SECRET_KEY=dktokentestkey" \
--set-env-vars "TOKEN_ALGORITM=HS256" \
--set-env-vars "GOOGLE_APPLICATION_CREDENTIALS=./main/gruggie-service-key.json" \
--set-env-vars "GOOGLE_CLOUD_PROJECT=ymbl-development-gcp" \
--set-env-vars "POSTGRES_EVENTS_TOPIC=dk.services.postgres" \
--set-env-vars "REDIS_PASSWORD=TheDarkKnight33" \
--set-env-vars "DK_ADMIN_TOKEN_URL=https://astack-authenticator-3jcqeir73q-uc.a.run.app/admin-stack/beta-v1.0/oauth/authenticator/token" \
--set-env-vars "IS_LOCAL_CONTAINER=0"