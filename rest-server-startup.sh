#! /bin/bash

sudo apt-get update
sudo apt-get install python3-pip -y
sudo apt install libpq-dev python3-dev
sudo pip3 install jsonpickle
sudo pip3 install psycopg2
sudo pip3 install flask
sudo pip3 install pika

# Get files
gsutil cp gs://scripts-bucket-eua/config.py .
gsutil cp gs://scripts-bucket-eua/rest-server.py .
gsutil cp gs://scripts-bucket-eua/DataGenerator.py .

python3 rest-server.py