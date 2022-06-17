from machine import Pin
from time import sleep

led_red = Pin(14,Pin.OUT)
led_blue = Pin(15,Pin.OUT)
led_white = Pin(16,Pin.OUT)

while True:
    led_red.high()
    sleep(0.5)
    led_red.low()
    sleep(0.5)
    led_blue.high()
    sleep(0.5)
    led_blue.low()
    sleep(0.5)
    led_white.high()
    sleep(0.5)
    led_white.low()
    sleep(0.5)
