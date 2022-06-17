from machine import Pin,PWM
import time
from SG90 import Servo

servo = Servo(22)

servo.setServo90()
time.sleep(1)
servo.setServo180()
time.sleep(1)
servo.setServo90()
time.sleep(1)
servo.setServo0()
time.sleep(1)