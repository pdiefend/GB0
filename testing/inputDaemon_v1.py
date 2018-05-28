#!/usr/bin/env python3

#from gpiozero import Button
import signal
import os, sys
import time
#import uinput
from evdev import uinput, UInput, ecodes as e
import RPi.GPIO as gpio
#from smbus import SMBus

DEBUG = False
Debounce = 0.01

R_slider = 4	# uinput.KEY_VOLUMEUP, Right slider
L_slider = 27	# uinput.KEY_VOLUMEDOWN, Left slider
C_sldier = 17	# uinput.KEY_MUTE, Click slider
Turbo = 5		# uinput.KEY_T, Alt key/turbo button, center Top left
Mode = 26		# uinput.BTN_MODE, Mode/clear button , center top right
Start = 20		# uinput.BTN_START, Start Button, center bottom left
Select = 6		# uinput.BTN_SELECT, Select Button, center bottom right
Btn_A = 1		# uinput.BTN_A, A Button, right bottom
Btn_B = 16      # uinput.BTN_B, B Button, right right
Btn_X = 24		# uinput.BTN_X, X Button, right top
Btn_Y = 12		# uinput.BTN_Y, Y Button, right down
Btn_U = 11		# uinput.BTN_DPAD_UP, Up Button, left top
Btn_L = 9		# uinput.BTN_DPAD_LEFT, Left Button, left left
Btn_R = 0		# uinput.BTN_DPAD_RIGHT, Right Button, left right
Btn_D = 13		# uinput.BTN_DPAD_DOWN, Down Button, left down
Btn_LT = 10		# uinput.BTN_TL, Left Trigger
Btn_RT = 23		# uinput.BTN_TR, Right Trigger



buttonList = [R_slider, L_slider, C_sldier, Turbo, Mode, Start, Select, 
			  Btn_A, Btn_B, Btn_X, Btn_Y, Btn_U, 
			  Btn_L, Btn_R, Btn_D, Btn_LT, Btn_RT]


keyList = {
    R_slider:  e.KEY_VOLUMEUP,     	# Right slider
    L_slider: e.KEY_VOLUMEDOWN,		# Left slider
    C_sldier: e.KEY_MUTE,          	# Click slider
    Turbo:  e.KEY_C,             	# Alt key/turbo button, center Top left
    Mode: e.KEY_V,          		# Mode/clear button , center top right
    Start: e.KEY_ENTER,         	# Start Button, center bottom left
    Select:  e.KEY_SPACE,        	# Select Button, center bottom right
    Btn_A:  e.KEY_LEFTCTRL,         # A Button, right bottom
    Btn_B: e.KEY_LEFTALT,           # B Button, right right
    Btn_X: e.KEY_Z,             	# X Button, right top
    Btn_Y: e.KEY_X,             	# Y Button, right down
    Btn_U: e.KEY_UP,          		# Up Button, left top
    Btn_L:  e.KEY_LEFT,       		# Left Button, left left
    Btn_R:  e.KEY_RIGHT,      		# Right Button, left right
    Btn_D: e.KEY_DOWN,        		# Down Button, left down
    Btn_LT: e.KEY_Q,            	# Left Trigger
    Btn_RT: e.KEY_W,            	# Right Trigger
}

os.system("sudo modprobe uinput")

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buttonList, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    ui = UInput({e.EV_KEY: keyList.values()}, name="retrogame", bustype=e.BUS_USB)
except uinput.UInputError as e:
    sys.stdout.write(e.message)
    sys.stdout.write("Have you tried running as root? sudo {}".format(sys.argv[0]))
    sys.exit(0)

def log(msg):
    sys.stdout.write(str(datetime.now()))
    sys.stdout.write(": ")
    sys.stdout.write(msg)
    sys.stdout.write("\n")
    sys.stdout.flush()

def handle_button(pin):
    key = keyList[pin]
    time.sleep(Debounce)
    if pin >= 1000:
      state = analog_states[pin-1000]
    else:
      state = 0 if gpio.input(pin) else 1
    ui.write(e.EV_KEY, key, state)
    ui.syn()
    if DEBUG:
        log("Pin: {}, KeyCode: {}, Event: {}".format(pin, key, 'press' if state else 'release'))


for button in buttonList:
    gpio.add_event_detect(button, gpio.BOTH, callback=handle_button, bouncetime=1)

while True:
	try:
		time.sleep(0.01)
	except KeyboardInterrupt:
		print("Stopping")
		sys.exit(0)


'''

buttonList = [
    [4,  uinput.KEY_VOLUMEUP],      # Right slider
    [27, uinput.KEY_VOLUMEDOWN],    # Left slider
    [17, uinput.KEY_MUTE],          # Click slider
    [5,  uinput.KEY_LEFTALT],             # Alt key/turbo button, center Top left
    [26, uinput.KEY_LEFTCTRL],          # Mode/clear button , center top right
    [20, uinput.KEY_ENTER],         # Start Button, center bottom left
    [6,  uinput.KEY_SPACE],        # Select Button, center bottom right
    [1,  uinput.KEY_A],             # A Button, right bottom
    [16, uinput.KEY_B],             # B Button, right right
    [24, uinput.KEY_X],             # X Button, right top
    [12, uinput.KEY_Y],             # Y Button, right down
    [11, uinput.KEY_UP],            # Up Button, left top
    [9,  uinput.KEY_LEFT],          # Left Button, left left
    [0,  uinput.KEY_RIGHT],         # Right Button, left right
    [13, uinput.KEY_DOWN],          # Down Button, left down
    [10, uinput.KEY_L],            # Left Trigger
    [23, uinput.KEY_R],            # Right Trigger
]



# Decontruct the lists that are indexed the same for recall
eventList = [item[1] for item in buttonList]
pinList = [item[0] for item in buttonList]
 
device = uinput.Device(eventList)

buttons = []

for pin in pinList:
    # create a button with 5ms bounce timer
    buttons.append(Button(pin, bounce_time=0.005))

time.sleep(0.125)

print('Ready')

while(1):
    for idx in range(0,len(pinList)):
        if(buttons[idx].is_pressed):
            #device.emit_click(eventList[idx])
            device.emit(eventList[idx], 1)
        else:
            device.emit(eventList[idx], 0)
    time.sleep(0.0165)
'''



