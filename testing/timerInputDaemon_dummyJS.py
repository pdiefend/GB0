#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import os, sys
import time
import uinput


buttonList = [
    [4,  uinput.KEY_VOLUMEUP],      # Right slider
    [27, uinput.KEY_VOLUMEDOWN],    # Left slider
    [17, uinput.KEY_MUTE],          # Click slider
    [5,  uinput.KEY_T],             # Alt key/turbo button, center Top left
    [26, uinput.BTN_MODE],          # Mode/clear button , center top right
    [20, uinput.BTN_START],         # Start Button, center bottom left
    [6,  uinput.BTN_SELECT],        # Select Button, center bottom right
    [1,  uinput.BTN_A],             # A Button, right bottom
    [16, uinput.BTN_B],             # B Button, right right
    [24, uinput.BTN_X],             # X Button, right top
    [12, uinput.BTN_Y],             # Y Button, right down
    [11, uinput.BTN_DPAD_UP],            # Up Button, left top
    [9,  uinput.BTN_DPAD_LEFT],          # Left Button, left left
    [0,  uinput.BTN_DPAD_RIGHT],         # Right Button, left right
    [13, uinput.BTN_DPAD_DOWN],          # Down Button, left down
    [10, uinput.BTN_TL],            # Left Trigger
    [23, uinput.BTN_TR],            # Right Trigger
]

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

'''

# Decontruct the lists that are indexed the same for recall
eventList = [item[1] for item in buttonList]
pinList = [item[0] for item in buttonList]
		
# add the joystick axes to the event list
#eventList.append(uinput.ABS_X + (0, 255, 0, 0))
#eventList.append(uinput.ABS_Y + (0, 255, 0, 0))
		    
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
        
        #fill joystick up with dummy info so we have something to read
        #device.emit(uinput.ABS_X, (idx*10), syn=False)
        #device.emit(uinput.ABS_Y, (idx*10))

    time.sleep(0.0165)


