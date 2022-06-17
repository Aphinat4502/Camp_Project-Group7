from machine import Pin, PWM
import utime

trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)
buzzer = PWM(Pin(18))

def sound_on():
    for i in range(2):
        buzzer.duty_u16(700000)
        utime.sleep_ms(100)
        buzzer.duty_u16(0)
        utime.sleep_ms(100)

def sound_off():
    for i in range(2):
        buzzer.duty_u16(0)
        utime.sleep_ms(100)

while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed*0.0343) / 2
    print("The distance from object is",distance,"cm")
    utime.sleep(1)
    if(distance <= 10):
        sound_on()
   
        
    
        
    