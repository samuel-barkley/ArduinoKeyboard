import os
import serial
from pynput.keyboard import Key, Controller

arduino = serial.Serial('COM3', 9600, timeout=0.1)
keyboard = Controller()
keyPressed = False
delay = 0

while True:
    data = arduino.readline()[:-2] # deleting the new line chars
    if data:
        dataString = data.decode('utf-8')
        if dataString == "key03" and not keyPressed:
            keyPressed = True
            appLocation = "C:\\Users\\samue\\Documents\\Projects\\Scripts\\AHK\\RunStreamlabs.ahk"
            os.startfile(appLocation)
            print("Opened Streamlabs")
    else:
        # This delay is there because when you let go of a key it might register one last keypress.
        if delay > 0:
            keyPressed = False
            delay = 0
        else:
            delay += 1
        

