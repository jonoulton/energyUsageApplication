#! /bin/bash

# Delete all resources (but not cluster)
kubectl delete -f rest-server.yaml
kubectl delete -f rest-server-service.yaml