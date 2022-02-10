# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import gc
gc.collect()
from reset import Reset
reset= Reset(info=1)
print(f"\n      boot: '{reset.typ}' reset")
print( f"rtc-memory: {reset.message}" )