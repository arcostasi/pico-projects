"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico LED Flasher (MicroPython)              ┃
┃                                                          ┃
┃ A program to control an onboard LED with alternating     ┃
┃ fast flashes and regular blinks.                         ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

from machine import Pin
import utime

led = Pin(25, Pin.OUT)

FAST_FLASH_DELAY =         30  # 30 ms for fast flash
SLOW_FLASH_DELAY =        500  # 500 ms for slow flash
FAST_FLASH_COUNT =          6  # Number of fast flashes
SLOW_FLASH_COUNT =          3  # Number of slow flashes

def flash_led(delay, count):
    # Loop through the given number of times (count) to flash the LED
    for _ in range(count):
        led.toggle()           # Toggle the LED state (on/off)
        utime.sleep_ms(delay)  # Wait for the specified delay time
        led.toggle()           # Toggle the LED state (on/off) again
        utime.sleep_ms(delay)  # Wait for the specified delay time

while True:
    # Fast flashing sequence
    flash_led(FAST_FLASH_DELAY, FAST_FLASH_COUNT)

    # Short pause between sequences
    utime.sleep_ms(500)

    # Slow flashing sequence
    flash_led(SLOW_FLASH_DELAY, SLOW_FLASH_COUNT)

    # Longer pause between sequences
    utime.sleep_ms(1000)
