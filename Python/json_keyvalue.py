#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-30-2020

# A simple script to check the json array for cetain key/value pairs

import urllib.request
import json

# Metod to get a response from the URL
def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

# Main function to retrieve Hex, Flight & Sqiawk from the json data
# If available, otherwise no details are available

def main():

    urlData = "http://192.168.0.113/dump1090-fa/data/aircraft.json"
    jsonData = getResponse(urlData)
    # print the state id and state name corresponding
    for i in jsonData["aircraft"]:
        print(f'Hex:  {i["hex"]} , Flight: {i["flight"]} , Squawk : {i["squawk"]}')
    else:
        print("No details")

if __name__ == '__main__':
    main()
