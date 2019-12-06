#! /bin/bash

# Configure gcloud CLI tool
./configure-gcloud-CLI.sh

# Create a 3-node kubernetes cluster
CLUSTER_NAME="energyusageapplication-cluster"
gcloud beta container --project "energyusageapplication" clusters create ${CLUSTER_NAME} --zone "us-west1-a" --no-enable-basic-auth --cluster-version "1.13.11-gke.14" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-cloud-logging --enable-cloud-monitoring --enable-ip-alias --network "projects/energyusageapplication/global/networks/default" --subnetwork "projects/energyusageapplication/regions/us-west1/subnetworks/default" --default-max-pods-per-node "110" --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair
gcloud container clusters get-credentials ${CLUSTER_NAME}