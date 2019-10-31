#! /bin/bash

# This file starts the cloud proxy and tests the database creation and upload some test data

./cloud_sql_proxy -dir=\cloudsql -instances=energyusageapplication:us-west1:energy-usage-psql-database=tcp:5432 -credential_file=/Users/jon/Desktop/energyusageapplication-962af9407bfb.json &
echo "Sleeping for 5 seconds"
sleep 5
database_data_entry_test.py

# Instructions for setting up the cloud sql proxy:

# Set user password
# gcloud sql users set-password postgres --instance energy-usage-psql-database --password energy

# Connection name for the instance:
# energyusageapplication:us-west1:energy-usage-psql-database

# Create a database on the instance:
# gcloud sql databases create energy-database --instance=energy-usage-psql-database

# Download the cloud proxy
# curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64

# Make it executable
# chmod +x cloud_sql_proxy