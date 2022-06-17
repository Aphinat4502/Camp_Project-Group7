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

#แสดงอุณหภูมิน้ำ
def Dss():
    ds.convert_temp()
    sleep_ms(750)         # wait for results
    print(ds.read_temp(sensor_id), " °C")
    sleep_ms(2000)
#################    
#ฟังชั้นเรียกใช้ปั้มน้ำ    
def pump_water():
    def pump_on():
        pump1.value(0)
        sleep_ms(50)
        #print("ON")

    def pump_off():
        pump1.value(1)
        #print("OFF")
        
    def pump_on2():
        pump2.value(0)
        sleep_ms(50)
        #print("ON2")
        
    def pump_off2():
        pump2.value(1)
        #print("OFF2")
########    
    gg = 0
    stop =True
    while stop ==True:
        if PP33.value()==1:
            if gg == 0:
                print("p2 active")#ถ้าน้ำอยู่ในระดับจะใช้ปั้มที่2 ดูดดน้ำออก
                pump_off()
                pump_on2()
                gg = 1 
            if gg == 2:
                pump_off2()
                pump_off
                print("gg p2 and p1 off")#ถ้าน้ำดูดออกจนถึงระดับเซ็นเซอรืจะสั่งไห้มันปิดปั้มท
                gg = 3
        if PP33.value()==0 :#ถ้าเกิดว่าดูดน้ำออกจนถึงระดับแล้วจะสั่งไห้ปั้ม1เติมน้ำเข้าจนถึงระดับ 
            if gg == 1:
                print("p1 active")#ปั้ม1 ทำงาน 
                pump_off2()
                pump_on()
                gg = 2  # ถ้าเกิดว่าถึงระดับ จะกลับไปที่  GG=2 สั่งไห้ปั้มทั้ง2 หยุดทำงาน 
                sleep_ms(50)
            if gg == 3:
                pump_off2()
                pump_off()
                print("p2 and p1 off no active")
                stop = False #จบการทำงาน    
##########

#รับส่งข้อมูลจากAPI


while True:
        Dss()
        pump_water()
   