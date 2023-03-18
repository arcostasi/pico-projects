"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Morse Code SOS with Raspberry Pi Pico and MicroPython    ┃
┃                                                          ┃
┃ This script demonstrates how to use a Raspberry Pi Pico  ┃
┃ to display the SOS Morse code using an LED connected to  ┃
┃ GPIO 25. The Morse code pattern will repeat every 5      ┃
┃ seconds.                                                 ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

import machine
import utime

# Morse Code patterns for SOS
data = [
    (3, 150),  # 3 short blinks
    (3, 450),  # 3 long blinks
    (3, 130)   # 3 short blinks
]

# Function to control the LED
def signal(blinks, duration):
    for i in range(blinks):
        led.value(1)  # Turn on the LED (HIGH)
        utime.sleep_ms(duration)
        led.value(0)  # Turn off the LED (LOW)
        utime.sleep_ms(duration)

# Configure pin 25 as output
led = machine.Pin(25, machine.Pin.OUT)

# Main loop
while True:
    for blinks, duration in data:
        signal(blinks, duration)
        utime.sleep_ms(1000)  # Interval between Morse code parts
    utime.sleep_ms(4000)      # 4-second interval before repeating Morse code (1000 ms already considered in the loop above)
