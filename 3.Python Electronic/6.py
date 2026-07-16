from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
import time
myI2c = I2C(0, sda=Pin(16), scl=Pin(17), freq = 400000)

oled = SSD1306_I2C(128, 64, myI2c)

n = 0
while True:
    str_n = str(n)
    oled.fill(0)
    oled.text(str_n,0,0)
    oled.show()
    time.sleep(1)
    n+=1