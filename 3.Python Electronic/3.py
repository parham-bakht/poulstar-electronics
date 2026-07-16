from machine import Pin, ADC
import time

sensor = machine.ADC(4)
redLed = Pin(16, Pin.OUT)
buzzer = Pin(15, Pin.OUT)

def ReadTemperature():
    adc_value = sensor.read_u16()
    voltage = (3.3/65025) * adc_value
    temperature = 27 - (voltage - 0.706)/0.001721
    return temperature

while True:
    temp = ReadTemperature()
    if temp > 22:
        redLed.value(1)
        buzzer.value(1)
    else:
        redLed.value(0)
        buzzer.value(0)

    print(temp)
    time.sleep(1)
    