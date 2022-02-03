# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import gc
from reset import Reset
gc.collect()
reset= Reset()
print(f"\n      boot: '{reset.typ}' reset")
print( f"rtc-memory: {reset.message}" )