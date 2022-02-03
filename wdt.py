## Simple software WDT implementation
import machine
from micropython import const

wdt_timeout= const(10)
class mywdt:
    def __init__(self):
        self.wdt_counter = 0
        self.wdt_timer=None

    def _callback(self):
        self.wdt_counter += 1
        if (self.wdt_counter >= wdt_timeout):
            machine.RTC().memory('my wdt reset')
            machine.reset()  ## softreset =4

    def feed(self):
        self.wdt_counter = 0

    def start(self):
        machine.RTC().memory('my wdt running')
        wdt_timer = machine.Timer(-1)
        wdt_timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=lambda t:self._callback())
        self.wdt_timer = wdt_timer

    def stop(self):
        if self.wdt_timer != None:
            self.wdt_timer.deinit()
        self.wdt_timer=None
        self.wdt_counter = 0

## END Simple software WDT implementation

'''
nachdem der watchdog mit ' wdt_start()' gestartet wurde, muss spaetestens nach 10 sekunden wieder 'wdt_feed()' aufgerufen werden.
falls ein programmteil sich aufhaengt oder mehr als 10 sekunden benoetigt, wird vom watchdog ein reset ausgeloest. der reset
erfolgt ueber 'machine.reset()' . Die CPU startet mit 'boot.py' neu mit der
meldung  'ets Jan  8 2013, rst cause:4, boot mode:(3,0) wdt reset '.
'''