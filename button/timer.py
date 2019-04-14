#!/usr/bin/python3

import time

print(time.time())

old=int(time.time())

time.sleep(1)

print(int(time.time())-old)
