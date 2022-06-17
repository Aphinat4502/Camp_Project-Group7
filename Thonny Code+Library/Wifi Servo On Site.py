from machine import UART, Pin
from NetworkHelper import NetworkHelper
import time, sys

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

host = "18.141.11.24"
path = "/hw/get_by_id"
param = "ID=30"

servo = Servo(27)

if(wifiCon):
    while(True):
        data = getApi(host, path, param)
        if(data):
            if(data[0]['value'] == 180):
                servo.setServo180()
                print("180 Degree")
            elif:(data[0]['value'] == 90):
                servo.setServo90()
                print("90 Degree")
            elif:(data[0]['value'] == 0):
                servo.setServo0()
                print("0 Degree")
            else:
                print("error")