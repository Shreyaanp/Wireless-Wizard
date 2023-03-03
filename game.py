import pygame
import random
import serial
from serial import Serial
from pynput.mouse import Button as but,Controller
from tkinter import *
import tkinter.font as font
from threading import Thread

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
        if(len(data)==4):
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
# Initialize Pygame
def game():

    # Initialize Pygame
    pygame.init()

    # Set the screen size and caption
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mouse Game")

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
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the cursor is within the dot
                if (cursor_pos[0]-dot_pos[0])*2 + (cursor_pos[1]-dot_pos[1])**2 < 50*2:
                    # Generate a new random dot position
                    dot_pos = [random.randint(0,700), random.randint(0,500)]
        # Get the mouse position
        cursor_pos = pygame.mouse.get_pos()

        # Clear the screen
        screen.fill(bg_color)

        # Draw the cursor at the updated position
        pygame.draw.circle(screen, (255, 0, 0), cursor_pos, 10)

        # Draw the dot at the random position
        pygame.draw.circle(screen, (0, 255, 0), dot_pos, 50)

        # Update the screen
        pygame.display.flip()

    # Exit Pygame
    pygame.quit()

Thread(target=game).start()
Thread(target=mouse).start()