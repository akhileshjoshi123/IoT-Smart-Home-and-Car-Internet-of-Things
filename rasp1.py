import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


from geopy.geocoders  import Nominatim
from geopy.distance import vincenty
from random import randint
from datetime import datetime

import RPi.GPIO as GPIO
import os, json
import uuid

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

Broker = "34.208.211.241"
sub_topic = "subscribe_topic"    # receive messages on this topic

pub_topic = "publish_topic"       # send messages to this topic


geolocator = Nominatim()
HomeLocation = raw_input("\n\nPlease Enter your home location : ")
location = geolocator.geocode(HomeLocation)

home_loc_cordinates = str(location.latitude) + "," +  str(location.longitude)

time.sleep(2)
print "Home_loc_cordinates :" + home_loc_cordinates + '\n'
print "\nHome Address :", location.address, '\n'
#latitude,longitude = home_loc_cordinates.split(",")
print "Home Latitude : ",location.latitude ,"Home Longitude: ",location.longitude

curr_latitude = location.latitude - 2

near_home_latitude = location.latitude - 1

#initial_RPM = 20
#initial_CFM = 1000

#CFM =initial_CFM ; #setting the sir flow rate
#rpm= initial_RPM ;

############### MQTT section ##################

# when connecting to mqtt do this;

client = mqtt.Client()
client.connect(Broker, 1883)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(sub_topic)

def on_message(client, userdata, msg):
    message = str(msg.payload)
    if message == "On":
        print(msg.topic+" "+message)
        GPIO.output(17, True)
    elif message == "Off":
        print(msg.topic+" "+message)
    else:
        print(msg.topic+" "+message)

print "Before Connect"
client.on_connect = on_connect
client.on_message = on_message

client.loop_start()
#client.subscribe(sub_topic)

client.publish(pub_topic, "Home Address")
client.publish(pub_topic, str(home_loc_cordinates))


client.publish(pub_topic, "Other co-ordinates")


while curr_latitude <= near_home_latitude :
        time.sleep(1)
        p = randint(80,150)
        CFM_new = (p/20) * 1000
        CFM=CFM_new
        rpm=p
        curr_latitude = curr_latitude + 0.1
        cur_loc_cordinates = str(curr_latitude) + "," +  str(location.longitude)
        lat,longi = cur_loc_cordinates.split(",")
        tme = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print ("At", tme, "we are at:", cur_loc_cordinates)
        client.publish(pub_topic, str(cur_loc_cordinates))
        print ("At", tme, "RPM:", p)
        r = "RPM" + str(p)
        client.publish(pub_topic, r)
        afr = round(CFM_new,2)
        a = "AFR" + str(afr)
        print ("At", tme, "air flow rate:", afr )
        client.publish(pub_topic, a)

#client.loop_forever()
#client.on_connect = on_connect
#client.on_message = on_message
#client.on_subscribe = on_subscribe
client.loop_forever()


