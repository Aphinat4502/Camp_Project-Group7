from machine import Pin, PWM
import time

PP33=Pin(28,Pin.IN)
pump1 = Pin(21, Pin.OUT)
pump2 = Pin(22, Pin.OUT)

def pump_water():
    def pump_on():
        red_led.value(0)
        green_led.value(1)
        pump1.value(0)
        time.sleep(2)
    
    def pump_off():
        red_led.value(1)
        green_led.value(0)
        pump1.value(1)
    
    def pump_on2():
        red_led.value(0)
        green_led.value(1)
        pump2.value(0)
        time.sleep(2)
    
    
    def pump_off2():
        red_led.value(1)
        green_led.value(0)
        pump2.value(1)
    
    gg = 0
    stop =True
    while stop ==True:
        if PP33.value()==1:
            if gg == 0:
                print("p2 active")
                red_led.value(0)
                green_led.value(1)
                pump_off()
            
            
                pump_on2()
                gg = 1 
            if gg == 2:
                pump_off2()
                pump_off()
                print("gg p2 and p1 off")
                gg = 3
            
        if PP33.value()==0 :
            if gg == 1:
                print("p1 active")
                red_led.value(0)
                green_led.value(1)
                pump_on()
                gg = 2
                sleep(1)
            if gg == 3:
                pump_off2()
                pump_off()
                print("p2 and p1 off no active")
                stop = False