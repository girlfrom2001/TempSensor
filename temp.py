#!/bin/python3

import time ## allows to work with time related functions
import RPi.GPIO as GPIO ## Lets you select pin numbering
from w1thermsensor import W1ThermSensor ## Allows access to containers for temperature sensor
GPIO.setmode(GPIO.BCM) ## Labels pins
GPIO.setup(6,GPIO.OUT) ## pin is output
sensor = W1ThermSensor() ## Variable that initializes temperature sensor

def buzzerOFF(): ## This is a function that allows you to turn buzzer off
    B_pin = 6 ## ## This is the pin that the buzzer is on, we are just defining it which pin in a variable.
    GPIO.output(B_pin,GPIO.HIGH) ## This is telling GPIO 6 to turn off, using the variable we created above.
     
def buzzerON(): ## This is a function that allows you to turn buzzer on
     B_pin = 6 ## This is the pin that the buzzer is on, we are just defining it which pin in a variable.
     GPIO.output(B_pin,GPIO.LOW) ## This is telling GPIO 6 to turn on, using the variable we created above.
     

while True: ## This is just while loop that is essentially turned on when the paramters below are true.
    temperature = sensor.get_temperature() ## This is a variable that is basically holding another variable that initalizes the temperature sensor and then grabs the temperature itself.
    print("The temperature is %s celsius" % temperature) ## This line is just printing the current temperature reading as an output so that we can see what the temperature is.
    time.sleep(.1) ## This is just saying that we want to get the temperature every 10th of a second.
    if temperature >= 25: ## This is the start of an if/else statement that is saying if the temperature is equal to or above 25 degrees to turn on buzzer.
        buzzerON() ## We are calling the function we made on line 10
    else:
        buzzerOFF() ## We are calling the function made on line 14


   




    