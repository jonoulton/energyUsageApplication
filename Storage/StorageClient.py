import os
import json
import config
import datetime
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials


class StorageClient:
    def __init__(self):
        # Authentication information
        self.service_file = config.GCP_CREDENTIALS_FILE
        self.project = config.GCP_PROJECT
        self.bucket_name = config.STORAGE_BUCKET_NAME
        self.client = self._authenticate_to_gcp()
        self.bucket = self.client.get_bucket(self.bucket_name)

    def _authenticate_to_gcp(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.service_file)
        return storage.Client(credentials=credentials, project=self.project)

    def upload_existing_file(self, file):
        """
        Uploads a file to the cloud bucket
        :param file: The absolute or relative path of the file that should be uploaded
        :return: None
        """
        blob = self.bucket.blob(file)
        blob.upload_from_filename(file)

    def upload_from_dict(self, dataDict):
        """
        Creates a file from a dictionary (as a JSON file) and uploads that file to the cloud bucket on GCP
        :param dataDict: The dictionary to be saved as a json file
        :return: None
        """
        # Define the file name
        temp_filename = dataDict['type']

        # Create the temporary file locally
        with open(temp_filename, 'w') as outfile:
            json.dump(dataDict, outfile)

        # Upload the file to the bucket
        self.upload_existing_file(temp_filename)

        # Remove the temporary file
        os.remove(temp_filename)