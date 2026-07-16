# clock_display.py

import gfx
import math

xcenter = 95
ycenter = 32
radius = 30

def display_clock(oled, hrs, mins, secs):
    graphics = gfx.GFX(128, 64, oled.pixel)
    
    oled.text('12', 90, 4)   
    oled.text('3', 117, 30)
    oled.text('6', 92, 52)
    oled.text('9', 67, 30)
    graphics.circle(xcenter, ycenter, radius, 1)
    
    Sangle = secs * 6      
    Mangle = mins * 6      
    if 0 <= hrs <= 12:
        Hangle = 30 * hrs  
    elif hrs > 12:     
        Hangle = (hrs - 12) * 30
    
    shift_sec_x = radius * math.sin(math.radians(Sangle))
    shift_sec_y = radius * math.cos(math.radians(Sangle))
    graphics.line(xcenter, ycenter, round(xcenter + shift_sec_x), round(ycenter - shift_sec_y), 1)
    
    shift_min_x = 0.8 * radius * math.sin(math.radians(Mangle))
    shift_min_y =  0.8 * radius * math.cos(math.radians(Mangle))
    graphics.line(xcenter, ycenter, round(xcenter + shift_min_x), round(ycenter - shift_min_y), 1)
    
    shift_hour_x = 0.6 * radius * math.sin(math.radians(Hangle))
    shift_hour_y = 0.6 * radius * math.cos(math.radians(Hangle))
    graphics.line(xcenter, ycenter, round(xcenter + shift_hour_x), round(ycenter - shift_hour_y), 1)

