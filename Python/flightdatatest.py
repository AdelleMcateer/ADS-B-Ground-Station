# Author: Adelle McAteer
# Version: 1
# Date: 12-10-2020

# A test script to import the json data from the PiAware feed

from urllib.request import urlopen

import json
json = json.loads(urlopen('http://192.168.1.123/dump1090-fa/data/aircraft.json').read())
print (json)

