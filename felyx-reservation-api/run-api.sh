#!/usr/bin/env bash
docker build -t felyx-reservation-api .
docker run -p 8000:8000 -t felyx-reservation-api
