from machine import UART, Pin
import time
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522
import machine
import _thread
import time
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import machine, onewire, ds18x20, time
from machine import Pin
import utime
from machine import Pin
import time
import utime
from utime import sleep
red_led = Pin(9, Pin.OUT)
green_led = Pin(10, Pin.OUT)
sensor = Pin(27, Pin.IN, Pin.PULL_DOWN)
pump1 = Pin(26, Pin.OUT)
pump2 = Pin(20, Pin.OUT)
#ตัดน้ำ
PP33=Pin(28,Pin.IN)
ledr = Pin(9, Pin.OUT)
ledg = Pin(10, Pin.OUT)

def ESP8266Read():
    data=uart.readline()
    if data is not None:
        print(data.decode('UTF8'))
    time.sleep(0.1)
    
uart = UART(0,baudrate=115200, tx=Pin(16), rx=Pin(17))
time.sleep(1.0)
uart.write('SETWIFI,"Pimrada R109","0903319646"')   #กำหนด ตัวรับ WIFI
time.sleep(1.0)
#uart.write('SUB,"/ESP/LED1"') เลือก TOPIC ที่ต้องรับข้อมูลหรือรับข้อมูล
#time.sleep(1.0)
#uart.write('PUB,"22/99/33","test"') #เลือก TOPIC ที่ต้องส่งข้อมูลหรือรับข้อมูล
#_thread.start_new_thread(ESP8266Read(), ()) # starts the webserver in a _thread

led = Pin(25, Pin.OUT)
true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(6, Pin.OUT)
mosi = Pin(7, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(22, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0xeb29f82d"
card2 = "0x12ac531b"
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
ledr = Pin(9, Pin.OUT)
ledg = Pin(10, Pin.OUT)


ds_pin = machine.Pin(13)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
print('Found a ds18x20 device')
 
ds_sensor.convert_temp()
time.sleep_ms(300)


def monitor(show):
    show = str(show)
    showmoni = "    "+ show
    
    I2C_ADDR     = 0x27
    I2C_NUM_ROWS = 2
    I2C_NUM_COLS = 16

    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

    lcd.putstr(showmoni)


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
                temp_test()
                print("card 1 ok ")
                uart.write('PUB,"22/06","ON"')
                
            elif uid == card2:
                true.toggle()
                time.sleep(1)
                print("card 2 ok")
           
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
def temp_test():
    ds_sensor.convert_temp()
    time.sleep_ms(300)
          
    for rom in roms:
          show = ds_sensor.read_temp(rom)
          #print(ds_sensor.read_temp(rom))
          float(show)
          if(show>25):
              monitor(show)
              show = str(show)
              gg = 'PUB,"22/06",' + '"' + show + '"'
              print(gg)
              uart.write(gg)
              time.sleep(15)
          else:
              monitor(show)
              
def pump_on():
    red_led.value(1)
    green_led.value(0)
    pump1.value(1)
    time.sleep(5)
    
def pump_off():
    red_led.value(0)
    green_led.value(1)
    pump1.value(0)
    
def pump_on2():
    red_led.value(1)
    green_led.value(0)
    pump2.value(1)
    time.sleep(5)
    
    
def pump_off2():
    red_led.value(0)
    green_led.value(1)
    pump2.value(0)
    
    
def pump33():
    gg = 0
    if PP33.value()==1:
        if gg == 0:
            print("p2 active")
            ledr.high()
            ledg.low()
            pump_off()
            pump_on2()
            sleep(1)
        if  gg!= 0:
            pump_off2()
            pump_off()
            print("p2 and p1 off")
     
        gg = gg + 1        
    if PP33.value()==0 :
        print("p1 active")
        ledg.high()
        ledr.low()
        pump_on()
        sleep(1)
        if gg != 0:
            pump_off2()
            pump_off()
            print("p2 and p1 off") 
    
while True:
    temp_test()
    time.sleep(2)
    card_scan()
    time.sleep(2)
    print(uart.read())
    time.sleep(2)
    AA = b'MESSAGE,"22/06","ON"\r\n'
    if uart.read() == AA:
        green_led.value(1)
        red_led.value(0)
        pump33()
        print(pump_on())
        time.sleep(5)

    else:
        red_led.value(1)
        green_led.value(0)