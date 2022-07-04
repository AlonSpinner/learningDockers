#!/bin/bash
IMAGE_TAG="testdocker"
CONTAINER_NAME="tempContainer"

docker build -t ${IMAGE_TAG} .
docker run --name ${CONTAINER_NAME} -d ${IMAGE_TAG}

docker cp ${CONTAINER_NAME}:'/usr/src/points.csv' .
docker stop ${CONTAINER_NAME}
docker rm ${CONTAINER_NAME}
