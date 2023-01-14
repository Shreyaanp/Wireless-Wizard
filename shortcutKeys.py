import requests
import time
import serial
import pyautogui as pyag
from pynput.mouse import Button, Controller


def control_mouse():
    m = Controller()
    ser = serial.Serial('COM5',baudrate = 9600)       
    while 1:                                           
        res = ser.readline()                           
        res = str(res)                                
        res = res[2:-5]                               
        data = res.split(',')                         
        print(data)
        if data[0] == "DATAL":                        
            m.move(int(data[1]), int(data[2]))    
            if data[0] == "DATAB":                        
                if data[1] == 'L' :                      
                    m.press(Button.left)               
                    m.release(Button.left)
                if data[1] == 'R' :                     
                    m.press(Button.right)     
                    m.release(Button.right)
    

serial_read = serial.Serial('COM9',9600)
pyag.FAILSAFE=False

errorx=-10
errory=20

while True:
    arduino_output = serial_read.readline()
    decoded = arduino_output.decode().rstrip()
    decoded=decoded.split(",")
    print(arduino_output)
    if(len(decoded)==5):
        pyag.moveRel(float(decoded[3])-errorx,float(decoded[4])-errory)
    
    if decoded[0] == 1:
        pyag.hotkey("windows","shift","s")
        try:
            control_mouse()
        except:
            print("Mouse Error !!!")
            k=input("Press any key to exit")
    elif decoded[0]==2:
        pyag.hotkey("alt","Tab")
        try:
            control_mouse()
        except:
            print("Mouse Error !!!")
            k=input("Press any key to exit")
    
