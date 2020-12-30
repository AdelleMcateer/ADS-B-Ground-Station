#!/usr/bin/python3
# Author: Adelle McAteer
# Version: 1
# Date: 12-30-2020

# This is a script that I found on this site:
# https://www.stuffaboutcode.com/2015/10/piaware-aircraft-overhead-led.html
# It is a work in progress and I have amended it somewhat to get it to print the current
# json info to the Pi shell

from urllib.request import urlopen
import json
from time import sleep

#json = json.loads(urlopen('http://192.168.0.113/dump1090-fa/data/aircraft.json').read())

DUMP1090DATAURL = "http://192.168.0.113/dump1090-fa/data/aircraft.json"
#print (json)

class FlightData():
    def __init__(self, data_url = DUMP1090DATAURL):

        self.data_url = data_url

        self.refresh()

    def refresh(self):
        #open the data url
        self.req = urlopen(self.data_url)

        #read data from the url
        self.raw_data = self.req.read()

        #encode the data - updated "utf8"
        encoding = self.req.headers.get_content_charset("utf8")

        #load in the json
        self.json_data = json.loads(self.raw_data.decode(encoding))

        self.aircraft = AirCraftData.parse_flightdata_json(self.json_data)

# Define the aircraft date
class AirCraftData():
    def __init__(self,
                 hex,
                 flight):

        self.hex = hex
        self.flight = flight

    @staticmethod
    def parse_flightdata_json(json_data):
        aircraft_list = []
        print(json.dumps(json_data,sort_keys=True,indent=2))
        for aircraft in json_data:
            aircraftdata = AirCraftData(
                aircraft[0],
                aircraft[0])
            aircraft_list.append(aircraftdata)
        return aircraft_list

#test
if __name__ == "__main__":
    #create FlightData object
    myflights = FlightData()
    while True:
        #loop through data found in the aircraft array
        for aircraft in myflights.aircraft:
        #print the aircraft's data
            print(aircraft.hex)
            print(aircraft.flight)
       # Repeat every 5 minutes for testing purposes, based on current location 15-30 mins will 
       # likely be a better timeframe
        sleep(60*5)

        #refresh the flight data
        myflights.refresh()



