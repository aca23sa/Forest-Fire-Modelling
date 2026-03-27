#!/bin/sh

# Allow X11 connections (for GUI support)
xhost +127.0.0.1

# Build Docker image
docker build -t forest-fire-model .

# Run container with display forwarding
docker run -it \
    -p 5001:5000 \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v "$(pwd)":/app \
    --name forest-fire-model \
    --hostname forest-fire-model \
    forest-fire-model \
    bash