#!/bin/bash

# build image in rosters directory
docker build -t astack-rosters ../../microservices/astack-rosters/api/

# Tag image with correct url in cloud
docker tag astack-rosters gcr.io/ymbl-development-gcp/astack-rosters

# Push updated image to cloud
docker push gcr.io/ymbl-development-gcp/astack-rosters

# Clean up instantly
docker image rm gcr.io/ymbl-development-gcp/astack-rosters