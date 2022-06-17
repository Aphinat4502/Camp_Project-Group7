from machine import Pin, PWM
import utime

led_red = Pin(0,Pin.OUT)
led_green = Pin(1,Pin.OUT)
trigger = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)
pwm = PWM(Pin(27))
buzzer = PWM(Pin(18))

MIN = 650000
MID = 1500000
MAX = 3000000

pwm.freq(50)
pwm.duty_ns(MID)

def open_warning():
    for i in range(2):
        buzzer.duty_u16(900000)
        utime.sleep_ms(100)
        buzzer.duty_u16(0)
        utime.sleep_ms(100)
        
def close_warning():
    for i in range(1):
        buzzer.duty_u16(900000)
        utime.sleep_ms(100)
        buzzer.duty_u16(0)

def open_door():
    pwm.duty_ns(MAX)
    utime.sleep(0.1)

def close_door():
    pwm.duty_ns(MID)
    utime.sleep(0.1)

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
    if(distance < 15):
        led_red.low()
        led_green.high()
        open_warning()
        open_door()
    else:
        led_red.high()
        led_green.low()
        close_warning()
        close_door()
        