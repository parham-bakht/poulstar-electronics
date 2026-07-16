from machine import Pin
from dht import DHT11
import time

myDht = DHT11(Pin(15))

while True:
    myDht.measure()

    temp = myDht.temperature()
    hum = myDht.humidity()

    print(f"temperature is:{temp}°C\nhumidity is:{hum}%")
    
    time.sleep(2)
