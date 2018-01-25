# webdev-demo

An example of a typical web dev environment built with Docker, Django, Nginx, Redis, and more.

## Requirements

* Docker
* docker-compose

## Setup

* Clone repo
* `cd` to the root of the repo
* Generate self-signed SSL cert and key: `openssl req -nodes -x509 -newkey rsa:4096 -keyout certs/server.key -out certs/server.crt -days 365` (accept all defaults)
* `docker-compose up -d`
* Access the website on http://localhost:8000 or https://localhost:4433 (accept any security warnings)
