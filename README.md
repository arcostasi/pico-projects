# Pico Projects

This repository contains a collection of projects and code examples for the Raspberry Pi Pico using MicroPython.

The Raspberry Pi Pico is a microcontroller board that provides an affordable and versatile platform for embedded projects. It features the RP2040 microcontroller, which is designed by Raspberry Pi and includes a powerful dual-core ARM Cortex-M0+ processor, along with various peripherals.


## Projects

1. [SOS Morse Code](micropython/sos_morse.py)
This script demonstrates how to use a Raspberry Pi Pico to display the SOS Morse code using an LED connected to GPIO 25. The Morse code pattern will repeat every 3 seconds. This project is a great starting point for beginners who want to learn about basic GPIO control and timing in MicroPython on the Raspberry Pi Pico.

2. [LED Flasher](micropython/led_flasher.py)
The provided MicroPython code is designed to run on a Raspberry Pi Pico, controlling the onboard LED to create an alternating flashing sequence. The program has two distinct flash patterns: a fast flashing sequence and a slow flashing sequence. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359571061032587265)

3. [Traffic Light Controller](micropython/tlight.py)
Traffic Light Controller is a MicroPython-based project that simulates a real-life traffic light sequence using LEDs. This project demonstrates how to program a Raspberry Pi Pico microcontroller to control the timing and sequence of LED lights, emulating the behavior of traffic lights at an intersection. The traffic light sequence includes red, yellow, and green lights for each direction, with a configurable delay between each state transition. The state machine design pattern is employed to manage the various states and transitions efficiently, ensuring a smooth and accurate traffic light simulation. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359490482573538305)

6. [DHT22 Sensor Data Reader](micropython/dht22.py) This script demonstrates how to use a Raspberry Pi Pico to read and display temperature and humidity data from a DHT22 sensor. The script continuously reads the sensor data and prints the temperature and humidity values to the console every second. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359493497594540033)

5. [I2C LCD Display](micropython/lcd_i2c.py)
The Raspberry Pi Pico I2C LCD Display is a MicroPython-based project that demonstrates how to interface and control an I2C LCD display using the Raspberry Pi Pico microcontroller. This project showcases how to set up the I2C communication between the Pico and the LCD display, send text and commands to the display, and manipulate the display's features, such as cursor position, backlight, and blinking. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359400194112248833)

6. [SSD1306 OLED Display](micropython/ssd1306_pico.py)
The SSD1306 OLED Display with Raspberry Pi Pico is a MicroPython-based project that demonstrates how to interface and control an SSD1306 OLED display using the Raspberry Pi Pico microcontroller. This project showcases how to set up the I2C communication between the Pico and the OLED display, display a logo and text on the screen, and create a simple timer animation. It also demonstrates how to clear specific lines of text on the display without clearing the entire screen. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359558101922696193)

7. [HC-SR04 Ultrasonic Distance Sensor](micropython/hcsr04_pico.py)
The HC-SR04 Ultrasonic Distance Sensor with Raspberry Pi Pico is a MicroPython-based project that demonstrates how to interface and measure distances using the HC-SR04 ultrasonic sensor and the Raspberry Pi Pico microcontroller. This project showcases how to set up the GPIO pins for triggering and receiving echo signals, calculate the time taken for the echo to return, and convert this time into distance measurements in centimeters or inches. You can then display the distance measurements on an SSD1306 OLED display or an I2C LCD display, which you have already worked with, to create a real-time distance monitoring system. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359562059458336769)

8. [7-Segment Display Counter](micropython/seg7_counter.py)
The 7-Segment Display Counter with Raspberry Pi Pico is a MicroPython-based project that demonstrates how to interface with a 7-segment display to show an ascending and descending hexadecimal counter. Using the Raspberry Pi Pico microcontroller, this project shows you how to set up the GPIO pins to control each segment of the display, define the digit patterns for the hexadecimal counter, and use a switch to control the counting direction. You can expand this project by connecting multiple 7-segment displays or integrating other input devices to create an interactive counter or display system. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/300210834979684872)


## Getting Started

To get started with these projects, you'll need to set up your [Raspberry Pi Pico with MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html). Follow the [official documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) to learn how to install MicroPython on your Pico and start running the code.


## Contributing

Feel free to contribute to this repository by submitting pull requests with new projects or improvements to existing ones. Please ensure that your code is well-documented and follows the general structure and style of the existing projects.


## License

All projects in this repository are licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
