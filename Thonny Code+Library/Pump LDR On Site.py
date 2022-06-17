from machine import ADC, Pin
import time
from time import sleep

pump = Pin(22,Pin.OUT)
photoPIN = 26

def readLight(photoGP):
    photoRes = ADC(Pin(26))
    light = photoRes.read_u16()
    light = round(light/65553*100,2)
    return light

def pump_off():
    pump.value(0)
    print("On")
    
def pump_on():
    pump.value(5)
    print("Off")
    
while True:
    print("light: " + str(readLight(photoPIN))+"%")
    sleep(1)
    if(readLight(photoPIN)) <= 50:
        pump_on()
    else:
        pump_off()
        