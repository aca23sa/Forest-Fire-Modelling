#!/bin/sh

# Allow X11 connections (for GUI support)
xhost +127.0.0.1

# Build Docker image
docker build -t forest-fire-model .

# Run container with display forwarding
docker run -it \
    -p 5001:5000 \
    -e DISPLAY=host.docker.internal:0 \
    -v "$(pwd)":/app \
    --name forest-fire-model \
    --hostname forest-fire-model \
    forest-fire-model \
    bash