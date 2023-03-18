"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico 7-Segment Display Counter (MicroPython)┃
┃                                                          ┃
┃ A program to demonstrate the use of a 7-segment display  ┃
┃ by implementing an ascending/descending hexadecimal      ┃
┃ counter based on the state of an input switch.           ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

from machine import Pin
from utime import sleep

# 7-segment display layout
#       A
#      ---
#  F |  G  | B
#      ---
#  E |     | C
#      ---
#       D

pins = [
    Pin(2, Pin.OUT),  # A
    Pin(3, Pin.OUT),  # B
    Pin(4, Pin.OUT),  # C
    Pin(5, Pin.OUT),  # D
    Pin(6, Pin.OUT),  # E
    Pin(8, Pin.OUT),  # F
    Pin(7, Pin.OUT),  # G
    Pin(0, Pin.OUT)   # DP (not connected)
]

# Common anode 7-segment display digit patterns
digits = [
    [0, 0, 0, 0, 0, 0, 1, 1], # 0
    [1, 0, 0, 1, 1, 1, 1, 1], # 1
    [0, 0, 1, 0, 0, 1, 0, 1], # 2 
    [0, 0, 0, 0, 1, 1, 0, 1], # 3
    [1, 0, 0, 1, 1, 0, 0, 1], # 4
    [0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 1, 0, 0, 0, 0, 0, 1], # 6
    [0, 0, 0, 1, 1, 1, 1, 1], # 7
    [0, 0, 0, 0, 0, 0, 0, 1], # 8
    [0, 0, 0, 1, 1, 0, 0, 1], # 9
    [0, 0, 0, 1, 0, 0, 0, 1], # a
    [1, 1, 0, 0, 0, 0, 0, 1], # b
    [0, 1, 1, 0, 0, 0, 1, 1], # C
    [1, 0, 0, 0, 0, 1, 0, 1], # d
    [0, 1, 1, 0, 0, 0, 0, 1], # E
    [0, 1, 1, 1, 0, 0, 0, 1], # F
]

def reset():
    """Turns off all segments on the 7-segment display."""
    for pin in pins:
        pin.value(1)

reset()

switch = Pin(11, Pin.IN)

while True:
    if switch.value() == 1:
        # Ascending counter
        for i in range(len(digits)):
            if switch.value() == 0:
                break
            for j in range(len(pins) - 1):
                pins[j].value(digits[i][j])
            sleep(0.5)
    else:
        # Descending counter
        for i in range(len(digits) - 1, -1, -1):
            if switch.value() == 1:
                break
            for j in range(len(pins)):
                pins[j].value(digits[i][j])
            sleep(0.5)
