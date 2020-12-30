#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-26-2020

# This script imports the json data and prints it

from urllib.request import urlopen

import json
json = json.loads(urlopen('http://192.168.0.113/dump1090-fa/data/aircraft.json').read())
print (json)

