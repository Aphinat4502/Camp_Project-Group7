def warning():
    for i in range(7):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)