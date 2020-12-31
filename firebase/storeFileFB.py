#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-30-2020

# This script loads the json data to Firebase
# The code is a reworking of one of the weekly labs with help from an online tutorial

import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import datetime
import time
import os

# import requests to connect to the URL.
import requests

# import json to parse output and extract the data.
import json

# This is the url address of the PiAware json dumps
url = 'http://192.168.0.113/dump1090-fa/data/aircraft.json'

# Timestamp for the data loaded to Firebase
currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Using print(response) returns <Response [200]> to show successful connecttion to the url.
response = requests.get(url)
print(response)

data = response.text
parsed = json.loads(data)

print(json.dumps(parsed, indent=4))

# Firebase credentials
cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'ads-b-ground-station.appspot.com',
    'databaseURL': 'https://ads-b-ground-station-default-rtdb.firebaseio.com/'
})

bucket = storage.bucket()

ref = db.reference('/')
home_ref = ref.child('file')

def store_file(fileLoc):

    filename=os.path.basename(fileLoc)
    # Store File in FB Bucket
    blob = bucket.blob(filename)
    outfile=fileLoc
    blob.upload_from_filename(outfile)

def push_db(fileLoc, time):

    filename=os.path.basename(fileLoc)

    # Push the aircraft data in Realtime DB
    home_ref.push({
        'data': filename,
        'timestamp': time}
    )

# JSON file created for the data and data appended each time the script is run 
if __name__ == "__main__":
    f = open("./data.json", "a+")
    f.write(json.dumps(parsed, indent=4))
    f.close()
    store_file('./data.json')
    push_db(data, currentTime)
    time.sleep(60*10)
