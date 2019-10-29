#! /Users/jon/anaconda3/bin/python3

"""
Author: Jon Oulton
Datacenter Scale Computing Final Project
File: rest-server-PUT.py

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

from flask import Flask, request, Response
import jsonpickle
import json
import sys
import io
import gcloud

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/api/json_put_request', methods=['POST'])
def post_data_to_gcp():
    data = request.data    # Get the request
    try:
        # Decode the data
        jsonpickle.decode(data)

        # Store the file a GCP file storage bucket as a .json file


        # Store the data in a GCP database


        response = 0    # Success
    except:
        response = 1    # Failure

    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    # Return the response
    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run(host="0.0.0.0", port=5000)


def store_file_in_GCP_storage():
    raise NotImplementedError

def store_data_in_GCP_database():
    raise NotImplementedError












