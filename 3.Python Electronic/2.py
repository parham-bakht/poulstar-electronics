from machine import Pin

ledRed = Pin(16, Pin.OUT)
pushButton= Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    pb=pushButton.value()
    
    if pb == 0:
        ledRed.value(1)
    else:
        ledRed.value(0)