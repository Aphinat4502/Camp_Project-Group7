from machine import Pin
import time
import machine, onewire, ds18x20, time
from machine import I2C, Pin, SPI
from pico_i2c_lcd import I2cLcd
from lcd_api import LcdApi

ds_pin = machine.Pin(15)
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


def temp_test():
    ds_sensor.convert_temp()
    time.sleep_ms(300)
    print( ds_sensor.convert_temp())
    for rom in roms:
          show = ds_sensor.read_temp(rom)
          #print(ds_sensor.read_temp(rom))
          float(show)
          if(show>10):
              monitor(show)
              show = str(show)
              gg = 'PUB,"NonJoong/hardware/temp",' + '"' + show + '"'
              #print(gg)
              uart.write(gg)
          else:
               monitor(show)

while True:
    temp_test()
    time.sleep(2)
    