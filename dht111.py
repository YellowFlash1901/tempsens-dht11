import paho.mqtt.client as mqtt

import time

import sys

import Adafruit_DHT

 

time.sleep(30)

 

username = "b0750020-2218-11ec-9f5b-45181495093e USERNAME"

password = "a37fcf292c148e5a0770b360f3af620686ec77f2 PASSWORD"

clientid = "81554a60-2219-11ec-ad90-75ec5e25c7a4"

 

mqttc = mqtt.Client(client_id=clientid)

mqttc.username_pw_set(username, password=password)

mqttc.connect("mqtt.mydevices.com", port=1883, keepalive=60)

mqttc.loop_start()

 

topic_dht11_temp = "v1/" + username + "/things/" + clientid + "/data/1"

topic_dht11_humidity = "v1/" + username + "/things/" + clientid + "/data/2"

 

 

while True:

    try:

        humidity11, temp11 = Adafruit_DHT.read_retry(11, 17)   

      

       

        if temp11 is not None:

            temp11 = "temp,c=" + str(temp11)

            mqttc.publish(topic_dht11_temp, payload=temp11, retain=True)

        if humidity11 is not None:

            humidity11 = "rel_hum,p=" + str(humidity11)

            mqttc.publish(topic_dht11_humidity, payload=humidity11, retain=True)

      

        time.sleep(5)

    except (EOFError, SystemExit, KeyboardInterrupt):

        mqttc.disconnect()

        sys.exit()
