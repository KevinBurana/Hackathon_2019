#!/usr/bin/python3
import time
from tkinter import *      
#import RPi.GPIO as GPIO

#GPIO.setMode(GPIO.BOARD)
#GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUT_UP)

root = Tk()      


#def test():
 #   q=1
  #  print("im a fuchtion")
   # while True:
    #    q=q

canvas = Canvas(root, width = 1280, height = 720)      
root.attributes("-fullscreen", True)
canvas.pack()      
img = PhotoImage(file="onTheWay.gif")      
canvas.create_image(0,0, anchor=NW, image=img)      

def showBlack():
    img = PhotoImage(file="black.gif")
    canvas.create_image(0,0, anchor=NW, image=img)
    root.update()

def showOnTheWay():
    img = PhotoImage(file="onTheWay.gif")
    canvas.create_image(0,0, anchor=NW, image=img)
    root.update()

def showWaitForResponce():
    img = PhotoImage(file="waitForResponce.gif")
    canvas.create_image(0,0, anchor=NW, image=img)
    root.update()

def showNotAvailable():
    img = PhotoImage(file="notAvailable.gif")
    canvas.create_image(0,0, anchor=NW, image=img)
    root.update()

def showClickForAss():
    img = PhotoImage(file="clickForAssistance.gif")
    canvas.create_image(0,0, anchor=NW, image=img)
    root.update()


#while True:
 #   for x in range (1,20):
  #      showBlack()
  #      time.sleep(.1)
  #  for x in range (1,20):
 #     showOnTheWay()
#     time.sleep(.1)


#mainloop() 




#thread.daemon=True
#thread.start()

