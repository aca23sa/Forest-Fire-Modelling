
@echo off
REM ============================
REM Run Forest Fire Model Web App on Windows with Docker
REM ============================

REM ---- CONFIG ----
set IMAGE_NAME=forest-fire-model

REM ---- BUILD IMAGE ----
echo Building Docker image...
docker build -t %IMAGE_NAME% .

REM ---- RUN CONTAINER WITH INTERACTIVE SHELL ----
echo Running web app on http://127.0.0.1:5000 ...
docker run -it ^
    -e DISPLAY=host.docker.internal:0.0 ^
    -p 5000:5000 ^
    %IMAGE_NAME% ^
    bash

pause
