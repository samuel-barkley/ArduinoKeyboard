import os
import serial
from pynput.keyboard import Key, Controller
from pynput import keyboard
import re


pressesSinceCtrl = 0
pressesSinceC = 0
pressesnotCorCtrl = 0
lastKey = ' '
secondToLastKey = ' '

def on_press(key):
    global lastKey, pressesSinceC
    global secondToLastKey
    global pressesSinceCtrl

    try:
        if key.char == 'c':
            pressesSinceC += 1

        secondToLastKey = lastKey
        lastKey = key.char
    except AttributeError:
        if key == Key.ctrl_l:
            pressesSinceCtrl += 1
        secondToLastKey = lastKey
        lastKey = key

def handleInput():
    keyPressed = False
    global pressesSinceCtrl
    global pressesSinceC
    global lastKey
    global secondToLastKey

    arduino = serial.Serial('COM3', 9600, timeout=0.1)
    delay = 0

    shouldContinue = True

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while shouldContinue:
        data = arduino.readline()[:-2]  # deleting the new line chars
        if data:
            dataString = data.decode('utf-8')
            if not keyPressed:
                if dataString == "key00":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key00.ahk")
                elif dataString == "key01":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key01.ahk")
                elif dataString == "key02":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key02.ahk")
                elif dataString == "key03":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key03.ahk")
                elif dataString == "key10":

                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key10.ahk")
                elif dataString == "key11":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key11.ahk")
                elif dataString == "key12":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key12.ahk")
                elif dataString == "key13":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key13.ahk")
                elif dataString == "key20":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key20.ahk")
                elif dataString == "key21":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key21.ahk")
                elif dataString == "key22":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key22.ahk")
                elif dataString == "key23":
                    keyPressed = True
                    openApp("C:\\Users\\samue\\Documents\\Projects\\ArduinoKeyboard\\scripts\\Key23.ahk")

        else:
            # This delay is there because when you let go of a key it might register one last keypress.
            if delay > 0:
                keyPressed = False
                delay = 0
            else:
                delay += 1

        if lastKey == "0" and secondToLastKey == Key.f12:
            shouldContinue = False


def openApp(execLocation):
    os.startfile(execLocation)
    name = re.search("(\w+\.)", execLocation).group(0)[:-1]
    print(name)
