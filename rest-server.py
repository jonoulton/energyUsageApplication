#! /Users/jon/anaconda3/bin/python3

"""
Author: Jon Oulton
Datacenter Scale Computing Final Project
File: rest-server.py

File Description:

Python program to receive POST REST requests with JSON data in the body.
Should perform the following actions:
    -Start a Flask server and spin, waiting for requests
    -When a request is received:
        -Read the data in to local memory
        -Store the file in a GCP file storage bucket as a JSON file
        -Store the data in a GCP database
        -Send a response that everything went well, or that it didn't go well.
"""

import io
import sys
import json
import jsonpickle
from flask import Flask, request, Response
from Storage.StorageClient import StorageClient
from Database.DatabaseClient import DatabaseClient

# Initialize the Flask application
app = Flask(__name__)

# If in development, empty the database first
DEVELOPMENT = True
if DEVELOPMENT:
    DatabaseClient().reset_database()

# route http posts to this method
@app.route('/api/json_post_data_request', methods=['POST'])
def post_data_to_gcp():
    data = request.data    # Get the request

    # Decode the data
    jsonDataDict = jsonpickle.decode(data)
    response = []

    print()
    # Upload data to storage
    try:
        # Store the file a GCP file storage bucket as a .json file
        print("Instantiating a StorageClient object")
        storageClient = StorageClient()

        print("Using StorageClient object to upload file")
        storageClient.upload_from_dict(jsonDataDict)

        print("Storage upload was successful")
        response.append("Storage Upload Successful")
    except Exception as e:
        response.append("Storage Upload Unsuccessful")
        print("Data was not successfully uploaded to storage")
        print("Exception: {}".format(e))

    print()
    # Upload data to database
    try:
        # Store the data in a GCP database
        print("Instantiating a DatabaseClient object")
        databaseClient = DatabaseClient()

        print("Using DatabaseClient object to upload data to database")
        databaseClient.add_data_from_dict(jsonDataDict)

        print("Database upload was successful")
        response.append("Database Upload Successful")
    except:
        response.append("Database Upload Unsuccessful")
        print("Data was not successfully uploaded to database")
    print()

    # Encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    # Return the response
    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run(host="0.0.0.0", port=5000)













