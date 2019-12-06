#!/bin/sh
#
# This is the script you need to provide to launch a rabbitmq instance
# service
#

kubectl create -f rabbitmq.yaml
kubectl create -f rabbitmq-service.yaml