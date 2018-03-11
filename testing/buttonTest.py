#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import os, sys
import time

b = [4,17,27,22,10,9,11,0,5,6,13,26,23,24,1,12,16,20]
buttons = []

for pin in b:
    buttons.append(Button(pin, bounce_time=0.002))

while(1):
    for btn in buttons:
        #btn = Button(pin, bounce_time=0.002)
        print('' + str(btn.pin) + ': ' + str(btn.is_pressed))
    time.sleep(1)