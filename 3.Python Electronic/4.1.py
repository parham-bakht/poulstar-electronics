from machine import Pin
import time

touch = Pin(15, Pin.IN, Pin.PULL_DOWN)
redLed = Pin(16, Pin.OUT)

while True:
    if touch.value():
        print("touched...")
        redLed.value(1)
    else:
        redLed.value(0)
        
    time.sleep(0.2)