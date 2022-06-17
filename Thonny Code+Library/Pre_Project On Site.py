from machine import UART, Pin, PWM, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import machine
import _thread
import time
import utime
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522
from SG90 import Servo

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

led_red = Pin(0,Pin.OUT)
led_green = Pin(1,Pin.OUT)
trigger = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN)
pwm = PWM(Pin(27))
true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(6, Pin.OUT)
mosi = Pin(7, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(22, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0xe3088734"
card2 = "0x4bfff02d"
buzzer =PWM(Pin(18))

MIN = 650000
MID = 1500000
MAX = 3000000

pwm.freq(50)
pwm.duty_ns(MID)

def card_1():
    lcd.putstr('LOTTER Passed')
    utime.sleep(1)
    lcd.clear()
    print('LOTTER Passed')
    
def card_2():
    lcd.putstr('BEST Passed')
    utime.sleep(1)
    lcd.clear()
    print('BEST Passed')
    
def open_Scaning():
    for i in range(4):
        buzzer.duty_u16(900000)
        utime.sleep_ms(40)
        buzzer.duty_u16(0)
        utime.sleep_ms(40)
        led_red.low()
        led_green.high()
        
def close_warning():
    for i in range(2):
        buzzer.duty_u16(900000)
        utime.sleep_ms(100)
        buzzer.duty_u16(0)

def open_door():
    pwm.duty_ns(MAX)
    utime.sleep(1)

def close_door():
    pwm.duty_ns(MID)
    utime.sleep(4)

def card_scan():
    rdr = MFRC522(spi, sda, rst)
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1:
                true.toggle()
                time.sleep(1)
                open_Scaning()
                card_1()
                open_door()
            elif uid == card2:
                true.toggle()
                time.sleep(1)
                open_Scaning()
                card_2()
                open_door()
            else:
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(1)
                close_warning()

while True:
    card_scan()
    led_red.high()
    led_green.low()
    close_door()