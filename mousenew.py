import serial
from serial import Serial
from pynput.mouse import Button, Controller
from tkinter import *
import tkinter.font as font
 
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

def move_mouse():
  mouse = Controller()
  try:
    ser = serial.Serial('COM3',baudrate = 9600)       # Setting Serial port number and baudrate
    while 1:                                            # While loop to continuesly scan and read data from serial port and execute
        dump = ser.readline()                           # Reading Serial port
        dump = str(dump)                                # Converting byte data into string
        dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
        data = dump.split(',')                          # Spliting up the data to individual items in a list. the first item being the data identifier
        print(data)
        if data[0] == "DATAL":                          # Checking if the identifier is "DATAL" which the Arduino sends the data as the gyro X, Y and Z values
          mouse.move(int(data[1]), int(data[2]))        # Moving the mouse by using the X and Y values after converting them into integer

        if data[0] == "DATAB":                          # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
              if data[1] == 'L' :                       # If the Left button is pressed
                mouse.press(Button.left)                # The corresponding button is pressed and released
                mouse.release(Button.left)
              if data[1] == 'R' :                       # If the Right button is pressed
                      mouse.press(Button.right)         # The corresponding button is pressed and released
                      mouse.release(Button.right)
  except:
    print("Mouse not found or disconnected.")
    k=input("Press any key to exit.")



mouse = Controller()
try:
  ser = serial.Serial('COM9',baudrate = 9600)       # Setting Serial port number and baudrate
  while 1:                                        # While loop to continuesly scan and read data from serial port and execute
      dump = ser.readline()                           # Reading Serial port
      dump = str(dump)                                # Converting byte data into string
      dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
      data = dump.split(',')
      # print("hello")
                      # Spliting up the data to individual items in a list. the first item being the data identifier
      print(data)                     # Calculating the difference between the current Y value and the previous Y value
      if(len(data)==4):
        if (data[0] == "DATAL" ):
          mouse.move(int(int(data[2])/1.6),int(int(data[1])/1.5))
                     # Checking if the identifier is "DATAL" which the Arduino sends the data as the gyro X, Y and Z values
                # Moving the mouse by using the X and Y values after converting them into integer
      if(len(data)==2):
        if data[0] == "DATAB":
                                  # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
              if data[1] == 'L' :                       # If the Left button is pressed
                mouse.press(Button.left)                # The corresponding button is pressed and released
                mouse.release(Button.left)
              if data[1] == 'R' :                       # If the Right button is pressed
                      mouse.press(Button.right)         # The corresponding button is pressed and released
                      mouse.release(Button.right)
      if(len(data)==1):
        if(data[0]=="SENSOR ACTIVE!!!"):
            while data[0]=="SENSOR ACTIVE":
                dump = ser.readline()                           # Reading Serial port
                dump = str(dump)                                # Converting byte data into string
                dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
                data = dump.split(',')
            show_menu()
      #limit the loop to 10 times per second
      #limit the mouse position to alittle less than screen size
      if mouse.position[0] > 1200 and mouse.position[1] > 720 :
        mouse.position = (1200, mouse.position[1])
        mouse.position = (mouse.position[0], 720)

except Exception as e:
  print(e)
  k=input("Press any key to exit.")