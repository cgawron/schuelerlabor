from machine import reset_cause,DEEPSLEEP,RTC,deepsleep,reset,I2C,Pin
from   time import sleep,time
import network
import sys
from   BME280_1 import BME280
import batterie
from   send_thingspeak2 import send
from   wdt import mywdt
from reset import Reset

blaueLed= Pin(2, Pin.OUT, value=1 )
roteled = Pin(14, Pin.OUT, value=1 ) #aus

class Schlafen:
    def __init__(self,*, minuten=0):
        self._en=0
        self.rtc = RTC()
        self.zeit(minuten)      
        self.rtc.irq(trigger=self.rtc.ALARM0, wake=DEEPSLEEP)
    def zeit(self,minuten=10.0):
        self._minuten=minuten
        if minuten > 0:
            self._en=True
        else:
            self._en=False
        ms= int(self._minuten*60*1000)
        self.rtc.alarm(self.rtc.ALARM0, ms )
    def jetzt(self):
        if self._en:           
            print( "{} Minuten schlafen...".format(self._minuten))
            deepsleep()
            sleep(1) ##???
        else:
            print( 'deepsleep nicht freigegeben')
            wdt.stop()
            sys.exit()

bme=None
def start_bme():
    global bme
    try:
        # i2c sensor bme-280
        i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
        bme = BME280(address=0x77, i2c=i2c)    # abweichend vom standard: adr=0x77
        sleep(2)
    except Exception as e:
        y='?'
        if e.args[0]==19:
            y='Kein solches Geraet'
        raise Exception('BME, i2c :', y)

def messwerte():
    #messwerte lesen
    t = bme.temperature
    h = bme.humidity
    d = bme.pressure
    v = round(batterie.volt(),2)
    return t,h,d,v

def blink(led= blaueLed):   # 0.1 sec
    sleep(.07)
    led.value(0)
    sleep(.02)
    led.value(1)



def schlaf_nach_fehler(e='alles ok'):
    print ('*** Fehler:',e)
    wdt.stop()
    blink(roteled) 
    schlaf.jetzt() 

## hier start #########################################
print('...client')
if __name__ == '__main__':
    schlaf= Schlafen(minuten=0)
else:
    schlaf= Schlafen(minuten=10)
reset=Reset()
wdt= mywdt()
wdt.start()
if reset.typ== "watchdog":   # kommt dann, wenn Batterie im tiefschlaf abgeklemmt wird
    schlaf.zeit(0.02)
    schlaf_nach_fehler('watchdog')
try:
    start_bme()
except Exception as e:
    schlaf_nach_fehler(e)
 
for i in range(10): # 10sec, um kb interrupt zu ermoeglichen
    blink()
    
WiFi_SSID, WiFi_PW= "dk2jk","dk2jk X1"
try:               
    sta = network.WLAN(network.STA_IF)
    if sta.active() and sta.isconnected():   # schon verbunden ?
        print ( 'verbunden mit "{}"'.format( sta.ifconfig()[0] ))
    else:
        # neu verbinden
        try:
            sta.active(True)
            sta.connect(WiFi_SSID, WiFi_PW)
        except Exception as e:
            schlaf_nach_fehler(e) # verbindung hat nicht geklappt
            
        now=time()
        timeout=9
        wdt.feed()
        count=0
        while not sta.isconnected (): # im abstand von 1 sec versuchen
            sleep(1)
            count=count+1
            print('{}'.format(count),end=' ') # ...
            if  count >= timeout:
                schlaf_nach_fehler('WLAN timeout!')
                break
    try:
        t,h,d,v=messwerte()
        send(t,h,d,v)
    except:
        schlaf_nach_fehler('send()')
    finally:
        schlaf.jetzt()
    #ende
        
except KeyboardInterrupt:
    print( "kb interrupt erlaubt, stop hier")
except Exception as e:
    schlaf_nach_fehler(e) 
    #ende
