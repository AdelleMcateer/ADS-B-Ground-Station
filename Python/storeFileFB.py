#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-24-2020

# This script attempts to load the json data to Firebase
# The code is a reworking of one of the weekly labs with help from an online tutorial

import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import time
from datetime import datetime
import os

# import requests (or urllib2) to connect to the URL.
import requests

# import json to parse the JSON output and extract the data you need.
import json

url = 'http://192.168.1.123/dump1090-fa/data/aircraft.json'

# Using print(response) returns <Response [200]> which means you are successfully connected.
response = requests.get(url)
print(response)

# Read the output
data = response.text

# Parse JSON – convert the string to JSON
parsed = json.loads(data)

# Use of indentation to make the data more readable 
print(json.dumps(parsed, indent=4))

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

    # Push file reference to image in Realtime DB
    home_ref.push({
        'image': filename,
        'timestamp': time}
    )

if __name__ == "__main__":
    f = open("./test.txt", "w")
    f.write("test")
    f.close()
    store_file('./test.txt')
    push_db('./test.txtO', '12/23/2020 9:00')

