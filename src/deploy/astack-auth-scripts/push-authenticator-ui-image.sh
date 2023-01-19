#!/bin/bash

# build image in authentication directory
docker build -t astack-authenticator-ui ../../microservices/astack-authentication/ui/

# Tag image with correct url in cloud
docker tag astack-authenticator-ui gcr.io/ymbl-development-gcp/astack-authenticator-ui

# Push updated image to cloud
docker push gcr.io/ymbl-development-gcp/astack-authenticator-ui

# Clean up instantly
docker image rm gcr.io/ymbl-development-gcp/astack-authenticator-ui