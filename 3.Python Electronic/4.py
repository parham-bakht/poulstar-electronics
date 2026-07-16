from machine import Pin, PWM
import time

ledOnBoard = PWM(Pin(16))

ledOnBoard.freq(1000)

while True:
    for duty in range(0,65025,5):
        ledOnBoard.duty_u16(duty)
        time.sleep(0.0001)
        
    for duty in range(65025,0,-5):
        ledOnBoard.duty_u16(duty)
        time.sleep(0.0001)