
 
 
 
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms


# จอ LCD
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

 
ds = DS18X20(OneWire(Pin(15)))
sensor_id = ds.scan()[0]  # the one and only sensor


 
def Dss():
    ds.convert_temp()
    sleep_ms(750)         # wait for results
    print(ds.read_temp(sensor_id), " °C")
    sleep_ms(2000)

 
while True:
    Dss()
    
