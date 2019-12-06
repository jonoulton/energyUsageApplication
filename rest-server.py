#! /Users/jon/anaconda3/bin/python3

"""
Author: Jon Oulton
Datacenter Scale Computing Final Project
File: rest-server.py

File Description:

Python program to receive POST REST requests with JSON data in the body.
Should perform the following actions:
	-Start a Flask server and spin, waiting for requests
	-When a POST request is received:
		-Read the data in to local memory
		-Store the file in a GCP file storage bucket as a JSON file
		-Store the data in a GCP database
		-Send a response that everything went well, or that it didn't go well.
	-When a GET request is received:
		-Get the data from the tables in the database
		-Return them to the user, unless something went wrong
"""

from flask import Flask, request, Response
from Database.DatabaseClient import DatabaseClient
import jsonpickle
import config
import pika

# Establish a connection to rabbitmq
credentials = pika.PlainCredentials(username="guest", password="guest")
connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBITMQ_ADDRESS, port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='toWorker')

# Initialize the Flask application
app = Flask(__name__)

def return_response(response):
	print()
	# Encode response using jsonpickle
	response_pickled = jsonpickle.encode(response)
	# Return the response
	return Response(response=response_pickled, status=200, mimetype="application/json")


# route http posts to this method
@app.route('/post_data', methods=['POST'])
def post_data_to_gcp():
	data = request.data    # Get the request
	data = data.decode("utf-8")

	# Decode the data
	jsonDataDict = jsonpickle.decode(data)

	body = {
		"method": "POST",
		"jsonDataDict": jsonDataDict
	}

	body = jsonpickle.encode(body)

	channel.basic_publish(exchange="", routing_key="toWorker", body=body)

	return return_response("True")


# route http posts to this method
@app.route('/get_data', methods=['GET'])
def get_data_from_gcp():
	print()
	# Get the data
	try:
		# Store the data in a GCP database
		print("Instantiating a DatabaseClient object")
		databaseClient = DatabaseClient()

		print("Using DatabaseClient object to retrieve data from the database")
		responseDict = databaseClient.get_all_data_from_database()

	except Exception as e:
		print("Data was not successfully retrieved from database")
		print("Exception: {}".format(e))
		responseDict = {}

	return return_response(responseDict)


# start flask app
app.run(host="0.0.0.0", port=5000)













