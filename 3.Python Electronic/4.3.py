from machine import Pin,PWM
import time

touch = Pin(15, Pin.IN, Pin.PULL_DOWN)
redLed = PWM(Pin(16))
redLed.freq(1000)

duty = 0

while True:
    touchSensor = touch.value()
    if touchSensor:
        duty += 1000
        print("TOUCHED...")
    redLed.duty_u16(duty)
    
    time.sleep(0.2)