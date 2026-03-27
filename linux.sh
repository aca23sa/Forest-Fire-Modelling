#!/bin/sh

#  com3524.sh
xhost +127.0.0.1

# 2. Build the image (rebuild every time if needed)
docker build -t com3524 .

# 3. Run your app with display forwarding
docker run -it \
    -p 5000:5000 \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    com3524 \
    bash
#
#  Created by Ayesha Sana on 21/08/2025.
#  
