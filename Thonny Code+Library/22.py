

from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms

ds_pin = machine.Pin(15)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found a ds18x20 device')

