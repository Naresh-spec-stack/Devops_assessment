#!/bin/bash
docker build -t localhost:5000/api:latest ./api
docker push localhost:5000/api:latest
