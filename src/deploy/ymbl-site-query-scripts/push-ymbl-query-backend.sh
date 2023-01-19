#!/bin/bash

# build image in ymbl-site-query directory
docker build -t ymbl-query-backend ../../microservices/ymbl-site-query/api/

# Tag image with correct url in cloud
docker tag ymbl-query-backend gcr.io/ymbl-development-gcp/ymbl-query-backend

# Push updated image to cloud
docker push gcr.io/ymbl-development-gcp/ymbl-query-backend

# Clean up instantly
docker image rm gcr.io/ymbl-development-gcp/ymbl-query-backend