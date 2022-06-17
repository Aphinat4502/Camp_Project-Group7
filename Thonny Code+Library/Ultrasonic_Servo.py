from machine import Pin, PWM
import utime

trigger = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)
pwm = PWM(Pin(27))

MIN = 650000
MID = 1500000
MAX = 3000000

pwm.freq(50)
pwm.duty_ns(MID)

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
    utime.sleep(1)
    if(distance < 7):
        pwm.duty_ns(MAX)
        utime.sleep(0.1)
    else:
        pwm.duty_ns(MID)
        utime.sleep(0.1)