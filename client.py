import ubinascii
import network
import time
from umqttsimple import MQTTClient


ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'
mqtt_server = 'broker.hivemq.com'
#mqqt_server = "18.194.65.151"

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = 'testtopic/1'
topic_pub = 'testtopic/1'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())


client_id = ubinascii.hexlify(machine.unique_id())
print("Client ID: " + str(client_id))


def sub_cb(topic, msg):
    print((topic, msg))


def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server, port=1883)
    client.set_callback(sub_cb)
    client.connect()
    return client


client = connect_and_subscribe()
count = 1
while True:
    print("Publishing message: " + str(count))
    client.publish(topic_pub, 'Zaehler ' + str(count))
    count += 1
    time.sleep(1)
