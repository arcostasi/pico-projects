"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico Traffic Light Controller (MicroPython) ┃
┃                                                          ┃
┃ An interactive LED traffic light sequence.               ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

import machine
import utime

# Define the LED pins
led_red = machine.Pin(16, machine.Pin.OUT)
led_yellow = machine.Pin(17, machine.Pin.OUT)
led_green = machine.Pin(18, machine.Pin.OUT)

# Create a list of LED pins and their corresponding delay times
led_sequence = [
    (led_red, 5),
    (led_yellow, 3),
    (led_green, 5)
]

def traffic_light():
    while True:
        for led, delay in led_sequence:
            # Turn on the LED and wait for the specified delay time
            led.value(1)
            utime.sleep(delay)
            led.value(0)

# Run the traffic light sequence
traffic_light()
