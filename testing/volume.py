import uinput
import time
from gpiozero import Button
from signal import pause

device = uinput.Device([
    uinput.KEY_VOLUMEUP,
    uinput.KEY_VOLUMEDOWN,
    uinput.KEY_MUTE,
])

time.sleep(0.125)

def pressVUP():
    device.emit_click(uinput.KEY_VOLUMEUP)

def pressVDN():
    device.emit_click(uinput.KEY_VOLUMEDOWN)

def pressVMU():
    device.emit_click(uinput.KEY_MUTE)


btn_VUP = Button(4)
btn_VUP.when_pressed = pressVUP
btn_VDN = Button(27)
btn_VDN.when_pressed = pressVDN
btn_VMU = Button(17)
btn_VMU.when_pressed = pressVMU

print('Ready')
pause()
