import ds3231
import time
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(sda = Pin(4), scl = Pin(5), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)

rtc = ds3231.RTC(sda_pin = 21, scl_pin = 22)
rtc.SetTime(hours= 17, minutes= 45, seconds= 0, weekday= 2, day= 22, month= 10, year= 23)

while True:
    time_ds3231 = rtc.ReadTime("time")
    
    oled.fill(0)
    oled.text(str(time_ds3231), 0, 0)
    oled.show()
    
    time.sleep(1)