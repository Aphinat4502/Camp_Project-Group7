#วัดอุณภูมิ 
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
#WiFi API
from machine import UART, Pin
from NetworkHelper import NetworkHelper
import time, sys
#ปั้มน้ำกับเซนเซอร์วัดระดับน้ำ
from machine import Pin
import time

PP33=Pin(9,Pin.IN)
pump1 = Pin(5, Pin.OUT)
pump2 = Pin(7, Pin.OUT)

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
    
host = " 192.168.0.105"
path = "/"
param = "ID= "

con = NetworkHelper()
wifiCon = wifi()

def pump_water():
    def pump_on():
        red_led.value(0)
        green_led.value(1)
        pump1.value(1)
        time.sleep(2)
    
    def pump_off():
        red_led.value(1)
        green_led.value(0)
        pump1.value(0)
    
    def pump_on2():
        red_led.value(0)
        green_led.value(1)
        pump2.value(1)
        time.sleep(2)
    
    
    def pump_off2():
        red_led.value(1)
        green_led.value(0)
        pump2.value(0)
    
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

ds = DS18X20(OneWire(Pin(15)))
sensor_id = ds.scan()[0]  # the one and only sensor

def temp_test():
    ds.convert_temp()
    sleep_ms(750)         # wait for results
    print(ds.read_temp(sensor_id), " °C")
    sleep_ms(2000)
    
while True:
    temp_test()
    