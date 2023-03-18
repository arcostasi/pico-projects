"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico I2C LCD Display (MicroPython)          ┃
┃                                                          ┃
┃ An example of using an I2C LCD display with the          ┃
┃ Raspberry Pi Pico.                                       ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

def initialize_i2c_lcd(sda_pin, scl_pin, i2c_freq):
    """Initialize the I2C LCD display with the given parameters."""
    i2c_bus = I2C(0, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=i2c_freq)
    i2c_address = i2c_bus.scan()[0]
    return I2cLcd(i2c_bus, i2c_address, 2, 16), i2c_address

def display_address(lcd, i2c_address):
    """Display the I2C address in decimal and hexadecimal formats."""
    lcd.blink_cursor_on()
    for address_format in (str, hex):
        lcd.putstr(f"I2C Address: {address_format(i2c_address)}\n")
        lcd.putstr("PI PICO Hardware")
        sleep(2)
        lcd.clear()
    lcd.blink_cursor_off()

def backlight_test(lcd):
    """Perform a backlight test by blinking the backlight 10 times."""
    lcd.clear()
    lcd.putstr("Backlight Test")
    for _ in range(10):
        lcd.backlight_on()
        sleep(0.2)
        lcd.backlight_off()
        sleep(0.2)
    lcd.backlight_on()

def hide_cursor_count(lcd):
    """Hide the cursor and display a count from 0 to 19."""
    lcd.clear()
    lcd.hide_cursor()
    for count in range(20):
        lcd.putstr(str(count))
        sleep(0.4)
        lcd.clear()

def main():
    """Main function to run the I2C LCD display example."""
    lcd_display, i2c_address = initialize_i2c_lcd(sda_pin=0, scl_pin=1, i2c_freq=400000)
    while True:
        display_address(lcd_display, i2c_address)
        backlight_test(lcd_display)
        hide_cursor_count(lcd_display)

if __name__ == '__main__':
    main()
