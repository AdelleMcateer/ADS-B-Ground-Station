#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-24-2020

# This script loads the json data from the url and stores it in a file on the RaspberryPi
# The code is a reworking of one of the weekly labs with help from an online tutorial

import datetime
import time

# import requests to connect to the URL.
import requests

# import json to parse output and extract the data.
import json

# This is the url address of the PiAware json dumps
url = 'http://192.168.0.113/dump1090-fa/data/aircraft.json'

# Timestamp for the data loaded to the data file
currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Using print(response) returns <Response [200]> 
# shows successful connecttion to the url.

response = requests.get(url)
print(response)

data = response.text
parsed = json.loads(data)

# Print the json info, indented to 4 spaces for readability
print(json.dumps(parsed, indent=4))

while True:

    fileLoc = f'/home/pi/assignment/data.json' # set location of data file and current time
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'data taken at {currentTime}') # print the time data taken at
    f = open("..//data.json", "a+") #open a local file and append the information
    f.write(currentTime) #time and date added before data
    f.write(data)  # Write the data to the file
    f.close()
    time.sleep(60*15) # Repeat every 15 minutes, will add to crontab once complete

