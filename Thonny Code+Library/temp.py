from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
 
ds = DS18X20(OneWire(Pin(17)))
sensor_id = ds.scan()[0]  # the one and only sensor
 
while True:
    ds.convert_temp()
    sleep_ms(750)         # wait for results
    print(ds.read_temp(sensor_id), " Â°C")
    sleep_ms(2000)