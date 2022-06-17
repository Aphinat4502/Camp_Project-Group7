from machine import UART, Pin
import machine, onewire, ds18x20, time, sys
from NetworkHelper import NetworkHelper

pump1 = Pin(21,Pin.OUT)
pump2= Pin(22,Pin.OUT)

ds_pin = machine.Pin(17)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Temp ds18x20 device')

ds_sensor.convert_temp()
time.sleep_ms(300)

def pump_water():
    def pump_on():
    pump1.value(1)
    time.sleep(2)
    
    def pump_off():
    pump1.value(0)
    
    def pump_on2():
    red_led.value(0)
    green_led.value(1)
    pump1.value(1)
    time.sleep(2)
    
    def pump_off2():
    red_led.value(1)
    green_led.value(0)
    pump1.value(0)

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
              gg = 'PUB,"NonJoong/hardware/temp",' + '"' + show + '"'
              #print(gg)
              uart.write(gg)
          else:
              monitor(show)

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
