#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import os, sys
import time
import uinput

device = uinput.Device([
	uinput.KEY_A,
	uinput.KEY_B,
	uinput.KEY_C,
	uinput.KEY_D,
	uinput.KEY_E,
	uinput.KEY_F,
	uinput.KEY_G,
	uinput.KEY_H,
	uinput.KEY_I,
	uinput.KEY_J,
	uinput.KEY_K,
	uinput.KEY_L,
	uinput.KEY_M,
	uinput.KEY_N,
	uinput.KEY_O,
	uinput.KEY_P,
	uinput.KEY_Q,
	uinput.KEY_R,
	])

# it seems to need a delay before we can do stuff
# 0.125s seems to work, 0.1 doesn't and that's good enough for a first time startup delay
# this seems to be true of the dev's examples too. This might be RPi-specific
time.sleep(0.125)


'''
b = [4,17,27,22,10,9,11,0,5,6,13,26,23,24,1,12,16,20]
buttons = []

for pin in b:
    buttons.append(Button(pin, bounce_time=0.002))

while(1):
    for btn in buttons:
        #btn = Button(pin, bounce_time=0.002)
        print('' + str(btn.pin) + ': ' + str(btn.is_pressed))
    time.sleep(1)
'''

def press_A():
	device.emit_click(uinput.KEY_A) #4

def press_B():
	device.emit_click(uinput.KEY_B) #17

def press_C():
	device.emit_click(uinput.KEY_C) #27

def press_D():
	device.emit_click(uinput.KEY_D) #22

def press_E():
	device.emit_click(uinput.KEY_E) #10

def press_F():
	device.emit_click(uinput.KEY_F) #9

def press_G():
	device.emit_click(uinput.KEY_G) #11

def press_H():
	device.emit_click(uinput.KEY_H) #0

def press_I():
	device.emit_click(uinput.KEY_I) #5

def press_J():
	device.emit_click(uinput.KEY_J) #6

def press_K():
	device.emit_click(uinput.KEY_K) #13

def press_L():
	device.emit_click(uinput.KEY_L) #26

def press_M():
	device.emit_click(uinput.KEY_M) #23

def press_N():
	device.emit_click(uinput.KEY_N) #24

def press_O():
	device.emit_click(uinput.KEY_O) #1

def press_P():
	device.emit_click(uinput.KEY_P) #12

def press_Q():
	device.emit_click(uinput.KEY_Q) #6

def press_R():
	device.emit_click(uinput.KEY_R) #20

btn_A = Button(4)
btn_A.when_pressed = press_A
btn_B = Button(17)
btn_B.when_pressed = press_B
btn_C = Button(27)
btn_C.when_pressed = press_C
btn_D = Button(22)
btn_D.when_pressed = press_D
btn_E = Button(10)
btn_E.when_pressed = press_E
btn_F = Button(9)
btn_F.when_pressed = press_F
btn_G = Button(11)
btn_G.when_pressed = press_G
btn_H = Button(0)
btn_H.when_pressed = press_H
btn_I = Button(5)
btn_I.when_pressed = press_I
btn_J = Button(6)
btn_J.when_pressed = press_J
btn_K = Button(13)
btn_K.when_pressed = press_K
btn_L = Button(26)
btn_L.when_pressed = press_L
btn_M = Button(23)
btn_M.when_pressed = press_M
btn_N = Button(24)
btn_N.when_pressed = press_N
btn_O = Button(1)
btn_O.when_pressed = press_O
btn_P = Button(12)
btn_P.when_pressed = press_P
btn_Q = Button(16)
btn_Q.when_pressed = press_Q
btn_R = Button(20)
btn_R.when_pressed = press_R

print('Ready')
pause()
