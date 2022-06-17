from machine import Pin, PWM
import time

wlls=Pin(9,Pin.IN)
pump1 = Pin(5,Pin.OUT)
pump2 = Pin(7,Pin.OUT)

def pump_on():
    pump1.value(1)
    pump2.value(1)
    time.sleep(1)
    print("Pump On")
    
def pump_off():
    pump1.value(0)
    pump2.value(0)
    time.sleep(1)
    print("Pump Off")

wlls = 1
stop = True
while stop ==True:
        if wlls == 0:
            print("wlls p2 and p1 on")
            pump_on()
        if wlls == 1:
            print("wlls p2 and p1 off")
            pump_off()
            stop = False
    
