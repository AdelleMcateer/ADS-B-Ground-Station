# ADS-B-Ground-Station

Student Name: Adelle McAteer
Student Number: 20091411

Git repository located in the master branch
https://github.com/AdelleMcateer/ADS-B-Ground-Station/tree/master

Thing Speak Channel:
https://thingspeak.com/channels/1264716

YouTube Demo Video:
https://www.youtube.com/watch?v=DKgN_2fNHMk

YouTube link for Sensehat message display:
 https://www.youtube.com/watch?v=jFLCmrWethY

# Overview
A RaspberryPi set up as an ADS-B-Ground-Station used to track and collect data from flights in range.
Also uses sensor information to obtain data readings from the SenseHat for temperature, pressure and humidity.
System information about the RaspberryPi is collected to monitor CPU temperature, usage, memory and disk usage.

# Technologies and Tools
-	ThingSpeak/MQTT
-	ThingTweet/THingHTTP/React
-	Twitter 
-	IFTTT
-	Email notifications
-	Push notifications
-	Database Storage: Local & Firebase
-	Python Language
-	WiFi – to connect the RaspberyPi and transmit data

# Physical aspect
-	RaspberryPi4 with SenseHat & PiAware installed
-	Laptop
-	Mobile Phone
-	FlightAware Pro Stick Plus - FlightAware's USB SDR ADS-B Receiver with a built-in
  1090MHz bandpass filter 
-	1090MHz Desk Antenna - a 3dBi ADS-B 1090Mhz SMA Antenna with magnetic base


# Integration and how it functions:
RaspberryPi4 with PiAware installed connected to FlightAware's USB SDR ADS-B Receiver and 1090MHz Desk Antenna picks up ADS-B signals from aircraft in range. 

Raspberry Pi with a SenseHat and using a Python script displays a message: “Data Detection” when information is feeding from the PiAware URL endpoint. 
The script tests if there is JSON data available within the aircraft array.
For demonstration and data visitation purposes a message is also displayed: “No data” when no data is available.

Data is published to ThingSpeak and displayed on a public channel showing whether data was detected or not.

If data is available an email notification is sent to my mail account using ThingHTTP, IFTTT and Webhooks.

In both instance a tweet is also posted to Twitter using ThingTweet using reacts when certain conditions are met.
If data is available “Plane data detected!” is posted to Twitter.
If there is not data “No data available”. This is just for demonstration purposes and somewhat unnecessary.

# Weather/Sensor Data
The sensor data, humidity, temperature and pressure, is also published via MQTT to Thingspeak using the same script.

# MQTT Client: Publish/Subcribe to RaspberryPi system information
Using HiveMQ

# Python Script:
Python/writeEnvData.py

# Database Storage: 
# Python Scripts
Python /aircraft.py
firebase/ storeFileFB.py

# Sample storage file:
data.json
