from machine import Pin,SoftI2C
from ssd1306 import SSD1306_I2C
import time
import ds3231
from clock_display import display_clock

i2c = SoftI2C(sda = Pin(4), scl = Pin(5), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)

rtc = ds3231.RTC(sda_pin= 21, scl_pin= 22)
rtc.SetTime(hours= 18, minutes= 47, seconds= 0, weekday= 2, day= 22, month= 10, year= 23)

while True:
    
    rtc_time = rtc.ReadTime("time")
    
    hour, minute, second = rtc_time.split(":")
    
    oled.fill(0)
    display_clock(oled, int(hour), int(minute), int(second))
    oled.show()
    
    time.sleep(1)