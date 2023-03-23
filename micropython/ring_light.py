"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico NeoPixel Ring Animation (MicroPython)  ┃
┃                                                          ┃
┃ A program to demonstrate the use of a NeoPixel ring      ┃
┃ light with a Raspberry Pi Pico by implementing a         ┃
┃ Google Home four-color rotation animation.               ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

from machine import Pin
import array
import time
import rp2

# RP2040 PIO and Pin Configurations
PIN_NUM = 16  # Pin connected to the ring light
led_count = 16  # Number of LEDs in the ring light
brightness = 1.0  # 0.1 = darker, 1.0 = brightest

# WS2812 parameters
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT,
             autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Create the StateMachine with the ws2812 program, outputting on pre-defined pin
# at the 8MHz frequency
state_machine = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Activate the state machine
state_machine.active(1)

# Range of LEDs stored in an array
pixel_array = array.array("I", [0 for _ in range(led_count)])

def update_pixels(brightness_input=brightness):
    dimmer_array = array.array("I", [0 for _ in range(led_count)])
    for index, color in enumerate(pixel_array):
        red = int(((color >> 8) & 0xFF) * brightness_input)  # 8-bit red dimmed to brightness
        green = int(((color >> 16) & 0xFF) * brightness_input)  # 8-bit green dimmed to brightness
        blue = int((color & 0xFF) * brightness_input)  # 8-bit blue dimmed to brightness
        dimmer_array[index] = (green << 16) + (red << 8) + blue  # 24-bit color dimmed to brightness
    state_machine.put(dimmer_array, 8)  # Update the state machine with new colors
    time.sleep_ms(10)

def set_rgb_color(index, color):
    color = hex_to_rgb(color)
    pixel_array[index] = (color[1] << 16) + (color[0] << 8) + color[2]  # Set 24-bit color

def hex_to_rgb(hex_val):
    return tuple(int(hex_val.lstrip('#')[ii:ii+2], 16) for ii in (0, 2, 4))

def hsv_to_rgb(h, s, v):
    i = int(h * 6.)
    f = (h * 6.) - i
    p = v * (1. - s)
    q = v * (1. - s * f)
    t = v * (1. - s * (1. - f))
    i = i % 6

    if i == 0:
        return int(v * 255), int(t * 255), int(p * 255)
    elif i == 1:
        return int(q * 255), int(v * 255), int(p * 255)
    elif i == 2:
        return int(p * 255), int(v * 255), int(t * 255)
    elif i == 3:
        return int(p * 255), int(q * 255), int(v * 255)
    elif i == 4:
        return int(t * 255), int(p * 255), int(v * 255)
    elif i == 5:
        return int(v * 255), int(p * 255), int(q * 255)

def set_hsv_color(index, h, s, v):
    r, g, b = hsv_to_rgb(h, s, v)
    pixel_array[index] = (g << 16) + (r << 8) + b  # Set 24-bit color

def google_home_animation():
    # Google Home four-color rotation scheme
    google_colors = ['#4285f4', '#ea4335', '#fbbc05', '#34a853']  # Hex colors by Google
    cycles = 5  # Number of times to cycle 360-degrees

    for rotation in range(int(cycles * len(pixel_array))):
        for index in range(len(pixel_array)):
            if index % int(len(pixel_array) / 4) == 0:  # 90-degree LEDs only
                set_rgb_color((index + rotation) % led_count, google_colors[int(index / len(pixel_array) * 4)])
            else:
                set_rgb_color((index + rotation) % led_count, '#000000')  # Other pixels blank
        update_pixels()  # Update pixel colors
        time.sleep(0.05)  # Wait between changes

def rainbow_animation():
    for rotation in range(led_count * 10):  # Repeat the animation 10 times
        for index in range(led_count):
            hue = (index + rotation) % led_count / led_count
            set_hsv_color(index, hue, 1, 1)  # Set the current pixel to the rainbow color
        update_pixels()  # Update pixel colors
        time.sleep_ms(5)  # Wait between changes

def main():

    while True:
        google_home_animation()
        rainbow_animation()  # Bonus "Easter egg" animation

# Call the main function
if __name__ == "__main__":
    main()
