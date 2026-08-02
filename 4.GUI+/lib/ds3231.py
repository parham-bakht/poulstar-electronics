import machine

class RTC:
    w = ['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag']
    
    def __init__(self, sda_pin=16, scl_pin=17, port=0, speed=100000, address=0x68, register=0x00):
        self.rtc_address = address
        self.rtc_register = register
        sda = machine.Pin(sda_pin)
        scl = machine.Pin(scl_pin)
        self.i2c = machine.I2C(port, sda=sda, scl=scl, freq=speed)

    def SetTime(self, hours, minutes, seconds, weekday, day, month, year):
        # Ensure the year is in the 2-digit format (e.g., 2021 -> 21)
        year = year % 100  # Get the last two digits of the year

        # Convert time to BCD format and build the byte sequence
        NowTime = bytes([
            self.bin2bcd(seconds), 
            self.bin2bcd(minutes), 
            self.bin2bcd(hours), 
            self.bin2bcd(weekday), 
            self.bin2bcd(day), 
            self.bin2bcd(month), 
            self.bin2bcd(year)
        ])

        # Write the time to the RTC via I2C
        self.i2c.writeto_mem(self.rtc_address, self.rtc_register, NowTime)

    # Convert from binary to BCD (Binary-Coded Decimal)
    def bin2bcd(self, value):
        return ((value // 10) << 4) | (value % 10)

    # Convert from BCD to binary
    def bcd2bin(self, value):
        return ((value >> 4) * 10) + (value & 0x0F)

    # Add a 0 in front of numbers smaller than 10
    def pre_zero(self, value):
        if value < 10:
            value = '0' + str(value)
        return str(value)

    def ReadTime(self, mode=0):
        try:
            buffer = self.i2c.readfrom_mem(self.rtc_address, self.rtc_register, 7)
        except:
            return 'Error: Not connected to DS3231'
        
        year = self.bcd2bin(buffer[6]) + 2000
        month = self.bcd2bin(buffer[5])
        day = self.bcd2bin(buffer[4])
        weekday = self.bcd2bin(buffer[3])
        hour = self.bcd2bin(buffer[2])
        minute = self.bcd2bin(buffer[1])
        second = self.bcd2bin(buffer[0])
        
        # Output
        if mode == 'DIN-1355-1':
            return self.pre_zero(day) + '.' + self.pre_zero(month) + '.' + str(year)
        elif mode == 'DIN-1355-1+time':
            return self.pre_zero(day) + '.' + self.pre_zero(month) + '.' + str(year) + ' ' + self.pre_zero(hour) + ':' + self.pre_zero(minute) + ':' + self.pre_zero(second)
        elif mode == 'ISO-8601':
            return str(year) + '-' + self.pre_zero(month) + '-' + self.pre_zero(day)
        elif mode == 'time':
            return self.pre_zero(hour) + ':' + self.pre_zero(minute) + ':' + self.pre_zero(second)
        elif mode == 'weekday':
            return self.w[weekday]
        else:
            return second, minute, hour, weekday, day, month, year
