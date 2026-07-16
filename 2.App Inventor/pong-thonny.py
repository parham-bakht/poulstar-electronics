from machine import Pin , UART
import time


button = Pin(15, Pin.IN, Pin.PULL_UP)
button_1 = Pin(16, Pin.IN, Pin.PULL_UP)

uart = UART(1, 9600)
uart.init(9600, bits = 8, parity = None,stop = 1, rx = Pin(9), tx = Pin(8))

print("ready for send")

while True:
    
    if uart.any() > 0:  
        print("something recivied")
        
        data = uart.read().decode('ASCII').strip().lower().split(".")
        print(data)
    if not button.value():
        uart.write("ru.")
        time.sleep(0.2)
    elif not button_1.value():
        uart.write("rd.")
        time.sleep(0.2)
        