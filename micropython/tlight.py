"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico Traffic Light (MicroPython)            ┃
┃                                                          ┃
┃ A traffic light sequence using state machine logic.      ┃
┃ It controls the LEDs to simulate a traffic light,        ┃
┃ cycling through red, yellow, green, and a short yellow.  ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

import machine
import utime

# Define the LED pins
led_red = machine.Pin(1, machine.Pin.OUT)
led_yellow = machine.Pin(5, machine.Pin.OUT)
led_green = machine.Pin(9, machine.Pin.OUT)

def handle_red_state():
    led_red.value(1)
    led_yellow.value(0)
    led_green.value(0)

def handle_yellow_state():
    led_red.value(0)
    led_yellow.value(1)
    led_green.value(0)

def handle_green_state():
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)

def handle_yellow_state_short():
    led_red.value(0)
    led_yellow.value(1)
    led_green.value(0)

# State handlers list
state_handlers = [
    # (state function, time in milliseconds)
    (handle_red_state,            5000),  # Red LED, on for 5 seconds
    (handle_yellow_state,         3000),  # Yellow LED, on for 3 seconds
    (handle_green_state,          5000),  # Green LED, on for 5 seconds
    (handle_yellow_state_short,   2000)   # Short Yellow LED, on for 2 seconds
]

def traffic_light():
    state = 0

    while True:
        # Get the current state tuple (handler function and sleep time)
        current_handler_and_time = state_handlers[state]
        handler_func = current_handler_and_time[0]
        sleep_duration_ms = current_handler_and_time[1]

        # Execute the handler function and sleep for the specified time
        handler_func()
        utime.sleep_ms(sleep_duration_ms)

        # Update the state index
        state = (state + 1) % len(state_handlers)

# Run the traffic light sequence
traffic_light()
