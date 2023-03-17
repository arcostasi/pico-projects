# Pico Projects

This repository contains a collection of projects and code examples for the Raspberry Pi Pico using MicroPython.

The Raspberry Pi Pico is a microcontroller board that provides an affordable and versatile platform for embedded projects. It features the RP2040 microcontroller, which is designed by Raspberry Pi and includes a powerful dual-core ARM Cortex-M0+ processor, along with various peripherals.


## Projects

1. [SOS Morse Code] (sos_morse.py)
This script demonstrates how to use a Raspberry Pi Pico to display the SOS Morse code using an LED connected to GPIO 25. The Morse code pattern will repeat every 3 seconds. This project is a great starting point for beginners who want to learn about basic GPIO control and timing in MicroPython on the Raspberry Pi Pico.

2. [Traffic Light Controller](micropython/tlight.py)
Traffic Light Controller is a MicroPython-based project that simulates a real-life traffic light sequence using LEDs. This project demonstrates how to program a Raspberry Pi Pico microcontroller to control the timing and sequence of LED lights, emulating the behavior of traffic lights at an intersection. The traffic light sequence includes red, yellow, and green lights for each direction, with a configurable delay between each state transition.

3. [Pi Pico I2C LCD Display](micropython/lcd_i2c.py)
The Raspberry Pi Pico I2C LCD Display is a MicroPython-based project that demonstrates how to interface and control an I2C LCD display using the Raspberry Pi Pico microcontroller. This project showcases how to set up the I2C communication between the Pico and the LCD display, send text and commands to the display, and manipulate the display's features, such as cursor position, backlight, and blinking. The example code provided serves as a starting point for users to build upon and create their own custom projects that require displaying information on an LCD screen.


## Getting Started

To get started with these projects, you'll need to set up your Raspberry Pi Pico with MicroPython. Follow the official documentation to learn how to install MicroPython on your Pico and start running the code.


## Contributing

Feel free to contribute to this repository by submitting pull requests with new projects or improvements to existing ones. Please ensure that your code is well-documented and follows the general structure and style of the existing projects.


## License

All projects in this repository are licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
