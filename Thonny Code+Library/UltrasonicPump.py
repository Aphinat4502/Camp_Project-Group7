from machine import Pin
import time
import utime

pump = Pin(7,Pin.OUT)
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

def pump_on():
    pump.value(1)
    time.sleep(1)
    print("Pump On")
    
def pump_off():
    pump.value(0)
    time.sleep(1)
    print("Pump Off")
    
while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.tick_us()
    timepassed = signalon - signaloff
    distance = (timepassed*0.0343) / 2
    print("The distance from object is",distance,"cm")
    utime.sleep(2)
    if(distance < 10):
        pump_on()
    else:
        pump_off()