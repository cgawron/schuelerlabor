#test_bme.py
from machine import I2C,Pin
from  BME280_1 import BME280
from time import sleep
import batterie  


i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
bme = BME280(address=0x77, i2c=i2c)
sleep(2)

print( f'   Temperatur= {bme.temperature} Grad C')
print( f'  Luftfeuchte= {bme.humidity} rH')
print( f'    Luftdruck= {bme.pressure} hP')
print( f'Batterie Spg.= {round(batterie.volt(),2)} Volt')

blaueLed= Pin(2, Pin.OUT, value=1 )
roteLed = Pin(14, Pin.OUT, value=1 ) #aus
while True:
    blaueLed(0)
    sleep(.3)
    blaueLed(1)
    sleep(.3)
    roteLed(0)
    sleep(.3)
    roteLed(1)
    sleep(.3)