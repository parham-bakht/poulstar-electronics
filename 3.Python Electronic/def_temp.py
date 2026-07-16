def ReadTemperature():
    adc_value = sensor.read_u16()
    voltage = (3.3/65025) * adc_value
    temperature = 27 - (voltage - 0.706)/0.001721
    return temperature