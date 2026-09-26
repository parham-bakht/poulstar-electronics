from machine import Pin , UART
import time

led = Pin(25,Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_1 = Pin(15, Pin.IN, Pin.PULL_DOWN)

button_2 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(12, Pin.IN, Pin.PULL_DOWN)

uart = UART(1, 9600)
uart.init(9600, bits = 8, parity = None,stop = 1, rx = Pin(9), tx = Pin(8))

print("ready for send")

while True:
    
    if uart.any() > 0:  
        print("something recivied")
        
        data = uart.read().decode('ASCII').strip().lower().split(".")
        print(data)
    if button.value():
        led.toggle()
        uart.write("ru.")
        time.sleep(0.2)
    elif button_1.value():
        led.toggle()
        uart.write("rd.")
        time.sleep(0.2)
        
    elif button_2.value():
        led.toggle()
        uart.write("lu.")
        time.sleep(0.2)
    elif button_3.value():
        led.toggle()
        uart.write("ld.")
        time.sleep(0.2)