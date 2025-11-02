# Nexus : Minimal System Dashboard

![Docker Image Size](https://img.shields.io/docker/image-size/kevinchrist/nexus)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

A resource-efficient, server-side rendered system dashboard ,
developed with Python and Flask. Focused on minimal dependencies (psutil).

This is the offical image: [Docker Hub](https://hub.docker.com/r/kevinchrist/nexus)

## Features

- CPU utilization
- Memory usage
- Disk space

## Installation

The installation is pretty simple. Make sure to download Docker and 
[Docker-compose](https://docs.docker.com/compose/install/). Then just simply
use the docker-compose file from this repo

1. Copy the docker-compose.yml file

```docker
services:
  Nexus:
    container_name: nexus
    image: kevinchrist/nexus:v1.0
    restart: unless-stopped
  
    network_mode: "host"
    
    # change the port binding how you like, e.g. "0.0.0.0:8080" ...
    command: ["gunicorn", "--bind", "0.0.0.0:5080", "src.app:app"]

```

2. Start the container with `docker-compose up -d`

The application should now be available on the port you mapped it to.
