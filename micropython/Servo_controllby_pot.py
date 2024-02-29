'''
https://github.com/Javatti
'''
from time import sleep
from machine import Pin, PWM , ADC
pwm_pin =7; #almost GPIOs in pi-pico support rasbery
pot_pin =26; #check the pinout and choose one of the pin support ADC channel
pwm_servo = PWM(Pin(pwm_pin)) 
pwm_servo.freq(50) #set frequency 
pot_blue=ADC(Pin(pot_pin))

def map_range(x, in_min, in_max, out_min, out_max): #define a function for map two range base on map()Arduino
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    pot_value=pot_blue.read_u16() #read Analog value from potentiometer
    print(pot_value)
    pot_value=map_range(pot_value,0,65535,1000,9000) #mapping range of potentiometer with servo range
    pwm_servo.duty_u16(pot_value) #set the value for servo to turn 
    sleep(0.1)
