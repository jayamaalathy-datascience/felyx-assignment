#!/usr/bin/env bash
docker pull mysql
docker run -p 3306:3306 --name felyx-mysql -e MYSQL_ROOT_PASSWORD=felyx -e MYSQL_DATABASE=felyxDB -d mysql:latest
