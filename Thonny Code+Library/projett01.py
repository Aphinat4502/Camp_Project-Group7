#wifi
from machine import UART, Pin
from NetworkHelper import NetworkHelper
import time, sys
###########

#วัดอุณหภูมิ
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms, time
###########

#วัดอุณหภูมิน้ำ
ds = DS18X20(OneWire(Pin(15)))
sensor_id = ds.scan()[0]  # the one and only sensor
#########

#เซ็นเซอร์วัดระดับ
PP33=Pin(9,Pin.IN)
#######

#ปั้มน้ำ
pump1 = Pin(5, Pin.OUT)
pump2 = Pin(7, Pin.OUT)
#######

#รับส่งข้อมูลAPI
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

#ตั้งค่าWiFi
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
    ssid = "B" #wifi name
    pwd = "55555555" # password
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



#แสดงอุณหภูมิน้ำ
def Dss():
    ds.convert_temp()
    sleep_ms(750)
    temp = ds.read_temp(sensor_id)# wait for results
    print(temp, " °C")
    sleep_ms(300)
#################    
#ฟังชั้นเรียกใช้ปั้มน้ำ    


host = "192.168.43.118"
path = "/update_hard_ware4"
param = "ID= "
while True:
    Dss()
    data = getApi(host,path,param)
   