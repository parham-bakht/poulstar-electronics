import ds3231
import time

rtc = ds3231.RTC(sda_pin = 21, scl_pin = 22)
rtc.SetTime(hours= 17, minutes= 45, seconds= 0, weekday= 2, day= 22, month= 10, year= 23)

while True:
    time_ds3231 = rtc.ReadTime("time")
    print(time_ds3231)
    
    time.sleep(1)
