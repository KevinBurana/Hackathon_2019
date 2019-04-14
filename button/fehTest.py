#!/usr/bin/python3

import time
import subprocess


def putImage():
    subprocess.Popen('feh -XFZ onTheWay.gif',shell=True)

def kill():
    subprocess.Popen('pkill feh',shell=True)

while True:
    time.sleep(1)
    putImage()
    time.sleep(1)
    kill()
    print("didi i kill")
