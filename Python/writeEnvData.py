#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-30-2020

# This script pulls the JSON data and sends it to a ThingSpeak channel
# It also sends the sensor and system data to ThingSpeak and displays a message
# on the SenseHat relative to what information is available.

from urllib.request import urlopen
import json
import time
from sense_hat import SenseHat
import requests
from subprocess import check_output
from re import findall

# Import for the system information
import psutil

# ThingSpeak API PiAware channel key
WRITE_API_KEY='8I224HGCPZE8CG6Y'

# ThingSpeak ThingTweetURL & channel API key
baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

# clear sensehat and intialise light_state
sense.clear()

# api -endpoint
URL = 'http://192.168.0.113/dump1090-fa/data/aircraft.json'

# Determine the colour for the SenseHat messages
green =(0, 255, 0)
red = (255, 0, 0)

# CPU Temperature
def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

# Disk Usage
def get_disk_usage():
    return str(psutil.disk_usage('/').percent)

# Memory Usage
def get_memory_usage():
    return str(psutil.virtual_memory().percent)

# CPU Usage
def get_cpu_usage():
    return str(psutil.cpu_percent(interval=None))

def writeData(status,temp,press,hum,cputemp,disk,mem,usage):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s&field7=%s&field8=%s' % (status,temp,press,hum,cputemp,disk,mem,usage))
    print(conn.read())
    # Closing the connection
    conn.close()

# If statement to search the json array
# The sense hat displays Data Detection - Green or No data - Red,  
# depending on the information stored in the URL array

while True:
    r = requests.get(url = URL)
    data = r.json()

    flightData = data["aircraft"]
    print("Aircraft data: "+str(flightData))

    temp=round(sense.get_temperature(),2)
    press=round(sense.get_pressure(),2)
    hum=round(sense.get_humidity(),2)
    cputemp=get_temp()
    disk=get_disk_usage()
    mem=get_memory_usage()
    usage=get_cpu_usage()

    if flightData:
        sense.show_message("Data Detection!", text_colour = green)
        status = 1
        writeData(status,temp,press,hum,cputemp,disk,mem,usage)

    else:
        sense.show_message("No Data", text_colour = red)
        status=0
        writeData(status,temp,press,hum,cputemp,disk,mem,usage)

    #Testing every 15 minutes
    time.sleep(60*15)
