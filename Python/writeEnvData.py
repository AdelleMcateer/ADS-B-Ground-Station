#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-24-2020

# This script incorporates the flighttest.py script.
# It is expanded further to send a react to ThingSpeak if data is detected in the array 

from urllib.request import urlopen
import  json
import  time
from sense_hat import SenseHat

import requests
import json

#ThingSpeak API PiAware channel key
WRITE_API_KEY='8I224HGCPZE8CG6Y'

#ThingSpeak ThingTweetURL & channel API key
baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

#clear sensehat and intialise light_state
sense.clear()

#api -endpoint
URL = 'http://192.168.1.123/dump1090-fa/data/aircraft.json'

green =(0, 255, 0)
red = (255, 0, 0)

def writeData(status):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s' % (status))
    print(conn.read())
    # Closing the connection
    conn.close()

# If statement to search the json array
# The sense hat displays Data Detection or No data depending on the information
# stored in the URL array

while True:
    r = requests.get(url = URL)
    data = r.json()

    flightData = data["aircraft"]
    print("Aircraft data: "+str(flightData))

    if flightData:
        sense.show_message("Data Detection!", text_colour = green)
        status=1
        writeData(status)

    else:
      # if not aircraft :
        sense.show_message("No Data", text_colour = red)

    time.sleep(60)
