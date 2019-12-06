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

import sys
import json
import requests
import jsonpickle
from DataGenerator import DataGenerator

# Set DEBUG to be true if you want print statements
DEBUG = True

# Get the arguments
# Should be "python3 rest-client.py <REST SERVER IP> <GET/POST>
args = sys.argv


def print_debug(msg=""):
	if DEBUG is True:
		print(msg)


class ClientApp:
	def __init__(self, test_file="./Database/example_data.json"):
		self.addr = sys.argv[1]
		self.service = sys.argv[2]
		self._get_arguments()
		self.test_file = test_file
		self.data_to_send = DataGenerator().generate_all_data()
		self.return_value = self._call_method()

	def _get_arguments(self):
		"""
		Intended usage:
		FOR SERVER ON LOCALHOST:
		python3 rest-client.py

		FOR REMOTE SERVER
		python3 rest-client.py server_rest_address

		Note: Server_rest_address should be JUST the IP address
		:return:
		"""
		args = sys.argv
		if len(args) == 1:
			return "localhost"
		if len(args) >= 2:
			if sys.argv[2] == "POST":
				self.server_address = "http://" + self.addr + ":5000/post_data"
			if sys.argv[2] == "GET":
				self.server_address = "http://" + self.addr + ":5000/get_data"

	def _call_method(self):
		if self.service == "GET":
			return self.get_method()
		elif self.service == "POST":
			return self.post_all_data()
		else:
			print("Provided Method is Invalid")

	def post_method(self, json_data_dict):
		# Send data to the server
		print_debug("Beginning to send data to the server")
		print_debug("Sending POST request to server")
		response = requests.post(self.server_address, data=jsonpickle.encode(json_data_dict))
		print_debug("Response from [{}]: {}".format(self.server_address, response))
		print_debug()
		return response

	def get_method(self):
		print_debug("Requesting data from the server")
		response = requests.get(self.server_address)
		if response is None:
			print_debug("Response is None. No data found or an error occurred")
		print_debug("Response from [{}]: {}".format(self.server_address, response))
		return response

	def post_test_data(self):
		# Read in the data to be sent
		print_debug("Reading data from [{}] into a dictionary".format(self.test_file))
		json_data_dict = json.load(open(self.test_file))
		print_debug()
		for item in json_data_dict:
			print("Sending [{}]".format(item))
			self.post_method(json_data_dict[item])

	def post_all_data(self):
		for dataDict in self.data_to_send:
			print("Sending [{}]".format(dataDict))
			self.post_method(dataDict)

	def fetch_response(self):
		self.return_value = self.return_value.text
		return jsonpickle.decode(self.return_value)


if __name__ == "__main__":
	result = ClientApp().fetch_response()

	for item in result:
		try:
			print("{}: {}".format(item, result[item][0]))
		except:
			print("{}: []".format(item))
