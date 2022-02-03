import machine

class Reset:
    def __init__(self):
        self._typ = self.gettyp()
        self._message= machine.RTC().memory().decode()
    def gettyp(self):
        x=machine.reset_cause()
        y='unbekannter'
        if x==6:
            y="hardware"
        elif x==5:
            y="deepsleep"
        elif x==0:
            y="poweron"
        elif x==4:
            y="software"
        elif x==1:
            y= "watchdog"
        return y
    
    @property
    def typ(self):
        return self._typ

    @property
    def message(self):
        return self._message 
        
    