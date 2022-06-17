from machine import Pin
from time import sleep

led_red = Pin(14,Pin.OUT)
led_yellow = Pin(15,Pin.OUT)
led_green = Pin(16,Pin.OUT)

def red_on():
    led_red.high()
    led_yellow.low()
    led_green.low()
    sleep(3)
    
def yellow_on():
    led_red.low()
    led_yellow.high()
    led_green.low()
    sleep(1)
    
def green_on():
    led_red.low()
    led_yellow.low()
    led_green.high()
    sleep(2)

while True:
    red_on()
    yellow_on()
    green_on()