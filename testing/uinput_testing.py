# make sure uinput is installed (sudo pip install python-uinput)
# then run sudo modprobe uinput to make sure it's active.
# must run as sudo, see example for drop priviledges (which we may not care)


import uinput
import time

device = uinput.Device([
	uinput.KEY_E,
	uinput.KEY_H,
	uinput.KEY_L,
	uinput.KEY_O,
	])

# it seems to need a delay before we can do stuff
# 0.125s seems to work, 0.1 doesn't and that's good enough for a first time startup delay
# this seems to be true of the dev's examples too. This might be RPi-specific
time.sleep(0.125)

device.emit_click(uinput.KEY_H)
device.emit_click(uinput.KEY_E)
device.emit_click(uinput.KEY_L)
device.emit_click(uinput.KEY_L)
device.emit_click(uinput.KEY_O)
