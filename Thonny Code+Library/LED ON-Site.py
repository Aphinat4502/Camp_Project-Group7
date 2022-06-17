from machine import Pin
from time import sleep

led_blue = Pin(0,Pin.OUT)

while True:
    led_blue.high()
    sleep(1)
    led_blue.low()
    sleep(1)
    