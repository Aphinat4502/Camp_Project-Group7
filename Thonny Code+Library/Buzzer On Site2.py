from machine import Pin, PWM
import utime

buzzer = PWM(Pin(18))

def sound():
    for i in range(5):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)

