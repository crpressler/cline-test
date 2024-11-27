@echo off
REM Build the Docker image if it doesn't exist
docker build -t webpage-monitor .

REM Run the container with mounted volumes
docker run -v "%cd%/state:/app/state" -v "%cd%/changes:/app/changes" webpage-monitor %*
