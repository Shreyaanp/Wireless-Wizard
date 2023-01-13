import serial
import time
from serial import Serial
from pynput.mouse import Button, Controller

mouse = Controller()
try:
  ser = serial.Serial('COM3',baudrate = 9600)       # Setting Serial port number and baudrate
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
          mouse.move(int(int(data[2])/1.5),int(int(data[1])/1.5))
                     # Checking if the identifier is "DATAL" which the Arduino sends the data as the gyro X, Y and Z values
                # Moving the mouse by using the X and Y values after converting them into integer
      if(len(data)==2):
        if data[0] == "DATAB":
              time.sleep(1)                         # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
              if data[1] == 'L' :                       # If the Left button is pressed
                mouse.press(Button.left)                # The corresponding button is pressed and released
                mouse.release(Button.left)
              if data[1] == 'R' :                       # If the Right button is pressed
                      mouse.press(Button.right)         # The corresponding button is pressed and released
                      mouse.release(Button.right)

except Exception as e:
  print(e)
  k=input("Press any key to exit.")