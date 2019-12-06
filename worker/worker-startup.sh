#! /bin/bash

#sudo apt-get update
#sudo apt-get install python3-pip -y
#sudo apt-get install libpq-dev python3-dev -y
#sudo pip3 install jsonpickle
#sudo pip3 install flask
#sudo pip3 install pika

# Move things into the correct location
mkdir Database
mkdir Storage
mv DatabaseClient.py Database/DatabaseClient.py
mv StorageClient.py Storage/StorageClient.py

# Get files
#gsutil cp gs://scripts-bucket-eua/config.py .
#gsutil cp gs://scripts-bucket-eua/worker.py .

#python3 worker.py