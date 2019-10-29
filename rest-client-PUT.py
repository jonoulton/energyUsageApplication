#! /Users/jon/anaconda3/bin/python3

"""
Author: Jon Oulton
Datacenter Scale Computing Final Project
File: rest-client-PUT.py

File Description:
Python program to submit a "POST" REST request to the "POST" REST server
File should be a JSON formatted file of energy use data.
The end-goal is to have the data stored in a GCP database
and the file stored in a GCP file storage bucket as a .json file
"""

import jsonpickle
import requests
import time
import sys

# Define the main parameters
addr = "http://localhost:5000/api/json_put_request"
filename = "example_data.json"

# Read in the data to be sent
json_data = open(filename).read()

print("Sending POST request to server")
response = requests.post(addr, data=jsonpickle.encode(json_data))
print("Response from server: {}".format(response))
