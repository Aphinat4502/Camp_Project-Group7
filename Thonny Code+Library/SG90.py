from time import sleep
from machine import Pin, PWM


class Servo:

    def __init__(self, pin=50):
        self.pin = pin
        self.min = 1000
        self.mid = 2701
        self.max = 4501
        self.auto_posi = 1000

        self.pwm = PWM(Pin(pin))
        self.pwm.freq(30)
        print(f"PIN :{pin}")

    def test(self):
        for position in range(self.min, self.max, 25):
            self.pwm.duty_u16(position)
        sleep(2)
        for position in range(self.max, self.min, -25):
            self.pwm.duty_u16(position)
        sleep(2)

    def setServo0(self):
        if(self.auto_posi == self.max):
            for position in range(self.max, self.min, -25):
                self.pwm.duty_u16(position)
                self.auto_posi = self.min
        elif(self.auto_posi == self.mid):
            for position in range(self.mid, self.min, -25):
                self.pwm.duty_u16(position)
                self.auto_posi = self.min

    def setServo90(self):
        if(self.auto_posi == self.min):
            for position in range(self.min, self.mid, 25):
                self.pwm.duty_u16(position)
                self.auto_posi = self.mid
        elif(self.auto_posi == self.max):
            for position in range(self.max, self.mid, -25):
                self.pwm.duty_u16(position)
                self.auto_posi = self.mid

    def setServo180(self):
        if(self.auto_posi == self.min):
            for position in range(self.min, self.max, 25):
                self.pwm.duty_u16(position)
                self.auto_posi = self.max
        elif(self.auto_posi == self.mid):
            for position in range(self.mid, self.max, 25):
                self.pwm.duty_u16(position)
                self.auto_posi = self.min
