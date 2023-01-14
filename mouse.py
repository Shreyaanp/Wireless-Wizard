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
def defmouse():
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


def game():


  # Initialize Pygame
  pygame.init()

  # Set the screen size and caption
  size = (700, 500)
  screen = pygame.display.set_mode(size)
  pygame.display.set_caption("Wireless Wizzard")

  # Set the background color
  bg_color = (255, 255, 255)

  # Create a variable to control the game loop
  running = True

  # Create a variable to store the cursor position
  cursor_pos = [350, 250]

  # Create a variable to store the dot position
  dot_pos = [random.randint(0,700), random.randint(0,500)]

  # Start the game loop
  while running:

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          elif event.type == pygame.MOUSEBUTTONDOWN:

              if (cursor_pos[0]-dot_pos[0])*2 + (cursor_pos[1]-dot_pos[1])**2 < 50*2:

                  dot_pos = [random.randint(0,700), random.randint(0,500)]

      cursor_pos = pygame.mouse.get_pos()


      screen.fill(bg_color)

      # Draw the cursor at the updated position
      pygame.draw.circle(screen, (255, 0, 0), cursor_pos, 10)

      # Draw the dot at the random position
      pygame.draw.circle(screen, (0, 255, 0), dot_pos, 50)

      # Update the screen
      pygame.display.flip()

  # Exit Pygame
  pygame.quit()

def Mouse():
  mouse = Controller()
  try:
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
          while(True):
            dump = ser.readline()                           # Reading Serial port
            dump = str(dump)                                # Converting byte data into string
            dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
            data = dump.split(',')
            if(len(data)==5):
              if(int(data[4]) <15 and int(data[4])>5):
                count = count + 1
              else:
                break
              if(count == 8):
                ser.close()
                Thread(target=show_menu).start()
                Thread(target=defmouse).start()
            if(len(data)==5):
              if(int(data[4]) >15 and int(data[4])<25):
                count = count + 1
              else:
                break
              if(count == 8):
                ser.close()
                Thread(target=game).start()
                Thread(target=defmouse).start()


        if(len(data)==2):
          if data[0] == "DATAB":
                if data[1] == 'L' :
                  mouse.press(but.left)
                  mouse.release(but.left)
                  count1=0
                  while (len(data)==2 and count1<=5):
                    count1+=1

                    dump = ser.readline()

                    dump = str(dump)
                    dump = dump[2:-5]
                    data = dump.split(',')

                if data[1] == 'R' :
                        mouse.press(but.right)
                        mouse.release(but.right)




  except Exception as e:
    print(e)
    k=input("Press any key to exit.")

Mouse()
