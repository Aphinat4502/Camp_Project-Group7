from machine import Pin
from time import sleep

led_blue = Pin(0,Pin.OUT)
led_white = Pin(6,Pin.OUT)
led_yellow = Pin(10,Pin.OUT)

while True:
    led_blue.high()
    led_white.high()
    led_yellow.high()
    sleep(0.5)
    led_blue.low()
    led_white.low()
    led_yellow.low()
    sleep(0.5)