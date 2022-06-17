from machine import UART, Pin, PWM
import machine, onewire, ds18x20, time, sys
from NetworkHelper import NetworkHelper

PP33=Pin(28,Pin.IN)
pump1 = Pin(21,Pin.OUT)
pump2 = Pin(22,Pin.OUT)

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
    time.sleep(2)

    def pump_on2():
    pump1.value(1)
    time.sleep(2)
    
    def pump_off2():
    pump1.value(0)
    time.sleep(2)

 gg = 0
    stop =True
    while stop ==True:
        if PP33.value()==1:
            if gg == 1:
                print("p2 and p1 on")
                pump_on()
                pump_on2() 
            if gg == 0:
                pump_off2()
                pump_off()
                print("p2 and p1 off")
                
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