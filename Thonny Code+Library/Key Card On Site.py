from machine import UART, Pin, PWM, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import machine
import _thread
import time
import utime
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

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

def card_1():
    lcd.putstr('Card 1 Complete')
    print('Card 1 Complete')
    
def card_2():
    lcd.putstr('Card 2 Complete')
    print('Card 2 Complete')
    
def pippip_card1():
    for i in range(3):
        buzzer.duty_u16(800000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        
def pippip_card2():
    for i in range(1):
        buzzer.duty_u16(800000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        
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
                pippip_card1()
                card_1()
            elif uid == card2:
                true.toggle()
                time.sleep(1)
                pippip_card2()
                card_2()
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


while True:
    card_scan()
    
        