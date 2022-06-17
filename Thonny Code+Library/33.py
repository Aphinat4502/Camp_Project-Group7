# Raspberry Pi Pico - MicroPython 1x DS18X20 Sensor demo
# scruss - 2021-02
# -*- coding: utf-8 -*-
 
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
 
ds = DS18X20(OneWire(Pin(15)))
sensor_id = ds.scan()[0]  # the one and only sensor
 
while True:
    ds.convert_temp()
    sleep_ms(750)         # wait for results
    print(ds.read_temp(sensor_id), " °C")
    sleep_ms(2000)