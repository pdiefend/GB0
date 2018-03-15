#!/usr/bin/env python3
from gpiozero import Button, LED
from signal import pause
import os, sys
import time

#offGPIO = int(sys.argv[1]) if len(sys.argv) >= 2 else 21
#holdTime = int(sys.argv[2]) if len(sys.argv) >= 3 else 6

ledGPIO = 7
offGPIO = 22
holdTime = 4

led = LED(ledGPIO)
led.on()
time.sleep(1)
led.off()

# the function called to shut down the RPI
def shutdown():
    os.system("sudo poweroff")

def warning_blink():
    led.blink(0.5, 0.5, 3)

btn = Button(offGPIO, hold_time=holdTime)
btn.when_held = shutdown
btn.when_pressed = warning_blink
pause()    # handle the button presses in the background
