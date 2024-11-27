#!/bin/bash

# Build the Docker image if it doesn't exist
docker build -t webpage-monitor .

# Run the container with mounted volumes
docker run -v "$(pwd)/state:/app/state" -v "$(pwd)/changes:/app/changes" webpage-monitor "$@"
