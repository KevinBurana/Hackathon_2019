#!/usr/bin/python3
import threading
import time
from tkinter import *      
import RPi.GPIO as GPIO

GPIO.setMode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUT_UP)

root = Tk()      


def test():
    q=1
    print("im a fuchtion")
    while True:
        q=q

def photo():
    canvas = Canvas(root, width = 1280, height = 720)      
    root.attributes("-fullscreen", True)
    canvas.pack()      
    img = PhotoImage(file="onTheWay.gif")      
    canvas.create_image(0,0, anchor=NW, image=img)      
    mainloop() 



thread = threading.Thread(target=o, args=())
thread.start()

photo()

#thread.daemon=True
#thread.start()

print("did I run")

time.sleep(30)
