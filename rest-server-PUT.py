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

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/api/json_put_request', methods=['POST'])
def test():

    # Get the request
    r = request
    # convert the data to a PIL image type so we can extract dimensions
    try:
        ioBuffer = io.BytesIO(r.data)
        img = Image.open(ioBuffer)
    # build a response dict to send back to client
        response = {
            'width' : img.size[0],
            'height' : img.size[1]
            }
    except:
        response = { 'width' : 0, 'height' : 0}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run(host="0.0.0.0", port=5000)















