from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from dht import DHT11
import time

builtInSensor = machine.ADC(4)
my_dht = DHT11(Pin(15))

def ReadTemperature():
    adc_value = builtInSensor.read_u16()
    voltage = (3.3/65025) * adc_value
    temperature = 27 - (voltage - 0.706)/0.001721
    return temperature

my_i2c = I2C(0, sda = Pin(16), scl = Pin(17), freq = 400000)

oled = SSD1306_I2C(128, 64, my_i2c)

while True:
    temp = ReadTemperature()
    temp = str(temp)
    
    my_dht.measure()
    ambient_temp = my_dht.temperature()
    hum = my_dht.humidity()

    oled.fill(0)

    oled.text(f"board temperature:",0,0)
    oled.text(f"{temp} C",0,10)
    
    oled.text(f"ambient temperature:",0,20)
    oled.text(f"{ambient_temp} C",0,30)
    
    oled.text(f"ambient humidity:",0,40)
    oled.text(f"{hum} %",0,50)

    oled.show()
    
    time.sleep(2)