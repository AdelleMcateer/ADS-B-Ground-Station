#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-26-2020

# This script runs through the PiAware Array and posts a message to the sense hat

import requests
import json

from time import sleep
import time
from sense_hat import SenseHat

sense = SenseHat()

#clear sensehat and intialise light_state
sense.clear()

green = (0, 255, 0)
red = (255,0,0)

#api -endpoint
URL = 'http://192.168.1.123/dump1090-fa/data/aircraft.json'

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
    else:
      # if not aircraft :
        sense.show_message("No Data", text_colour = red)

    time.sleep(60)
