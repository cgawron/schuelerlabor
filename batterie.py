# batterie.py

import machine
from time import sleep

def volt():
        return 5.0*machine.ADC(0).read() /944
    # bei 5V 944 gemessen ,empirisch

if __name__=='__main__':
    from time import sleep
    while True:
        print( volt() )
        sleep(1)