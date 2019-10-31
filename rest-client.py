#! /Users/jon/anaconda3/bin/python3

"""
Author: Jon Oulton
Datacenter Scale Computing Final Project
File: rest-client.py

File Description:
Python program to submit a "POST" REST request to the "POST" REST server
File should be a JSON formatted file of energy use data.
The end-goal is to have the data stored in a GCP database
and the file stored in a GCP file storage bucket as a .json file
"""

import json
import requests
import jsonpickle

# Define the main parameters
addr = "http://localhost:5000/api/json_post_data_request"
filename = "Database/example_data.json"

# Read in the data to be sent
jsonDataDict = json.load(open(filename))
print(type(jsonDataDict['data0']))
print(jsonDataDict['data0'])
print()
# Send data to the server
print("Beginning to send data to the server")
for i in range(len(jsonDataDict)):
    print()
    print("Sending {} POST request to server".format(jsonDataDict['data{}'.format(i)]))
    response = requests.post(addr, data=jsonpickle.encode(jsonDataDict['data{}'.format(i)]))
    print("Response from server: {}".format(response))

print()
