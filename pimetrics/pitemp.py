#!/usr/bin/python3

# Author: Adelle McAteer
# Version: 1
# Date: 12-30-2020

# This script shows the current CPU temperature in degress celsius
# Code was taken from a referenced online source 

import os

def main():
    print('Current CPU temperature is {:.2f} degrees Celsius.'.format(get_cpu_temp()))

def get_cpu_temp():
    # Obtains the current value of the CPU temperature.
    #:returns: Current value of the CPU temperature if successful, zero value otherwise.

    result = 0.0

    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.

    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()

        # Test if the string is an integer as expected.
        if line.isdigit():

            # Convert the string with the CPU temperature to a float in degrees Celsius.
            result = float(line) / 1000
    # result return
    return result
if __name__ == "__main__":
    main()
