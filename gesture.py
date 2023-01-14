import serial
from serial import Serial
from pynput.mouse import Button as but,Controller
from tkinter import *
import tkinter.font as font
from threading import Thread
import pyautogui as pyag

def menu():
  window=Tk()


  myFont = font.Font(size=10)

  window.geometry("1200x1200")




  btn1 = Button(window, text = 'Click Here !!!', bd = '5',
                            command = window.destroy,width=70,
      height=20,
      bg="#676161",
      fg="#dcd7d7",)
  btn2 = Button(window, text = 'Switch Tab', bd = '5',
                            command = switch_tab,width=70,
      height=20,
      bg="#676161",
      fg="#dcd7d7",)
  btn3 = Button(window, text = 'Take Screenshot', bd = '5',
                            command = take_ss,width=70,
      height=20,
      bg="#676161",
      fg="#dcd7d7",)
  btn4 = Button(window, text = 'Click Here !!!', bd = '5',
                            command = window.destroy,width=70,
      height=20,
      bg="#676161",
      fg="#dcd7d7",)
  btn1['font'] = myFont
  btn2['font'] = myFont
  btn3['font'] = myFont
  btn4['font'] = myFont

  btn1.place(x=20,y=30)
  btn3.place(x=620,y=30)
  btn2.place(x=20,y=400)
  btn4.place(x=620,y=400)



  window.mainloop()


def take_ss():
  pyag.hotkey("win","shift","s")
#   window.destroy()

def switch_tab():
  pyag.keyDown('alt')
  pyag.press('tab')
#   window.destroy()


def mouse():
    mouse = Controller()
    ser = serial.Serial('COM3',baudrate = 115200)       # Setting Serial port number and baudrate
    while 1:
        count = 0                             # While loop to continuesly scan and read data from serial port and execute
        dump = ser.readline()                           # Reading Serial port
        dump = str(dump)                                # Converting byte data into string
        dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
        data = dump.split(',')
        # print("hello")
                # Spliting up the data to individual items in a list. the first item being the data identifier
        print(data)                     # Calculating the difference between the current Y value and the previous Y value
        if(len(data)==5):
            if (data[0] == "DATAL" ):
                mouse.move(int(int(data[2])/1.6),int(int(data[1])/1.5))
        if(len(data)==2):
          if data[0] == "DATAB":                   # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
                if data[1] == 'L' :                       # If the Left button is pressed
                  mouse.press(but.left)                # The corresponding button is pressed and released
                  mouse.release(but.left)
                if data[1] == 'R' :                       # If the Right button is pressed
                        mouse.press(but.right)         # The corresponding button is pressed and released
                        mouse.release(but.right)

Thread(target=menu).start()
Thread(target=mouse).start()