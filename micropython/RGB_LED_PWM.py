from machine import Pin , PWM
from time import sleep


# Define the GPIO pin numbers for the RGB LED
LEDRGB_RED_PIN = 22
LEDRGB_GREEN_PIN = 21
LEDRGB_BLUE_PIN = 20
# Initialize Pins state
LED_RED = Pin(LEDRGB_RED_PIN,Pin.OUT)
LED_GREEN = Pin(LEDRGB_GREEN_PIN,Pin.OUT)
LED_BLUE = Pin(LEDRGB_BLUE_PIN,Pin.OUT)
#make the pins use PWM mode
RED = PWM(LED_RED)
GREEN = PWM(LED_GREEN)
BLUE = PWM(LED_BLUE)
#set frequency of PWM pins
frequency = 1000 #you can change the frequency to 5000 aftar that change the array in top uncomment that!
RED.freq (frequency)
GREEN.freq(frequency)
BLUE.freq(frequency)
#make a array of max,min,zero amount of pwm 
#PWM_Range = [65536,32768,0] #in 5kHrz
PWM_Range = [65520,32512,0]  #in 1kHrz
while True:
    #RED
 RED.duty_u16(PWM_Range[0])
 GREEN.duty_u16(PWM_Range[2])
 BLUE.duty_u16(PWM_Range[2])
 sleep(1)
    #GREEN
 RED.duty_u16(PWM_Range[2])
 GREEN.duty_u16(PWM_Range[0])
 BLUE.duty_u16(PWM_Range[2])
 sleep(1)
    #BLUE
 RED.duty_u16(PWM_Range[2])
 GREEN.duty_u16(PWM_Range[2])
 BLUE.duty_u16(PWM_Range[0])
 sleep(1)
    #PINK
 RED.duty_u16(PWM_Range[0])
 GREEN.duty_u16(PWM_Range[2])
 BLUE.duty_u16(PWM_Range[0])
 sleep(1)
    #YELLOW
 RED.duty_u16(PWM_Range[0])
 GREEN.duty_u16(PWM_Range[0])
 BLUE.duty_u16(PWM_Range[2])
 sleep(1)
    #Aqua
 RED.duty_u16(PWM_Range[2])
 GREEN.duty_u16(PWM_Range[0])
 BLUE.duty_u16(PWM_Range[0])
 sleep(1)
    #Slightly desaturated magenta
 RED.duty_u16(PWM_Range[1])
 GREEN.duty_u16(PWM_Range[2])
 BLUE.duty_u16(PWM_Range[1])
 sleep(1)  
  #Strong yellow
 RED.duty_u16(PWM_Range[1])
 GREEN.duty_u16(PWM_Range[1])
 BLUE.duty_u16(PWM_Range[2])
 sleep(1)


 