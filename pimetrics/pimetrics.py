#!/usr/bin/env python3

# Scipt to read the RaspberryPi information 

#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from urllib.parse import urlparse
import sys
import time
import json
from sense_hat import SenseHat
from subprocess import check_output
from re import findall
import psutil

sense = SenseHat()
sense.clear()

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    print("Message ID: " + str(mid))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# parse mqtt url for connection details
url_str = sys.argv[1]
print(url_str)
url = urlparse(url_str)
base_topic = url.path[1:]

# Connect
if (url.username):
    mqttc.username_pw_set(url.username, url.password)

mqttc.connect(url.hostname, url.port)
mqttc.loop_start()

# CPU Temperature
def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])
    print(get_temp())

# Disk Usage
def get_disk_usage():
    return str(psutil.disk_usage('/').percent)
    print(get_disk_usage())

# Memory Usage
def get_memory_usage():
    return str(psutil.virtual_memory().percent)
    print(get_memory_usage())

# CPU Usage
def get_cpu_usage():
    return str(psutil.cpu_percent(interval=None))
    print(get_cpu_usage())

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

while True:
    metrics=json.dumps({"CPU temperature": get_temp(),"Disk Usage %": get_disk_usage(), "Memory Usage %": get_memory_usage(),"CPU usage %": get_cpu_usage(), "timestamp":time.time()})
    mqttc.publish(base_topic+"/Pi Metrics", metrics)
    time.sleep(15)

   # mqttc.publish(base_topic+"/CpuTemp", get_temp())
   # mqttc.publish(base_topic+"/DiskUsagePercent", get_disk_usage())
   # mqttc.publish(base_topic+"/MemoryUsagePercent", get_memory_usage())
   # mqttc.publish(base_topic+"/CpuUsagePercent", get_cpu_usage())
   # time.sleep(15)

