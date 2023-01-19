#!/bin/bash

# build image in ymbl-site-static directory
docker build -t ymbl-static-frontend ../../microservices/ymbl-site-static/ui/

# Tag image with correct url in cloud
docker tag ymbl-static-frontend gcr.io/ymbl-development-gcp/ymbl-static-frontend

# Push updated image to cloud
docker push gcr.io/ymbl-development-gcp/ymbl-static-frontend

# Clean up instantly
docker image rm gcr.io/ymbl-development-gcp/ymbl-static-frontend