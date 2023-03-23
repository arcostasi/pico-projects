# Pico Projects

This repository contains a collection of projects and code examples for the Raspberry Pi Pico using MicroPython.

The Raspberry Pi Pico is a microcontroller board that provides an affordable and versatile platform for embedded projects. It features the RP2040 microcontroller, which is designed by Raspberry Pi and includes a powerful dual-core ARM Cortex-M0+ processor, along with various peripherals.


## Projects

1. [SOS Morse Code](micropython/sos_morse.py)
This script displays the SOS Morse code on an LED connected to GPIO 25 of the Raspberry Pi Pico. The pattern repeats every 3 seconds, making it an ideal beginner project for learning basic GPIO control and timing with MicroPython. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359638256784328705)

2. [LED Flasher](micropython/led_flasher.py)
This MicroPython code runs on a Raspberry Pi Pico and creates a flashing sequence for the onboard LED. It features two flash patterns: fast and slow, allowing users to learn about controlling LED sequences. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359571061032587265)

3. [Traffic Light Controller](micropython/tlight.py)
This project simulates a traffic light sequence with LEDs and a Raspberry Pi Pico. Users can learn about programming timing and LED sequences, while also employing the state machine design pattern for efficient management of states and transitions. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359490482573538305)

4. [DHT22 Sensor Data Reader](micropython/dht22.py)
This script reads and displays temperature and humidity data from a DHT22 sensor with a Raspberry Pi Pico. It continuously prints the sensor data to the console every second. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359493497594540033)

5. [I2C LCD Display](micropython/lcd_i2c.py)
This project demonstrates how to control an I2C LCD display with a Raspberry Pi Pico. Users can learn about setting up I2C communication, sending text and commands, and manipulating display features. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359400194112248833)

6. [SSD1306 OLED Display](micropython/ssd1306_pico.py)
This project showcases interfacing and controlling an SSD1306 OLED display with a Raspberry Pi Pico. Users can learn about setting up I2C communication, displaying text and images, and creating simple animations. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359558101922696193)

7. [HC-SR04 Ultrasonic Distance Sensor](micropython/hcsr04_pico.py)
This project demonstrates using the HC-SR04 ultrasonic sensor and Raspberry Pi Pico to measure distances. Users can learn about setting up GPIO pins, calculating time for echo signals, and converting time into distance measurements. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359562059458336769)

8. [7-Segment Display Counter](micropython/seg7_counter.py)
This project showcases interfacing with a 7-segment display to create an ascending and descending hexadecimal counter using a Raspberry Pi Pico. Users can learn about controlling display segments, defining digit patterns, and using a switch to control counting direction. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/300210834979684872)

9. [Google Home Four-Color Rotation Animation](micropython/ring_light.py)
This project showcases creating a Google Home inspired four-color rotation animation using a Raspberry Pi Pico and an LED ring light. Users can learn about controlling LED colors, defining pixel patterns, and creating a smooth color transition animation. [![Wokwi_badge](https://user-images.githubusercontent.com/63488701/212449119-a8510897-c860-4545-8c1a-794169547ba1.svg)](https://wokwi.com/projects/359664314470215681)

## Getting Started

To get started with these projects, you'll need to set up your [Raspberry Pi Pico with MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html). Follow the [official documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) to learn how to install MicroPython on your Pico and start running the code.


## Contributing

Feel free to contribute to this repository by submitting pull requests with new projects or improvements to existing ones. Please ensure that your code is well-documented and follows the general structure and style of the existing projects.


## License

All projects in this repository are licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
