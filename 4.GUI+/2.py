from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(sda = Pin(4), scl = Pin(5), freq = 400000)

oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("GUI with ESP32", 0, 0)
oled.show()

