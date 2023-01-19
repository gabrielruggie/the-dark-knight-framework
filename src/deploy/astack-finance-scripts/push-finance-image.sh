#!/bin/bash

# build image in authentication directory
docker build -t astack-finance ../../microservices/astack-finance/api/

# Tag image with correct url in cloud
docker tag astack-finance gcr.io/ymbl-development-gcp/astack-finance

# Push updated image to cloud
docker push gcr.io/ymbl-development-gcp/astack-finance

# Clean up instantly
docker image rm astack-finance -f