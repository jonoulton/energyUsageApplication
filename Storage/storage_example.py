import sys
import json
import time
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials

credentials_dict = {
    'type': 'service_account',

}
filename = "/Users/jon/Desktop/energyusageapplication-962af9407bfb.json"
project = "energyusageapplication"
bucket_name = "energy-usage-bucket"
file = "testJson.json"

test = {
    "type": "gas",
    "datetime": "12:00 10/21/19",
    "usage": 25
}

with open('testJson.json', 'w') as outfile:
    json.dump(test, outfile)

credentials = ServiceAccountCredentials.from_json_keyfile_name(filename)
client = storage.Client(credentials=credentials, project=project)
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(file)
blob.upload_from_filename(file)

time.sleep(60)
sys.path.remove(file)