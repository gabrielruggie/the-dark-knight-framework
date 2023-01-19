#!/bin/bash

# build image in authentication directory
docker build -t astack-authenticator ../../microservices/astack-authentication/api/

# Tag image with correct url in cloud
docker tag astack-authenticator gcr.io/ymbl-development-gcp/astack-authenticator

# Push updated image to cloud
docker push gcr.io/ymbl-development-gcp/astack-authenticator

# Clean up instantly
docker image rm gcr.io/ymbl-development-gcp/astack-authenticator