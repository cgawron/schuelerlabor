import ubinascii
import network
import time
from umqttsimple import MQTTClient
#import BME280
from BME280_1 import BME280
from machine import I2C,Pin

ssid = 'cgawron'
password = 'Schuelerlabor'
#ssid = 'deine_ssid'
#password = 'dein_passwort'
#mqtt_server = 'broker.hivemq.com'
mqtt_server = "34.194.225.123"
CHANNEL_ID    = "1533730"
WRITE_API_KEY = 'OFSMOZN1COHG6PAV'
topic_pub = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = 'testtopic/1'
#topic_pub = 'schuelerlabor/egs'

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
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
bme = BME280(address=0x77, i2c=i2c)

while True:
    ergebnis = bme.temperature, bme.humidity, bme.pressure
    print("Publishing message: " + str(ergebnis))
    payload ="field1="+str(bme.temperature)+\
            "&field2="+str(bme.humidity)+\
            "&field3="+str(bme.pressure)
#     client.publish(topic_pub + '/temperature', str(bme.temperature))
#     client.publish(topic_pub + '/humidity', str(bme.humidity))
    client.publish(topic_pub, payload)
    count += 1
    time.sleep(20)
