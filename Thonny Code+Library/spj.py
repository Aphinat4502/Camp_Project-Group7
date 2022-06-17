from machine import UART, Pin
import time
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522
from NetworkHelper import NetworkHelper
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
from machine import Pin, PWM
from utime import sleep

trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
led = Pin(5, Pin.OUT)
red_led = Pin(0, Pin.OUT)
green_led = Pin(1, Pin.OUT)

led = Pin(25, Pin.OUT)
true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(6, Pin.OUT)
mosi = Pin(7, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(19, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = "0xe3088734"
card2 = "0x12ac531b"

PP33=Pin(28,Pin.IN)
pump1 = Pin(21, Pin.OUT)
pump2 = Pin(22, Pin.OUT)

buzzer = PWM(Pin(11))
red_led = Pin(10, Pin.OUT)
green_led = Pin(9, Pin.OUT)

tones = {
"D6": 1175,
}

song = ["D6","D6"]



ds_pin = machine.Pin(13)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found a ds18x20 device')

ds_sensor.convert_temp()
time.sleep_ms(300)


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
                playsong(song)
                print("card 1 ok ")
                
                
            elif uid == card2:
                true.toggle()
                time.sleep(1)
                print("card 2 ok")
                playsong(song)
           
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
                




    
def playtone(frequency):
    buzzer.duty_u16(100000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
            red_led.low()
            green_led.high()
            time.sleep(2)
        else:
            playtone(tones[mysong[i]])
            red_led.high()
            green_led.low()
        sleep(0.3)
    bequiet()

def pump_water():
    def pump_on():
        red_led.value(0)
        green_led.value(1)
        pump1.value(0)
        time.sleep(2)
        print('on')
    def pump_off():
        red_led.value(1)
        green_led.value(0)
        pump1.value(1)
    
    def pump_on2():
        red_led.value(0)
        green_led.value(1)
        pump2.value(0)
        time.sleep(2)
    
    
    def pump_off2():
        red_led.value(1)
        green_led.value(0)
        pump2.value(1)
    
    gg = 0
    stop =True
    while stop ==True:
        if PP33.value()==1:
            if gg == 0:
                print("p2 active")
                red_led.value(0)
                green_led.value(1)
                pump_off()
            
            
                pump_on2()
                gg = 1 
            if gg == 2:
                pump_off2()
                pump_off()
                print("gg p2 and p1 off")
                gg = 3
            
        if PP33.value()==0 :
            if gg == 1:
                print("p1 active")
                red_led.value(0)
                green_led.value(1)
                pump_on()
                gg = 2
                sleep(1)
            if gg == 3:
                pump_off2()
                pump_off()
                print("p2 and p1 off no active")
                stop = False
   
   
   
   
   
def getApi(host, path, param=""):
    print("\r\n\r\n")
    print("Now it's time to start HTTP Get/Post Operation.......\r\n")
    # host = "192.168.1.2"  # host
    # path = "/"  # path  ?? url
    #param = ""
    if param != "":
        path = path + "?" + param
    else:
        path = path
    timeout = 0
    # default delay get api delay 3 sec
    while timeout < 3:
        httpCode, httpRes = con.doHttpGet(host, path,delay=1)
        print(
            "-----------------------------------------------------------------------------"
        )
        print("HTTP Code:", httpCode)
        print("HTTP Response:", httpRes)
        print(
            "-----------------------------------------------------------------------------\r\n"
        )
        if httpCode == 200:
            print("Get data successful..\r\n")
            return httpRes
            break
        else:
            print("Error")
            print("Get data fail...")
            print("Please wait to try again....\r\n")
            timeout += 1
            time.sleep(0.5)
        if timeout >= 3:
            return False

def wifi():
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("RPi-Pico MicroPython Ver:", sys.version)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    esp8266_at_ver = None
    print("StartUP", con.startUP())
    # print("ReStart",con.reStart())
    print("StartUP", con.startUP())
    print("Echo-Off", con.echoING())
    print("\r\n\r\n")
    esp8266_at_ver = con.getVersion()
    if esp8266_at_ver != None:
        print(esp8266_at_ver)
    con.setCurrentWiFiMode()
    print("\r\n\r\n")
    """
    Connect with the WiFi
    """
    ssid = "GGEZ" #wifi name
    pwd = "123456789" # password
    print("Try to connect with the WiFi..")
    timeout = 0
    # default delay wifi delay 5 sec
    while timeout < 6:
        if "WIFI CONNECTED" in con.connectWiFi(ssid, pwd,delay=3):
            print("ESP8266 connect with the WiFi..")
            return True
            break
        else:
            print(".")
            timeout += 1
            time.sleep(0.5)
    if timeout >= 6:
        print("Timeout connect with the WiFi")
        return False

con = NetworkHelper()
wifiCon = wifi()

host = "192.168.0.104"
path = "/"
param = ""

while wifiCon:
  data = getApi(host,path,param)
  time.sleep(3)

    

    
while True:
    temp_test()
    time.sleep(2)
    card_scan()
    time.sleep(2)
    
    
   
    
