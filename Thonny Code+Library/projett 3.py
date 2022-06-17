# จอ LCD
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#วัดอุณภูมิ 
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
 

 ds_sensor = DS18X20(OneWire(Pin(15)))
    sensor_id = ds.scan()[0] 





def monitor(show):
    show = str(show)
    showmoni = "    "+ show
    
    I2C_ADDR     = 0x27
    I2C_NUM_ROWS = 2
    I2C_NUM_COLS = 16

    i2c = I2C(0, sda=machine.Pin(12), scl=machine.Pin(13), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    lcd.putstr(showmoni)
        
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
              
          else:
              monitor(show)
              



while True:
    temp_test()
    time.sleep(1) 