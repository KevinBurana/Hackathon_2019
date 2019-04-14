#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(37, GPIO.HIGH)
    sleep(.5)
    GPIO.output(37, GPIO.LOW)
    sleep(.5)
