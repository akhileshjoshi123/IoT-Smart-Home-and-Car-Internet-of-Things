import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import re
import string

coordList=[]
airFlowList=[]
rpmList=[]

Broker = "34.208.211.241"

sub_topic = "subscribe_topic"    # receive messages on this topic

pub_topic = "publish_topic"       # send messages to this topic

# mqtt section

# when connecting to mqtt do this;
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(pub_topic)

# when receiving a mqtt message do this;
def on_message(client, userdata, msg):
    message = msg.payload
    pattern_one = re.compile('[A-Za-z]+')
    all=string.maketrans('','')
    nodigs=all.translate(all, string.digits)
    if "AFR" in message :
        message.translate(all, nodigs)
        afr = int(message)
        print afr
        airFlowList.append(afr)
    elif "RPM" in message :
        message.translate(all, nodigs)
        rpm = int(message)
        print rpm
        rpmList.append(rpm)
        if rpm<=100:
            publish_mqtt("Normal Air Flow")
            print "Normal Air Flow"
        else:
            publish_mqtt("Abnormal Air Flow")
            print "Abnormal Air Flow"                                                                                                                    
    elif pattern_one.match(message):
        print "Just Text"
    else:
        if ',' in message:
            longitude,lat = message.strip().split(',')
            coordList.append(float(longitude)-1)
            compareCoordinates(coordList)
        else:
            rpm = int(message)
            if rpm<=100:
                publish_mqtt("Normal Air Flow")
                print "Normal Air Flow"
            else:
                publish_mqtt("Abnormal Air Flow")
                print "Abnormal Air flow"

    #print coordList
    print(msg.topic+" "+message)
# to send a message
def compareCoordinates(myList):
    if len(myList)==11:
        print myList
        for i in range(1,11):
            if myList[0]-myList[i] <= 1:
                publish_mqtt("On")
                print "On"
            else:
                publish_mqtt("Off")

def publish_mqtt(msg):
    mqttc = mqtt.Client()
    mqttc.connect(Broker, 1883)
    mqttc.publish(sub_topic, msg)
    #mqttc.loop(2) //timeout = 2s

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, 1883, 60)
client.loop_forever()