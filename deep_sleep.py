import machine
led = machine.Pin(2, machine.Pin.OUT)
from time import sleep

def deep_sleep_ms(msecs):
  # configure RTC.ALARM0 to be able to wake the device
  rtc = machine.RTC()
  rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

  # set RTC.ALARM0 to fire after X milliseconds (waking the device)
  rtc.alarm(rtc.ALARM0, msecs)

  # put the device to sleep
  machine.deepsleep()
  
def blink():
    led.value(0)
    sleep(.2)
    led.value(1)
#sleep(0)

# wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# you should remove this sleep line in your final script
#sleep(0) # hier ist zeit für unterbrechung mit cntrl C

#print('Im awake, but Im going to sleep')

#sleep for 10 seconds (10000 milliseconds)
#deep_sleep(60000-5000)
#deep_sleep(15000)