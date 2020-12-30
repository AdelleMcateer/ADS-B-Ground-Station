#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-30-2020

from urllib.request import urlopen
import json
import time
from sense_hat import SenseHat
import requests

#ThingSpeak API PiAware channel key
WRITE_API_KEY='8I224HGCPZE8CG6Y'

#ThingSpeak ThingTweetURL & channel API key
baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

#clear sensehat and intialise light_state
sense.clear()

#api -endpoint
URL = 'http://192.168.0.113/dump1090-fa/data/aircraft.json'

green =(0, 255, 0)
red = (255, 0, 0)

def writeData(status,temp,press,hum):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s' % (status,temp,press,hum))
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

    temp=round(sense.get_temperature(),2)
    press=round(sense.get_pressure(),2)
    hum=round(sense.get_humidity(),2)
    #writeData(temp,press,hum)

    if flightData:
        status = 1
       # temp=round(sense.get_temperature(),2)
        writeData(status,temp,press,hum)
        sense.show_message("Data Detection!", text_colour = green)

    else:
      # if not aircraft :
        status=0
        writeData(status,temp,press,hum)
        sense.show_message("No Data", text_colour = red)

    #Testing every 30 minutes
    time.sleep(60*15)
