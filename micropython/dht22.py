"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico DHT22 Sensor Reader (MicroPython)      ┃
┃                                                          ┃
┃ A program to read temperature and humidity data from a   ┃
┃ DHT22 sensor and display the values on the console.      ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

import machine
import utime
import dht

# Configure the sensor data pin
DATA_PIN = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_UP)

# Create an instance of the DHT22 sensor
sensor = dht.DHT22(DATA_PIN)

def read_and_display_data():
    # Function to read and display data from the DHT22 sensor
    try:
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: {:.2f}°C, Humidity: {:.2f}%".format(temp, humidity))
    except Exception as e:
        print("Error reading sensor data:", e)

# Main loop
while True:
    read_and_display_data()
    utime.sleep(1)  # Wait for 1 seconds before reading the data again
