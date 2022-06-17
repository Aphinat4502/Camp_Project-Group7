from machine import Pin, PWM
import utine

pwm = PWM(Pin(27))

MIN = 650000
MID = 1500000
MAX = 3000000

pwm.freq(50)
pwm.duty_ns(MID)

while True:
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1)
    pwm.duty_ns(MAX)
    utime.sleep(1)