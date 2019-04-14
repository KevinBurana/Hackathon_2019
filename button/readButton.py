#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import datetime
import subprocess

from noLoop import *
from serverCall import *

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#subprocess.Popen('/home/pi/button/browserRun.sh', shell=True)
image = "showBlack"
last = 0
sinceLast = 0
press = 0
second = 0
#print(test)

def display():
    global image
    if(image == "showBlack"):
        showBlack()
    elif(image == "showOnTheWay"):
        showOnTheWay()
    elif(image =="showWaitForResponce"):
        showWaitForResponce()
    elif(image =="showClickForAss"):
        showClickForAss()
    elif(image =="showNotAvailable.gif"):
        showNotAvailable()
 #   print(image)


def phpCall():
    subprocess.Popen('php http://nrs-projects.humboldt.edu/~bjm23/Hackathon/python_function.php?name="SH130c"',Shell=True)

def blank():
    global image
    print("im doing noting")
    image = "showBlack"

def waitForAResponce():
    global image
    print("wait for a responce")
    image = "showWaitForResponce"
    techTimeOut= int(time.time()) - second

def timeout():
    global image
    print("helpers timed out, use anouther system")
    image = "showNotAvailable"

def helpOnWay():
    global image
    print("A help agent is on the way")
    image = "showOnTheWay"

def clickForAss():
    global image
    image = "showClickForAss"
    print("click again for assistance")

def buttonPressed(channel):
    global last
    global time    
    global second
    global sinceLast
    global press
#    sinceLast = int(time.time()) - second
    press = int(time.time())
  #  print(sinceLast)
 #   print(time)
    if(sinceLast <=5):
        waitForAResponce()
    else:
        clickForAss()




 

GPIO.add_event_detect(40,GPIO.FALLING, callback=buttonPressed,bouncetime=200)
#GPIO.add_event_detect(40,GPIO.RISING, callback=helpOnWay)

while True:
    global sinceLast
    display()
    print(image)    
    second = int(time.time())
    sinceLast = second - press
    print(sinceLast)
    if(sinceLast > 5):
       blank()
       GPIO.output(37, GPIO.LOW)
    else:
        GPIO.output(37, GPIO.HIGH)
    time.sleep(.1)
   # print(image)    
   # second = int(time.time())
   # sinceLast = second - press
    print(sinceLast)
 #   print("Hi")
   # print("hi")






