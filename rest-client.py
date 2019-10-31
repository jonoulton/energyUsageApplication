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

# Get the arguments
args = sys.argv


class ClientApp:
    def __init__(self, file_to_send="Database/example_data.json"):
        self.file_to_send_as_CLA = False
        self.server_address_as_CLA = False
        self._get_arguments()
        self.addr = sys.argv[1]
        self.server_address = "http://" + self.addr + ":5000/api/json_post_data_request"
        self.file_to_send = file_to_send

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
        if len(args) == 2:
            return sys.argv[1]
        self.server_address_as_CLA = True

    def client_main(self):
        # Read in the data to be sent
        print("Reading data from [{}] into a dictionary".format(self.file_to_send))
        json_data_dict = json.load(open(self.file_to_send))
        print()

        # Send data to the server
        print("Beginning to send data to the server")
        for i in range(len(json_data_dict)):
            print()
            print("Sending {} POST request to server".format('data{}'.format(i)))
            response = requests.post(self.server_address, data=jsonpickle.encode(json_data_dict['data{}'.format(i)]))
            print("Response from [{}]: {}".format(self.server_address, response))
        print()


if __name__ == "__main__":
    ClientApp().client_main()