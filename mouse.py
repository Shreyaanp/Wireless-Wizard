import serial
import time
from serial import Serial
from pynput.mouse import Button as but, Controller
from tkinter import *
import tkinter.font as font
import pygame
import random
import tkinter.font as font
from threading import Thread

def show_menu():

  window=Tk()


  myFont = font.Font(size=10)

  window.geometry("1200x1200")




  btn1 = Button(window, text = 'Take Screenshot', bd = '5',
                            command = window.destroy,width=70,
      height=20,
      bg="#676161",
      fg="#dcd7d7",)
  btn2 = Button(window, text = 'Switch Tab', bd = '5',
                            command = window.destroy,width=70,
      height=20,
      bg="#676161",
      fg="#dcd7d7",)
  btn3 = Button(window, text = 'Voice Control', bd = '5',
                            command = window.destroy,width=70,
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


def Mouse():
  mouse = Controller()
  try:
    ser = serial.Serial('COM3',baudrate = 115200)       # Setting Serial port number and baudrate
    while 1:
        count = 0
        dump = ser.readline()
        dump = str(dump)
        dump = dump[2:-5]
        data = dump.split(',')
        # print("hello")

        print(data)
        if(len(data)==4):
          if (data[0] == "DATAL" ):
            mouse.move(int(int(data[2])/1.3),int(int(data[1])/1.3))
        if(len(data)==2):
          if data[0] == "DATAB":                   # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
                if data[1] == 'L' :                       # If the Left button is pressed
                  mouse.press(but.left)                # The corresponding button is pressed and released
                  mouse.release(but.left)
                if data[1] == 'R' :                       # If the Right button is pressed
                        mouse.press(but.right)         # The corresponding button is pressed and released
                        mouse.release(but.right)

  except Exception as e:
    print(e)
    k=input("Press any key to exit.")

Mouse()
