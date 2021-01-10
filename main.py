
import serial
from pynput.keyboard import Key, Controller

arduino = serial.Serial('COM3', 9600, timeout=0.1)
keyboard = Controller()

test0 = "b\'on\'"

while True:
    data = arduino.readline()[:-2] # deleting the new line chars
    if data:
        #keyboard.press(Key.a)
        #keyboard.type(data)
        #data.
        print(data)